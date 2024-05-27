import React from 'react';
import NavBar from '../components/NavBar';
import './Style.css';

const Notifications = () => {
    const notifications = [
        "The item banana will expire tomorrow",
        "The item banana will expire tomorrow",
        "The item banana will expire tomorrow",
        "The item banana will expire tomorrow"
    ];

    return (
        <div className="main-content">
            <NavBar />
            <div className="notifications-content">
                <h1>Notifications</h1>
                <ul>
                    {notifications.map((notification, index) => (
                        <li key={index} className="notification-item">
                            <input type="checkbox"/>
                            <span>{notification}</span>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default Notifications;
