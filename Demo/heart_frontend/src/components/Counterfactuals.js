const labels = {
  trestbps: "Blood Pressure",
  oldpeak: "ST Depression",
  thalch: "Heart Rate",
  chol: "Cholesterol",
  ca: "Major Vessels",
};

function Counterfactuals({ data }) {
  if (!data || data.length === 0) return null;

  return (
    <div style={box}>
      <h3>Recommended Changes</h3>

      {data.map((c, i) => (
        <p key={i}>
          {c.to > c.from ? "Increase" : "Decrease"}{" "}
          <b>{labels[c.feature] || c.feature}</b> from {c.from} → {c.to}
        </p>
      ))}
    </div>
  );
}

const box = {
  background: "white",
  padding: "15px",
  marginTop: "20px",
  borderRadius: "10px",
};

export default Counterfactuals;
