import React from 'react';
import NavBar from '../components/NavBar';
import FridgeButton from '../components/FridgeButton';
import './Style.css';

const Fridges = () => {
    return (
        <div className="main-content">
            <NavBar />
            <div className="fridges-content">
                <h1>Total overview of all fridges</h1>
                <div className="fridges-container">
                    <FridgeButton fridgeNumber={1} />
                    <FridgeButton fridgeNumber={2} />
                    <FridgeButton fridgeNumber={3} />
                    <FridgeButton fridgeNumber={4} />
                </div>
            </div>
        </div>
    );
};

export default Fridges;
