import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { fetchCourses } from '../actions/index';

class CourseList extends Component {
    renderCourse(course) {
        const id = course.id;
        const code = course.code;
        const name = course.name;
        const semesters = course.semesters;
        
        return (
            <li key={id}>
                <Link to={ 'cursos/' + id }> {code} - {name}: {semesters} períodos</Link>
            </li>
        );
    }

    componentDidMount() {
        this.props.fetchCourses();
    }

    render() {
        if (typeof this.props.courses[0] !== 'undefined'){
            const courseList = this.props.courses[0].data
            return (
                <div>
                    <ul>
                        {courseList.map(this.renderCourse)}
                    </ul>
                </div>
            );
        } else {
            return <div> Loading... </div>
        }
        
    }
}

function mapStateToProps({ courses }) {
    return { courses };
}

const mapDispatchToProps = (dispatch) => {
    return bindActionCreators({ fetchCourses }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(CourseList);