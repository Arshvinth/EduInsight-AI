// Simple form to call ML endpoint /ml/predict-risk
import React, { useState } from "react";
import Card from "../components/Card";
import api from "../services/api";

export default function RiskPrediction() {
  const [form, setForm] = useState({
    attendance: 75,
    cgpa: 6.5,
    failed_modules: 0,
    recent_marks: 70
  });
  const [result, setResult] = useState(null);

  const handleChange = (k, v) => setForm({ ...form, [k]: v });

  async function submit(e) {
    e.preventDefault();
    try {
      const res = await api.post("/ml/predict-risk", form);
      setResult(res.data);
    } catch (err) {
      console.error(err);
      setResult({ error: err.message });
    }
  }

  return (
    <div>
      <h2 className="text-lg font-semibold mb-4">Student Risk Prediction</h2>
      <Card>
        <form onSubmit={submit} className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="text-sm">Attendance (%)</label>
            <input
              type="number"
              className="w-full border rounded px-3 py-2"
              value={form.attendance}
              onChange={(e) => handleChange("attendance", Number(e.target.value))}
            />
          </div>

          <div>
            <label className="text-sm">CGPA</label>
            <input
              type="number"
              step="0.1"
              className="w-full border rounded px-3 py-2"
              value={form.cgpa}
              onChange={(e) => handleChange("cgpa", Number(e.target.value))}
            />
          </div>

          <div>
            <label className="text-sm">Failed Modules</label>
            <input
              type="number"
              className="w-full border rounded px-3 py-2"
              value={form.failed_modules}
              onChange={(e) =>
                handleChange("failed_modules", Number(e.target.value))
              }
            />
          </div>

          <div>
            <label className="text-sm">Recent Marks (avg)</label>
            <input
              type="number"
              className="w-full border rounded px-3 py-2"
              value={form.recent_marks}
              onChange={(e) => handleChange("recent_marks", Number(e.target.value))}
            />
          </div>

          <div className="md:col-span-2">
            <button className="bg-primary-500 text-white px-4 py-2 rounded">Predict</button>
          </div>
        </form>

        {result && (
          <div className="mt-4">
            <div className="font-semibold">Result</div>
            <div className="mt-2 bg-slate-50 p-3 rounded">
              {result.prediction ? (
                <>
                  <div>Prediction: <strong>{result.prediction}</strong></div>
                  <div>Risk score: <strong>{result.risk_score}</strong></div>
                </>
              ) : (
                <div className="text-red-600">Error: {result.error}</div>
              )}
            </div>
          </div>
        )}
      </Card>
    </div>
  );
}