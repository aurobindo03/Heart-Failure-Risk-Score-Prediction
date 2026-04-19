from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib
import dice_ml
from dice_ml import Dice

app = Flask(__name__)
CORS(app)

# ======================
# LOAD DATA + MODEL
# ======================
df = pd.read_csv("cleaned_train.csv")

TARGET = "target"
X = df.drop(columns=[TARGET])

rf = joblib.load("rf_model.pkl")

# ======================
# DICE SETUP
# ======================
data_dice = dice_ml.Data(
    dataframe=df,
    continuous_features=list(X.columns),
    outcome_name=TARGET
)

model_dice = dice_ml.Model(model=rf, backend="sklearn")
dice = Dice(data_dice, model_dice)

# ======================
# SETTINGS
# ======================
features_to_vary_default = ['trestbps', 'oldpeak', 'thalch', 'chol', 'ca']

permitted_range = {
    'trestbps': [80, 200],
    'oldpeak': [0, 6],
    'thalch': [60, 200],
    'chol': [100, 400],
    'ca': [0, 3]
}

# ======================
# MAIN API
# ======================
@app.route("/counterfactual", methods=["POST"])
def generate_cf():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No input data provided"}), 400

        hrs_risk = data.get("risk")

        if hrs_risk != "High":
            return jsonify({
                "message": "Counterfactuals only for high-risk patients",
                "counterfactuals": []
            })

        # -----------------
        # INPUT → DF
        # -----------------
        query = pd.DataFrame([data])

        if "thalach" in query.columns:
            query.rename(columns={"thalach": "thalch"}, inplace=True)

        for col in X.columns:
            if col not in query.columns:
                query[col] = 0

        query = query[X.columns]

        # -----------------
        # FEATURES TO VARY
        # -----------------
        features_to_vary = data.get("top_features", [])

        if not isinstance(features_to_vary, list):
            features_to_vary = []

        if not features_to_vary:
            features_to_vary = features_to_vary_default

        # keep only valid columns
        features_to_vary = [f for f in features_to_vary if f in X.columns]

        # -----------------
        # DICE GENERATION
        # -----------------
        cf = dice.generate_counterfactuals(
            query,
            total_CFs=5,
            desired_class=0,
            features_to_vary=features_to_vary,
            permitted_range=permitted_range
        )

        cf_list = cf.cf_examples_list[0].final_cfs_df

        if cf_list is None or cf_list.empty:
            return jsonify({
                "message": "No counterfactuals found",
                "counterfactuals": []
            })

        # -----------------
        # FORMAT OUTPUT
        # -----------------
        results = []

        for i in range(len(cf_list)):
            changes = []

            for col in features_to_vary:
                original = float(query.iloc[0][col])
                new = float(cf_list.iloc[i][col])

                if abs(original - new) > 0.1:
                    changes.append({
                        "feature": col,
                        "from": round(original, 2),
                        "to": round(new, 2),
                        "change": "increase" if new > original else "decrease"
                    })

            results.append({
                "recommendation": i + 1,
                "changes": changes
            })

        return jsonify({
            "total_recommendations": len(results),
            "counterfactuals": results
        })

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


# ======================
# RUN SERVER
# ======================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)