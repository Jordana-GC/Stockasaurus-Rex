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
        fetch(`http://100.74.58.66:5000/api/Notifications`)
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

    const hideNotification = (itemID) => {
        if (!itemID) {
            console.error('Invalid itemID:', itemID);
            return;
        }
        // Find the index of the notification to be deleted
        const indexToDelete = notifications.findIndex(notification => notification.itemID === itemID);

        // Update the notifications state to remove the deleted notification
        setNotifications(prevNotifications => {
            const updatedNotifications = [...prevNotifications];
            updatedNotifications.splice(indexToDelete, 1);
            return updatedNotifications;
        });

        // Send a request to the back-end to mark the notification as hidden
        fetch(`http://localhost:5000/api/HideNotification/${itemID}`, {
            method: 'POST',
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                console.log(`Notification of itemID ${itemID} hidden successfully`);
                window.location.reload(true);
            })
            .catch(error => {
                // If there's an error, log it
                console.error('Error hiding notification:', error);
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
                                <p>On {notification[3]} the {notification[1]} in fridge "{notification[2]}" will expire
                                <a href={`/api/HideNotification/${notification[0]}`} onClick={(e) => {
                                    e.preventDefault();
                                    if (window.confirm('Warning: hiding this notification will stop the expiry track of the corresponding item in the fridge. Are you sure to hide?')) {
                                        hideNotification(notification[0]);
                                    }
                                }} className="delete-button">Hide</a></p>
                            </li>
                        ))
                    ) : (
                        <li className="notification-item">
                            <p>No new notifications.</p>
                        </li>
                    )}
                </ul>
            </div>
            <Footer />
        </div>
    );
};

export default Notifications;
