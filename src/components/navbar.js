import React, { Component } from 'react';
import { Link } from 'react-router-dom';

export default class Navbar extends Component {

  render() {
    return (
      <nav className="navbar navbar-dark bg-dark navbar-expand-lg rounded-bottom">
        <Link to="/" className="navbar-brand h1" style={{marginRight: "50px"}}>Soldier Health Dashboard</Link>
        <div className="collpase navbar-collapse">
        <ul className="navbar-nav mr-auto">
          <li className="navbar-item">
          <Link to="/" className="nav-link h2" style={{marginRight: "30px"}}>Home</Link>
          </li>
          <li className="navbar-item">
          <Link to="/soldier" className="nav-link h2" style={{marginRight: "30px"}}>Create Soldier</Link>
          </li>
        </ul>
        </div>
      </nav>
    );
  }
}