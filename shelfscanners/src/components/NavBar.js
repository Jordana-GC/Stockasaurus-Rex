import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './NavBar.css';
import Logo from "../assets/StockosaurusRex.png";
import FridgeIcon from "../assets/fridge.png";
import NotificationsIcon from "../assets/notifications.png";

const NavBar = () => {
    const [notificationsCount, setNotificationsCount] = useState(0);

    useEffect(() => {
        // update the number of notifications when the component is loading
        fetchNotificationsCount();
    }, []);

    const fetchNotificationsCount = () => {
        fetch(`http://localhost:5000/api/Notifications`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                console.log("Fetched notifications count:", data.length);
                setNotificationsCount(data.length);
            })
            .catch(error => console.error('Error fetching notifications count:', error));
    };

    const notificationText = notificationsCount > 0 ? `Notifications (${notificationsCount})` : 'Notifications';

    return (
        <div className="navbar">
            <div className="logo">
                <Link to="/fridges">
                    <img src={Logo} alt="logo" />
                </Link>
            </div>
            <ul>
                <li>
                    <Link to="/fridges">
                        <img src={FridgeIcon} alt="Fridge" className="nav-icon" />
                        Fridges
                    </Link>
                </li>
                <li>
                    <Link to="/notifications">
                        <img src={NotificationsIcon} alt="Notifications" className="nav-icon" />
                        {notificationText}
                    </Link>
                </li>
            </ul>
        </div>
    );
};

export default NavBar;