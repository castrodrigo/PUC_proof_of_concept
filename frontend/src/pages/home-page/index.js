import React, { Component } from 'react';
import Header from '../../components/header/'
import Footer from '../../components/footer/'
import Content from './components/content/'

import styles from './style.css'

export default class HomePage extends Component {
  render() {
    return (
      <div className={ styles.cover_container }>
        <Header />
        <main role="main" className={ styles.box }>
          <h1 className="cover-heading">Universidade</h1>
          <p className="lead">Formando profissionais e humanos. Trilhe seu caminho conosco</p>
        </main>
        <Content />
        <Footer />
      </div>
    );
  }
}
