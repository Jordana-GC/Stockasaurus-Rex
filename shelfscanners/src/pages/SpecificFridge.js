import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import NavBar from '../components/NavBar';
import './Style.css';
import Footer from "../components/Footer";

const SpecificFridge = () => {
    const { fridgeNumber } = useParams();
    console.log("fridgeNumber:", fridgeNumber);
    const [items, setItems] = useState([]);

    const navigate = useNavigate();
    const maxFridges = 4; 

    useEffect(() => {
        fetch(`https://100.95.179.98:5000/api/fridge/${fridgeNumber}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => setItems(data))
            .catch(error => console.error('Error fetching fridge data:', error));
    }, [fridgeNumber]);

    const handleNextClick = () => {
        const nextFridge = Number(fridgeNumber) + 1;
        if (nextFridge <= maxFridges) {
            navigate(`/fridge/${nextFridge}`);
        }
    };

    const handlePreviousClick = () => {
        const previousFridge = Number(fridgeNumber) - 1;
        if (previousFridge >= 1) {
            navigate(`/fridge/${previousFridge}`);
        }
    };

    return (
        <div className="main">
            <NavBar />
            <div className='main-content'>
                <h1>Fridge {fridgeNumber}</h1>
                <table>
                    <thead>
                        <tr>
                            <th>Item Name</th>
                            <th>Entry Date</th>
                            <th>Expiry Date</th>
                        </tr>
                    </thead>
                    <tbody>
                      {items.length === 0 ? (
                        <tr>
                          <td colSpan="3">No Items Currently</td>
                        </tr>
                      ) : (
                        items.map((item) => (
                          <tr key={item.itemID}>
                            <td>{item.itemName}</td>
                            <td>{item.entryDate}</td>
                            <td>{item.expiryDate}</td>
                          </tr>
                        ))
                      )}
                    </tbody>
                </table>
                <div className="button-container">
                    <button 
                        className="previous-button"
                        onClick={handlePreviousClick}
                        disabled={Number(fridgeNumber) <= 1}
                    >
                        Previous
                    </button>
                    <button 
                        className="next-button"
                        onClick={handleNextClick}
                        disabled={Number(fridgeNumber) >= maxFridges}
                    >
                        Next
                    </button>
                </div>
            </div>
            <Footer />
        </div>
    );
};

export default SpecificFridge;
