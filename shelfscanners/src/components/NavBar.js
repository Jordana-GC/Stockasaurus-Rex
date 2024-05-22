import React from 'react';
import { Link } from 'react-router-dom';
import './NavBar.css';

const NavBar = () => {
    return (
        <div className="navbar">
            <div className="logo">Stockosaurus Rex</div>
            <ul>
                <li><Link to="/">Fridges</Link></li>
                <li><Link to="/Notifications">Notifications</Link></li>
            </ul>
        </div>
    );
};

export default NavBar;
