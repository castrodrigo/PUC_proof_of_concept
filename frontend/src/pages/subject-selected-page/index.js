import React, { Component } from 'react';
import queryString from 'query-string'
import Header from '../../components/header/'
import Footer from '../../components/footer/'
import SubjectSelected from '../../containers/subject_selected'

import styles from './style.css'

export default class SubjectSelectedPage extends Component {
  render() {
    return (
      <div className={ styles.cover_container }>
        <Header />
        <div className={ styles.box }>
          <SubjectSelected id={ this.props.match.params.id } 
            courseId={ queryString.parse(this.props.location.search).course }/>
        </div>
        <Footer />  
      </div>
    );
  }
}
