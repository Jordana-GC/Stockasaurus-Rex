import React from 'react';
import { Link } from 'react-router-dom';
import './NavBar.css';
import Logo from "../assets/StockosaurusRex.png";

const NavBar = () => {
    return (
        <div className="navbar">
            <div className="logo">
                <img src={Logo} alt="logo" />
            </div>
            <ul>
                <li><Link to="/fridges">Fridges</Link></li>
                <li><Link to="/Notifications">Notifications</Link></li>
            </ul>
        </div>
    );
};

export default NavBar;
