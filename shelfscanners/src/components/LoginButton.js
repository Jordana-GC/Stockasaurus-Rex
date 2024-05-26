import React from 'react';
import '../pages/Style.css';

const LoginButton = ({ disabled }) => {
    return (
        <button type="submit" disabled={disabled}>
            Submit
        </button>
    );
};

export default LoginButton;
