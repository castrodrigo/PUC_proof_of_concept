import React, { Component } from 'react';
import Header from '../components/header/'
import Footer from '../components/footer/'
import CourseList from '../containers/course_list'

export default class CoursePage extends Component {
  render() {
    return (
      <div>
        <Header />
        <CourseList />
        <Footer />  
      </div>
    );
  }
}
