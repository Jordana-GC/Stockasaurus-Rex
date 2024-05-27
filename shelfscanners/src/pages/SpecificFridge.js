import React from 'react';
import { useParams } from 'react-router-dom';
import NavBar from '../components/NavBar';
import './Style.css';

const SpecificFridge = () => {
    const { fridgeNumber } = useParams();

    // Dummy data
    const items = [
        { name: 'Milk', entryDate: '2024-05-01', expiryDate: '2024-05-10' },
        { name: 'Eggs', entryDate: '2024-05-05', expiryDate: '2024-05-20' },
        { name: 'Banana', entryDate: '2024-05-03', expiryDate: '2024-05-15' },
    ];

    return (
        <div className="main-content">
            <NavBar />
            <div className='specific-fridge-content'>
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
                        {items.map((item, index) => (
                            <tr key={index}>
                                <td>{item.name}</td>
                                <td>{item.entryDate}</td>
                                <td>{item.expiryDate}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default SpecificFridge;
