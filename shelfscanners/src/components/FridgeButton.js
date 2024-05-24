import React from 'react';
import { Link } from 'react-router-dom';
import '../pages/Style.css';

const FridgeButton = ({ fridgeNumber }) => {
    return (
        <Link to={`/fridge/${fridgeNumber}`} className="fridge-button">
            <div>
                Fridge {fridgeNumber}
            </div>
        </Link>
    );
};

export default FridgeButton;
