import React from 'react';
import { Link } from 'react-router-dom';
import './NavBar.css';
import Logo from "../assets/StockosaurusRex.png";
import FridgeIcon from "../assets/fridge.png";
import NotificationsIcon from "../assets/notifications.png";

const NavBar = () => {
    return (
        <div className="navbar">
            <div className="logo">
                <img src={Logo} alt="logo" />
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
                        Notifications
                    </Link>
                </li>
            </ul>
        </div>
    );
};

export default NavBar;
