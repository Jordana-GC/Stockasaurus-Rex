import React, { useState } from 'react';
import './Style.css';
import LoginButton from '../components/LoginButton';

function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        // Example logic
        if (email === 'stockasaurus@rex.com' && password === 'Rex') {
            console.log('Email:', email);
            console.log('Password:', password);
            window.location.href = '/fridges';
        } else {
            setError('Invalid email or password');
        }
    };

    return (
        <div className="login-page">
            <div className="login-container">
                <h2>Log-in</h2>
                <form onSubmit={handleSubmit}>
                    <div className="input-group">
                        <label htmlFor="email">E-mail:</label>
                        <input
                            type="email"
                            id="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </div>
                    <div className="input-group">
                        <label htmlFor="password">Password:</label>
                        <input
                            type="password"
                            id="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                    </div>
                    {error && <p className="error">{error}</p>}
                    <div className="login-button">
                        <LoginButton disabled={!email || !password} />
                    </div>
                </form>
            </div>
        </div>
    );
}

export default Login;
