import React, { Component } from 'react';
import { Link } from 'react-router-dom';

export default class Navbar extends Component {

  render() {
    return (
      <nav className="navbar navbar-dark bg-dark navbar-expand-lg rounded-bottom">
        <Link to="/" className="navbar-brand">Soldier Health Dashboard</Link>
        <div className="collpase navbar-collapse">
        <ul className="navbar-nav mr-auto">
          <li className="navbar-item">
          <Link to="/" className="nav-link">Home</Link>
          </li>
          <li className="navbar-item">
          <Link to="/soldier" className="nav-link">Create Soldier</Link>
          </li>
        </ul>
        </div>
      </nav>
    );
  }
}