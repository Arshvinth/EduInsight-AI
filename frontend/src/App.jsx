// App routes: public login + protected routes (simple auth guard)
import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Students from "./pages/Students";
import StudentDetail from "./pages/StudentDetail";
import Modules from "./pages/Modules";
import Documents from "./pages/Documents";
import AIChat from "./pages/AIChat";
import RiskPrediction from "./pages/RiskPrediction";
import NotFound from "./pages/NotFound";
import Layout from "./components/Layout";
import { isLoggedIn } from "./services/auth";

function PrivateRoute({ children }) {
  return isLoggedIn() ? children : <Navigate to="/login" replace />;
}

export default function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />

      <Route
        path="/"
        element={
          <PrivateRoute>
            <Layout />
          </PrivateRoute>
        }
      >
        <Route index element={<Dashboard />} />
        <Route path="students" element={<Students />} />
        <Route path="students/:id" element={<StudentDetail />} />
        <Route path="modules" element={<Modules />} />
        <Route path="documents" element={<Documents />} />
        <Route path="ai-chat" element={<AIChat />} />
        <Route path="ml/risk" element={<RiskPrediction />} />
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  );
}