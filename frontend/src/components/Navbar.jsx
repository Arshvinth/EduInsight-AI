// Top navigation with simple search and user avatar
import React from "react";
import { logout } from "../services/auth";
import { useNavigate } from "react-router-dom";

export default function Navbar() {
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <header className="bg-white border-b">
      <div className="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
        <div className="flex items-center gap-4">
          <h1 className="text-xl font-semibold text-slate-700">EduInsight</h1>
          <div className="hidden md:block">
            <input
              className="border rounded-md px-3 py-1 text-sm"
              placeholder="Search students, modules..."
            />
          </div>
        </div>

        <div className="flex items-center gap-4">
          <button
            onClick={() => navigate("/ml/risk")}
            className="text-sm text-slate-600 hover:text-slate-800"
          >
            Predict Risk
          </button>

          <div className="flex items-center gap-2">
            <div className="text-sm text-slate-700">Admin</div>
            <button
              onClick={handleLogout}
              className="bg-primary-500 text-white rounded px-3 py-1 text-sm"
            >
              Logout
            </button>
          </div>
        </div>
      </div>
    </header>
  );
}