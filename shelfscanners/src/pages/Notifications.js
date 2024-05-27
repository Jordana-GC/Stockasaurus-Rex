import React, { useEffect, useState } from 'react';
import NavBar from '../components/NavBar';
import './Style.css';
import Footer from "../components/Footer";

const Notifications = () => {
    const [notifications, setNotifications] = useState([]);
    useEffect(() => {
        fetch(`http://localhost:5000/api/Notifications`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                console.log("Fetched data:", data);
                setNotifications(data);
            })
            .catch(error => console.error('Error fetching notifications:', error));
    }, []);
    return (
        <div className="main">
            <NavBar />
            <div className="main-content">
                <h1>Notifications</h1>
                <ul>
                    {notifications.length > 0 ? (
                        notifications.map((notification, index) => (
                            <li key={index} className="notification-item">
                                <p>The {notification[0]} is about to expire and the date is {notification[1]}</p>
                            </li>
                        ))
                    ) : (
                        <li className="notification-item">
                            <p>No notifications found.</p>
                        </li>
                    )}
                </ul>
            </div>
            <Footer />
        </div>
    );
};

export default Notifications;
