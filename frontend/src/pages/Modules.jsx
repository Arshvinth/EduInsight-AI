// List of modules; basic layout
import React, { useEffect, useState } from "react";
import Card from "../components/Card";
import api from "../services/api";

export default function Modules() {
  const [modules, setModules] = useState([]);

  useEffect(() => {
    async function load() {
      try {
        const res = await api.get('/modules');
        const mapped = (res.data || []).map((m) => ({
          id: m.id,
          code: m.module_code || m.code,
          title: m.module_name || m.title
        }));
        setModules(mapped);
      } catch (err) {
        console.error('Failed to load modules:', err);
      }
    }
    load();
  }, []);

  return (
    <div>
      <h2 className="text-lg font-semibold mb-4">Modules</h2>
      <div className="grid md:grid-cols-2 gap-4">
        {modules.map((m) => (
          <Card key={m.code}>
            <div className="flex items-center justify-between">
              <div>
                <div className="font-semibold">{m.title}</div>
                <div className="text-sm text-slate-500">{m.code}</div>
              </div>
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
}