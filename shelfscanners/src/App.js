import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Fridges from './pages/Fridges';
import SpecificFridge from './pages/SpecificFridge';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Fridges />} />
        <Route path="/fridge/:fridgeNumber" element={<SpecificFridge />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
