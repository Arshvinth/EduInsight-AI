// Document upload UI using form-data to backend /ai/upload-document
import React, { useState } from "react";
import Card from "../components/Card";
import api from "../services/api";

export default function Documents() {
  const [file, setFile] = useState(null);
  const [title, setTitle] = useState("");
  const [message, setMessage] = useState("");

  async function handleUpload(e) {
    e.preventDefault();
    if (!file) return setMessage("Choose a file first");

    const form = new FormData();
    form.append("file", file);
    if (title) form.append("title", title);

    try {
      const res = await api.post("/ai/upload-document", form, {
        headers: { "Content-Type": "multipart/form-data" }
      });
      setMessage(`Uploaded: ${res.data.filename}`);
    } catch (err) {
      console.error(err);
      setMessage("Upload failed");
    }
  }

  return (
    <div>
      <h2 className="text-lg font-semibold mb-4">Upload Document (PDF / DOCX)</h2>
      <Card>
        <form onSubmit={handleUpload} className="space-y-4">
          <div>
            <label className="text-sm block mb-1">File</label>
            <input
              type="file"
              accept=".pdf,.docx"
              onChange={(e) => setFile(e.target.files[0])}
            />
          </div>

          <div>
            <label className="text-sm block mb-1">Title (optional)</label>
            <input
              className="border rounded px-3 py-2 w-full"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
            />
          </div>

          <div>
            <button className="bg-primary-500 text-white px-4 py-2 rounded">
              Upload
            </button>
          </div>

          {message && <div className="text-sm text-slate-600">{message}</div>}
        </form>
      </Card>
    </div>
  );
}