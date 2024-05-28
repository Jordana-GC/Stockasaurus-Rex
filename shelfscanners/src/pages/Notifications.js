import React, { useState, useEffect } from 'react';
import NavBar from '../components/NavBar';
import './Style.css';
import Footer from "../components/Footer";

const Notifications = () => {
    const [notifications, setNotifications] = useState([]);

    useEffect(() => {
        fetchNotifications();
    }, []);

    const fetchNotifications = () => {
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
    };

    const deleteNotification = (itemId) => {
        // Find the index of the notification to be deleted
        const indexToDelete = notifications.findIndex(notification => notification.itemID === itemId);

        // Update the notifications state to remove the deleted notification
        setNotifications(prevNotifications => {
            const updatedNotifications = [...prevNotifications];
            updatedNotifications.splice(indexToDelete, 1);
            return updatedNotifications;
        });
    };


    return (
        <div className="main">
            <NavBar notificationsCount={notifications.length} />
            <div className="main-content">
                <h1>Notifications</h1>
                <ul>
                    {notifications.length > 0 ? (
                        notifications.map((notification, index) => (
                            <li key={index} className="notification-item">
                                <p>On {notification[3]} the {notification[1]} in fridge "{notification[2]}" will expire</p>
                                <a href={`/api/DeleteNotification/${notification.itemID}`} onClick={(e) => {
                                    e.preventDefault();
                                    if (window.confirm('Warning: deleting this notification will suspend the expiry track of the corresponding item in the fridge. Are you sure to delete?')) {
                                        deleteNotification(notification.itemID);
                                    }
                                }} className="delete-button">Hide</a>
                            </li>
                        ))
                    ) : (
                        <li className="notification-item">
                            <p>No notifications.</p>
                        </li>
                    )}
                </ul>
            </div>
            <Footer />
        </div>
    );
};

export default Notifications;


