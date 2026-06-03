// Student detail page showing profile + attendance + recent results
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import Card from "../components/Card";
import api from "../services/api";

export default function StudentDetail() {
  const { id } = useParams();
  const [student, setStudent] = useState(null);

  useEffect(() => {
    async function load() {
      try {
        const res = await api.get(`/students/${id}`);
        const s = res.data;
        setStudent({
          id: s.id,
          name: s.full_name || s.name,
          cgpa: s.cgpa,
          attendance: s.attendance || s.attendance_percent || 0,
          modules: s.recent_modules || s.modules || []
        });
      } catch (err) {
        console.error(err);
      }
    }
    load();
  }, [id]);

  if (!student) return <div>Loading...</div>;

  return (
    <div className="space-y-4">
      <Card>
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-xl font-semibold">{student.name}</h3>
            <div className="text-sm text-slate-500">CGPA: {student.cgpa}</div>
          </div>
        </div>
      </Card>

      <div className="grid md:grid-cols-2 gap-4">
        <Card title="Attendance">
          <div>{student.attendance}%</div>
        </Card>

        <Card title="Recent Results">
          <ul className="text-sm space-y-1">
            {student.modules.map((m) => (
              <li key={m.name}>
                {m.name} — <strong>{m.grade}</strong>
              </li>
            ))}
          </ul>
        </Card>
      </div>
    </div>
  );
}