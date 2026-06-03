// Reusable card component
import React from "react";

export default function Card({ title, children, className = "" }) {
  return (
    <div className={`bg-white shadow-sm rounded-lg p-4 ${className}`}>
      {title && <h3 className="font-semibold mb-2">{title}</h3>}
      {children}
    </div>
  );
}