// Chat UI that sends query to /ai/chat endpoint and displays context + answer
import React, { useState } from "react";
import Card from "../components/Card";
import api from "../services/api";

export default function AIChat() {
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");
  const [matched, setMatched] = useState([]);

  async function handleAsk(e) {
    e.preventDefault();
    try {
      const res = await api.post("/ai/chat", { query });
      setAnswer(res.data.answer);
      setMatched(res.data.matched_chunks || []);
    } catch (err) {
      console.error(err);
      setAnswer("Error: " + (err.response?.data?.detail || err.message));
    }
  }

  return (
    <div>
      <h2 className="text-lg font-semibold mb-4">AI Chat (RAG)</h2>
      <Card>
        <form onSubmit={handleAsk} className="space-y-3">
          <textarea
            className="w-full border rounded px-3 py-2"
            rows={4}
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Ask a question about uploaded documents or courses..."
          />
          <div>
            <button className="bg-primary-500 text-white px-4 py-2 rounded">
              Ask
            </button>
          </div>
        </form>

        {answer && (
          <div className="mt-4">
            <h4 className="font-semibold">Answer</h4>
            <div className="mt-2 p-3 bg-slate-50 rounded">{answer}</div>

            <h4 className="font-semibold mt-4">Matched Chunks</h4>
            <div className="mt-2 space-y-2 text-sm text-slate-600">
              {matched.map((m, i) => (
                <div key={i} className="p-2 border rounded bg-white">
                  {m}
                </div>
              ))}
            </div>
          </div>
        )}
      </Card>
    </div>
  );
}