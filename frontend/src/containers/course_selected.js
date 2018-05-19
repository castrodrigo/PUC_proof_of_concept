import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { fetchCourse } from '../actions/index';

class CourseSelected extends Component {

    componentDidMount() {
        this.props.fetchCourse(this.props.id);
    }

    render() {
        console.log(this.props.course[0]);
        if (typeof this.props.course[0] !== 'undefined'){
            return (
                <div>
                    <Link to="/cursos">voltar para cursos</Link>
                    <h1>{ this.props.course[0].code + ' - ' + this.props.course[0].name }</h1>
                    <h4> Tipo de formação</h4>
                    <p>{ this.props.course[0].type }</p>
                    <h4> Número de períodos</h4>
                    <p>{ this.props.course[0].semesters }</p>
                    <h4> Descrição</h4>
                    <p>{ this.props.course[0].summary }</p>
                    <h4> Disciplinas</h4>
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
    return bindActionCreators({ fetchCourse }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(CourseSelected);