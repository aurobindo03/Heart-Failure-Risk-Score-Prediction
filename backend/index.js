import express from "express";
import cors from "cors";
import hrsRoute from "./hrs.js";
import axios from "axios";
const app = express();
app.use(cors());
app.use(express.json());
app.post("/analyze", async (req, res) => {
  try {
    const input = req.body;

    // 👉 your HRS logic (or keep simple for now)
    let score = 0;

    if (input.trestbps > 140) score += 0.5;
    if (input.oldpeak > 2) score += 0.5;

    const risk = score > 0.7 ? "High" : "Moderate";

    // 👉 call Python (DiCE)
    let counterfactuals = [];

    try {
      const response = await axios.post(
        "http://localhost:6000/counterfactual",
        input,
      );

      counterfactuals = response.data;
    } catch (err) {
      console.log("Python API not running");
    }

    res.json({
      risk_score: score,
      risk_level: risk,
      top_features: [],
      counterfactuals,
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});
// ==============================

// existing routes (if any)

app.listen(5000, () => {
  console.log("Server running on port 5000");
});
app.use("/api/hrs", hrsRoute);

const PORT = 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));