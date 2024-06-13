import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './NavBar.css';
import Logo from "../assets/StockosaurusRex.png";
import FridgeIcon from "../assets/fridge.png";
import NotificationsIcon from "../assets/notifications.png";
import BurgerIcon from "../assets/burger-menu.png";

const NavBar = () => {
    const [notificationsCount, setNotificationsCount] = useState(0);
    const [menuOpen, setMenuOpen] = useState(false);

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

    const toggleMenu = () => {
        setMenuOpen(!menuOpen);
    };

    return (
        <div className="navbar">
            <div className="burger" onClick={toggleMenu}>
                <img src={BurgerIcon} alt="Menu" className="burger-icon" />
            </div>
            <div className="logo">
                <Link to="/fridges">
                    <img src={Logo} alt="logo" />
                </Link>
            </div>
            <ul className={menuOpen ? 'open' : ''}>
                <li>
                    <Link to="/fridges">
                        <img src={FridgeIcon} alt="Fridge" className="nav-icon" />
                        <span>Fridges</span>
                    </Link>
                </li>
                <li>
                    <Link to="/notifications">
                        <img src={NotificationsIcon} alt="Notifications" className="nav-icon" />
                        <span>{notificationText}</span>
                    </Link>
                </li>
            </ul>
        </div>
    );
};

export default NavBar;
