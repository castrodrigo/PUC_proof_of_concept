import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { fetchCourse, fetchSubject, FETCH_SUBJECT } from '../actions/index';

import SubjectInfo from './subject_info_listing';

class CourseSelected extends Component {
    componentDidMount() {
        this.props.fetchCourse(this.props.id);
    }

    render() {
        if (typeof this.props.course[0] !== 'undefined'){
            return (
                <div>
                    <Link to="/cursos"> &laquo; voltar para cursos</Link>
                    <h1>{ this.props.course[0].code + ' - ' + this.props.course[0].name }</h1>
                    <h4> Tipo de formação</h4>
                    <p>{ this.props.course[0].type }</p>
                    <h4> Número de períodos</h4>
                    <p>{ this.props.course[0].semesters }</p>
                    <h4> Descrição</h4>
                    <p>{ this.props.course[0].summary }</p>
                    <h4> Disciplinas</h4>
                    <ul>
                        {this.props.course[0].subjects.map((subject) => {
                            return <SubjectInfo id={ subject.id } 
                                semester={ subject.semester } 
                                courseId={ this.props.id }/>
                                return new Promise(resolve => setTimeout(resolve, 10000));
                        })}
                    </ul>
                </div>
            );
        } else {
            return <h4> Curso não encontrado </h4>
        }
    }
}

function mapStateToProps({ course }) {
    return { course };
}

const mapDispatchToProps = (dispatch) => {
    return bindActionCreators({ fetchCourse, fetchSubject }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(CourseSelected);