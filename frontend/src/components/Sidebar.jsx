// Sidebar navigation links
import React from "react";
import { NavLink } from "react-router-dom";

const links = [
  { to: "/", label: "Dashboard" },
  { to: "/students", label: "Students" },
  { to: "/modules", label: "Modules" },
  { to: "/documents", label: "Documents" },
  { to: "/ai-chat", label: "AI Chat" }
];

export default function Sidebar() {
  return (
    <aside className="w-64 bg-white border-r hidden md:block">
      <div className="p-6">
        <div className="mb-6">
          <h2 className="text-lg font-bold">EduInsight</h2>
          <p className="text-sm text-slate-500">Academic assistant</p>
        </div>

        <nav className="space-y-1">
          {links.map((l) => (
            <NavLink
              key={l.to}
              to={l.to}
              className={({ isActive }) =>
                `block px-3 py-2 rounded-md text-sm ${
                  isActive ? "bg-primary-50 text-primary-600" : "text-slate-700 hover:bg-slate-50"
                }`
              }
            >
              {l.label}
            </NavLink>
          ))}
        </nav>
      </div>
    </aside>
  );
}