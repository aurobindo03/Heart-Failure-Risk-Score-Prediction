import React, { useState } from "react";
import axios from "axios";
import InputForm from "../components/InputForm";
import ResultCard from "../components/ResultCard";
import SHAPInsights from "../components/SHAPInsights";
import Counterfactuals from "../components/Counterfactuals";

function Predictor() {
  const [result, setResult] = useState(null);

  

  const analyzePatient = async (data) => {
    try {
      // 1️⃣ CALL HRS
      const res = await axios.post("http://localhost:5000/api/hrs", data);
      const hrs = res.data;

      let cfData = [];

      // 2️⃣ IF HIGH → CALL COUNTERFACTUAL
      if (hrs.risk === "High") {
        const cfRes = await axios.post(
          "http://localhost:6000/counterfactual",
          data,
        );
        cfData = cfRes.data;
      }

      // 3️⃣ SAVE EVERYTHING
      setResult({
        risk_score: hrs.hrs_score,
        risk_level: hrs.risk,
        top_features: hrs.top_features,
        counterfactuals: cfData,
      });
    } catch (err) {
      console.error(err);
      alert("Something went wrong.");
    }
  };

  return (
    <div>
      <InputForm onSubmit={analyzePatient} />

      {result && (
        <>
          <ResultCard data={result} />
          <SHAPInsights features={result.top_features} />

          {result.counterfactuals.length > 0 && (
            <Counterfactuals data={result.counterfactuals} />
          )}
        </>
      )}
    </div>
  );
}

export default Predictor;
