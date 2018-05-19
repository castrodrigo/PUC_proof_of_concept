import React, { Component } from 'react';
import Header from '../../components/header/'
import Footer from '../../components/footer/'
import CourseList from '../../containers/course_list'

import styles from './style.css'

export default class CoursePage extends Component {
  render() {
    return (
      <div className={ styles.cover_container }>
        <Header />
        <div className={ styles.box }>
          <h2>Cursos</h2>
          <p>Nam quis felis et turpis consectetur feugiat. Mauris auctor est eget magna maximus laoreet. Maecenas metus dolor, dapibus quis ante eu, consectetur scelerisque dolor. Vivamus congue mattis condimentum. Cras tincidunt a urna sed rhoncus. Aenean euismod diam id leo egestas, commodo rhoncus ex tincidunt. Ut sagittis nulla non diam efficitur fringilla. Quisque posuere non massa quis eleifend. Ut molestie porttitor egestas.</p>
          <div className={ styles.box_inner }>
            <CourseList />
          </div>  
        </div>
        <Footer />  
      </div>
    );
  }
}
