import React from 'react';
import { Link } from 'react-router-dom';
import '../pages/Style.css';

const FridgeButton = ({ fridgeNumber }) => {
    return (
        <div className="fridge-button">
            <Link to={`/fridge/${fridgeNumber}`}>Fridge {fridgeNumber}</Link>
        </div>
    );
};

export default FridgeButton;
