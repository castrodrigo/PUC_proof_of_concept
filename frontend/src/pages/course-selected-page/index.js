import React, { Component } from 'react';
import Header from '../../components/header/'
import Footer from '../../components/footer/'
import CourseSelected from '../../containers/course_selected'

import styles from './style.css'

export default class CourseSelectedPage extends Component {
  render() {
    return (
      <div className={ styles.cover_container }>
        <Header />
        <div className={ styles.box }>
          <CourseSelected id={ this.props.match.params.id } />
        </div>
        <Footer />  
      </div>
    );
  }
}
