// Simple login page - for demo stores a fake token on success
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginSuccess } from "../services/auth";
import api from "../services/api";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      const res = await api.post('/auth/login', { username: email, password });
      // if backend returns a token, persist it
      if (res?.data?.access_token) loginSuccess(res.data.access_token);
      navigate("/");
    } catch (err) {
      console.error(err);
      setError("Login failed");
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-b from-slate-50 to-white">
      <div className="w-full max-w-md bg-white rounded-lg shadow p-6">
        <h2 className="text-2xl font-semibold mb-4">Sign in to EduInsight</h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="text-sm">Username or Email</label>
            <input
              className="w-full border rounded px-3 py-2"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>

          <div>
            <label className="text-sm">Password</label>
            <input
              type="password"
              className="w-full border rounded px-3 py-2"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>

          {error && <div className="text-red-600 text-sm">{error}</div>}

          <div>
            <button className="w-full bg-primary-500 text-white rounded px-4 py-2">
              Sign in
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}