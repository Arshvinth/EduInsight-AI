// Dashboard shows quick stats and recent activity
import React, { useEffect, useState } from "react";
import Card from "../components/Card";
import api from "../services/api";

export default function Dashboard() {
  const [stats, setStats] = useState({ students: 0, modules: 0 });

  useEffect(() => {
    // Example: call backend endpoints to fetch counts
    async function load() {
      try {
        const [sRes, mRes] = await Promise.all([
          api.get('/students/count'),
          api.get('/modules/count')
        ]);
        setStats({ students: sRes.data.count || 0, modules: mRes.data.count || 0 });
      } catch (err) {
        console.error(err);
      }
    }
    load();
  }, []);

  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card title="Students">
          <div className="text-3xl font-bold">{stats.students}</div>
        </Card>
        <Card title="Modules">
          <div className="text-3xl font-bold">{stats.modules}</div>
        </Card>
        <Card title="Documents">
          <div className="text-3xl font-bold">18</div>
        </Card>
      </div>

      <Card title="Recent Activity">
        <ul className="space-y-2 text-sm text-slate-600">
          <li>• New document uploaded: Operating Systems Notes</li>
          <li>• Student John Doe got 82% in Algorithms</li>
        </ul>
      </Card>
    </div>
  );
}