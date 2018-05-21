import React, { Component } from 'react';
import { Link } from 'react-router-dom';

import styles from './style.css';

export default class Header extends Component {
  render() {
    return (
      <div>
        <header>
          <nav className="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
            <Link to='/'  className="navbar-brand">Universidade</Link>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarCollapse">
              <ul className="navbar-nav mr-auto">
                <li className="nav-item">
                    <Link to='/' className="nav-link">Home</Link>
                </li>
                <li className="nav-item">
                    <Link to='/cursos' className="nav-link">Cursos</Link>
                </li>
                <li className="nav-item">
                    <a className="nav-link disabled" href="#">Sobre</a>
                </li>
                <li className="nav-item">
                    <a className="nav-link disabled" href="#">Fale Conosco</a>
                </li>
              </ul>
            </div>
          </nav>
        </header>
      </div>
    );
  }
}
