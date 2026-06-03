// Students list + quick search; links to student detail
import React, { useEffect, useState } from "react";
import Card from "../components/Card";
import { Link } from "react-router-dom";
import api from "../services/api";

export default function Students() {
  const [students, setStudents] = useState([]);

  useEffect(() => {
    async function load() {
      try {
        const res = await api.get('/students');
        // Map backend StudentRead to UI shape
        const mapped = (res.data || []).map((s) => ({
          id: s.id,
          name: s.full_name || s.name || `${s.first_name || ''} ${s.last_name || ''}`,
          cgpa: s.cgpa
        }));
        setStudents(mapped);
      } catch (err) {
        console.error(err);
      }
    }
    load();
  }, []);

  return (
    <div>
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-lg font-semibold">Students</h2>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {students.map((s) => (
          <Card key={s.id}>
            <div className="flex items-center justify-between">
              <div>
                <div className="font-semibold">{s.name}</div>
                <div className="text-sm text-slate-500">CGPA: {s.cgpa}</div>
              </div>
              <div>
                <Link
                  to={`/students/${s.id}`}
                  className="text-sm text-primary-600 hover:underline"
                >
                  View
                </Link>
              </div>
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
}