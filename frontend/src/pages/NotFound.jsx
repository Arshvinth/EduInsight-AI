import React from "react";

export default function NotFound() {
  return (
    <div className="flex items-center justify-center min-h-[60vh]">
      <div className="text-center">
        <h2 className="text-2xl font-semibold">Page not found</h2>
        <p className="text-slate-500 mt-2">The page you are looking for does not exist.</p>
      </div>
    </div>
  );
}