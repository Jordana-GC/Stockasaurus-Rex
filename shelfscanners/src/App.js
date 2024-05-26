import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Fridges from './pages/Fridges';
import SpecificFridge from './pages/SpecificFridge';
import Notifications from './pages/Notifications';
import Login from "./pages/Login";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/fridge/:fridgeNumber" element={<SpecificFridge />} />
        <Route path="/notifications" element={<Notifications />} />
        <Route path="/fridges" element={<Fridges />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
