# Heart Failure Risk Score Prediction — Professor Presentation Deck

> Use this as a ready-to-deliver script. Each slide includes **on-slide content** and **speaker notes**.

---

## Slide 1 — Title
**On-slide content**
- **Heart Failure Risk Score Prediction**
- Major Project Presentation
- Team: Arpit Mishra, Aditya Srivastav, Aurobindo Subudhi

**Speaker notes**
- Good morning/afternoon, Professor.
- This presentation summarizes our end-to-end machine learning workflow for heart failure risk prediction, from data preparation to clinical interpretation.

---

## Slide 2 — Agenda
**On-slide content**
1. Clinical motivation and problem statement
2. Dataset and preprocessing
3. Model building and Hybrid Risk Score (HRS)
4. Evaluation and threshold optimization
5. Explainability and counterfactual analysis
6. Final conclusions and future work

**Speaker notes**
- I’ll walk from motivation to deployment relevance, and conclude with key findings and next steps.

---

## Slide 3 — Why this problem matters
**On-slide content**
- Cardiovascular disease remains a major cause of mortality.
- Early risk detection can improve intervention decisions.
- Need both **predictive accuracy** and **clinical interpretability**.

**Speaker notes**
- In healthcare, raw accuracy alone is not enough.
- Models must support actionable, explainable decision-making.

---

## Slide 4 — Project objectives
**On-slide content**
- Build and compare LR, Random Forest, XGBoost, and CatBoost.
- Develop/assess a Hybrid Risk Score (HRS).
- Evaluate with discrimination + calibration + clinical utility.
- Optimize thresholds for real-world sensitivity/specificity trade-off.

**Speaker notes**
- This is why we included ROC-AUC, calibration, Brier score, and decision curve analysis rather than relying on one metric.

---

## Slide 5 — Dataset overview
**On-slide content**
- Rows: **920**
- Columns: **22**
- Structured clinical feature set for heart disease risk modeling.

**Speaker notes**
- The dataset size is moderate; this required careful validation to avoid overfitting.

---

## Slide 6 — Preprocessing and EDA
**On-slide content**
- Data cleaning and formatting.
- Train/test split exported as cleaned datasets.
- Exploratory analysis:
  - Class distribution
  - Correlation heatmap

**Speaker notes**
- Preprocessing quality is foundational.
- We used visual checks to understand imbalance and feature relationships before model training.

---

## Slide 7 — Model training setup
**On-slide content**
- Random Forest: n_estimators=200
- XGBoost: n_estimators=200, max_depth=4, learning_rate=0.05
- CatBoost: n_estimators=200, max_depth=4, learning_rate=0.05

**Speaker notes**
- We used controlled, comparable settings to ensure fair evaluation across tree-based models.

---

## Slide 8 — Model performance (core metrics)
**On-slide content**
- **CatBoost:** Accuracy 0.9022, F1 0.9151, AUC 0.9806
- **XGBoost:** Accuracy 0.9022, F1 0.9143, AUC 0.9787
- **RF:** Accuracy 0.8696, F1 0.8857, AUC 0.9600
- **LR:** Accuracy 0.8641, F1 0.8848, AUC 0.9406
- **HRS:** Accuracy 0.7228, F1 0.7512, AUC 0.8009

**Speaker notes**
- CatBoost and XGBoost are top performers by discrimination.
- HRS is not the top raw predictor but serves interpretability and clinical framing.

---

## Slide 9 — ROC and confusion matrix insights
**On-slide content**
- ROC curves confirm superior discrimination for CatBoost/XGBoost.
- Confusion matrices expose FP/FN trade-offs.
- Clinical settings often prioritize sensitivity at acceptable specificity.

**Speaker notes**
- We focused on balancing missed positives and false alarms rather than maximizing a single score.

---

## Slide 10 — Hybrid Risk Score (HRS)
**On-slide content**
- HRS used as an interpretable risk stratification layer.
- Risk categories mapped to patient-level score outputs.
- Supports communication and triage discussions.

**Speaker notes**
- Even when pure ML model is stronger, clinicians benefit from transparent risk categories.

---

