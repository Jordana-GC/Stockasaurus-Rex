import React, { useEffect, useState } from 'react';
import NavBar from '../components/NavBar';
import './Style.css';

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
                console.log("Fetched data:", data); // 打印获取的数据
                setNotifications(data);
            })
            .catch(error => console.error('Error fetching notifications:', error));
    }, []);

    return (
        <div className="fridges-page">
            <NavBar />
            <div className="notifications-content">
                <h1>Notifications</h1>
                <ul>
                    {notifications.length > 0 ? (
                        notifications.map((notification, index) => (
                            <li key={index} className="notification-item">
                                <p>{notification[0]} will expire at {notification[1]}</p>
                            </li>
                        ))
                    ) : (
                        <li>No notifications found.</li>
                    )}
                </ul>
            </div>
        </div>
    );
};


export default Notifications;
