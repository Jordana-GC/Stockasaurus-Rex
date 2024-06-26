import React, { useState } from 'react';
import NavBar from '../components/NavBar';
import FridgeButton from '../components/FridgeButton';
import SpecificFridge from '../pages/SpecificFridge';
import './Style.css';
import Footer from "../components/Footer";

const Fridges = () => {
    const [selectedFridge, setSelectedFridge] = useState(null);
    const handleFridgeClick = (fridgeNumber) => {
        setSelectedFridge(fridgeNumber);
    };

    return (
        <div className="main">
            <NavBar />
            <div className="main-content">
                <h1>Total overview of all fridges</h1>
                <div className="fridges-container">
                    <FridgeButton fridgeNumber={1} onClick={() => handleFridgeClick(1)} />
                    <FridgeButton fridgeNumber={2} onClick={() => handleFridgeClick(2)} />
                    <FridgeButton fridgeNumber={3} onClick={() => handleFridgeClick(3)} />
                    <FridgeButton fridgeNumber={4} onClick={() => handleFridgeClick(4)} />
                </div>
                {selectedFridge && <SpecificFridge fridgeNumber={selectedFridge} />}
            </div>
            <Footer/>
        </div>
    );
};

export default Fridges;