## Slide 11 — Aurobindo’s major contribution
**On-slide content**
- **Threshold Optimization + Final Integration**
- Responsibilities:
  - Calibration Curve
  - Brier Score
  - Decision Curve Analysis
  - Threshold optimization using Youden J-stat
  - Final summary consolidation

**Speaker notes**
- This stage converted model probabilities into clinically usable decision cutoffs.

---

## Slide 12 — Threshold optimization results
**On-slide content**
- LR optimal threshold: 0.60
- RF optimal threshold: 0.50
- XGBoost optimal threshold: 0.45
- CatBoost optimal threshold: 0.45
- HRS optimal threshold: 0.55

**Speaker notes**
- Thresholds were tuned to improve operating balance beyond the default 0.5 rule.

---

## Slide 13 — Final integrated model summary
**On-slide content**
- **CatBoost (thr 0.45):** AUC 0.9806, Brier 0.0862, Accuracy 0.9239
- **XGBoost (thr 0.45):** AUC 0.9787, Brier 0.0839, Accuracy 0.9293
- Clinical score leaders: CatBoost and XGBoost

**Speaker notes**
- XGBoost has slightly better accuracy and Brier; CatBoost has slightly better AUC and matched precision/recall balance.

---

## Slide 14 — Calibration and Brier score
**On-slide content**
- Calibration curves assess probability reliability.
- Lower Brier score indicates better probabilistic quality.
- Strong calibration strengthens trust in risk communication.

**Speaker notes**
- For healthcare decisions, calibrated probabilities are as important as classification labels.

---

## Slide 15 — Decision Curve Analysis (DCA)
**On-slide content**
- DCA evaluates **net clinical benefit** across thresholds.
- Confirms practical benefit of model-guided decisions.
- Supports threshold choices for screening/intervention.

**Speaker notes**
- This bridges data science performance to clinical utility.

---

## Slide 16 — SHAP explainability
**On-slide content**
- Global SHAP (beeswarm/bar) identifies influential features.
- Local explanations (force/waterfall) support patient-level rationale.
- Improves interpretability and model transparency.

**Speaker notes**
- Explainability helps clinicians understand “why” behind each risk estimate.

---

## Slide 17 — Counterfactual analysis
**On-slide content**
- Counterfactuals propose feasible feature changes.
- Demonstrated substantial risk reduction in sample patients.
- Enables actionable, personalized guidance.

**Speaker notes**
- This turns predictions into intervention ideas.

---

## Slide 18 — Team contributions
**On-slide content**
- **Arpit:** data preprocessing and data-quality pipeline.
- **Aditya:** model evaluation and comparative benchmarking.
- **Aurobindo:** threshold optimization, calibration, DCA, and final integration.

**Speaker notes**
- The project was modular, with each stage integrated into one coherent workflow.

---

## Slide 19 — Limitations and future work
**On-slide content**
- Need external validation on independent cohorts.
- Potential shift across populations/hospitals.
- Future: prospective validation and clinical decision-support deployment.

**Speaker notes**
- Next priority is generalizability and real-world operational testing.

---

## Slide 20 — Closing
**On-slide content**
- Key takeaway: high-performing, explainable, clinically-aware risk prediction pipeline.
- Thank you.
- Questions?

**Speaker notes**
- I can now take questions on model choice, thresholding rationale, or explainability workflow.

---

## Appendix — Slide assets mapping (for quick PPT build)
- Figures folder assets to embed:
  - class_distribution.png
  - correlation_heatmap.png
  - Plot12_ROC_Curves (1).png
  - Plot12b_Confusion_Matrices.png
  - hrs_score_distribution.png
  - Plot15_Calibration_Curve.png
  - Plot16_Decision_Curve_Analysis.png
  - Plot18_Threshold_Optimization_Curves.png
  - xgboost_shap_beeswarm.png
  - Counterfactual_Impact_updated.png
- Tables to include directly as snapshots or editable tables:
  - Table11__Model_Performance_Comparison.csv
  - Table14_Threshold_Optimization.csv
  - Table15_Final_Summary.csv
  - model_training_summary.csv
  - T1_dataset_overview.csv
