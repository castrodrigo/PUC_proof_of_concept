import React, { Component } from 'react';
import Header from '../../components/header/'
import CourseList from '../../containers/course_list'

import styles from './style.css'

export default class HomePage extends Component {
  render() {
    return (
      <div className="cover-container">
        <Header />
        <main role="main" className="inner cover">
          <h1 className="cover-heading">Universidade</h1>
          <p className="lead">Formando profissionais e humanos. Trilhe seu caminho conosco</p>
        </main>
      </div>
    );
  }
}
