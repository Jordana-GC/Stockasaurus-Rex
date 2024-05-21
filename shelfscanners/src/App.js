import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Fridges from './pages/Fridges';
import SpecificFridge from './pages/SpecificFridge';
import Notifications from './pages/Notifications';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Fridges />} />
        <Route path="/fridge/:fridgeNumber" element={<SpecificFridge />} />
        <Route path="/notifications" element={<Notifications />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
