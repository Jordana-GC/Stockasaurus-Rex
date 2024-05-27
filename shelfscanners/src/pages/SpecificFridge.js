import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import NavBar from '../components/NavBar';
import './Style.css';

const SpecificFridge = () => {
    const { fridgeNumber } = useParams();
    console.log("fridgeNumber:", fridgeNumber);
    const [items, setItems] = useState([]);

    useEffect(() => {
        fetch(`http://localhost:5000/api/fridge/${fridgeNumber}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => setItems(data))
            .catch(error => console.error('Error fetching fridge data:', error));
    }, [fridgeNumber]);

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
            </div>
        </div>
    );
};

export default SpecificFridge;
