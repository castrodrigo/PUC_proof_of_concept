import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { fetchSubject } from '../actions/index';

class SubjectSelected extends Component {
    componentDidMount() {
        this.props.fetchSubject(this.props.id);
    }

    render() {
        if (typeof this.props.subject[0] !== 'undefined'){
            return (
                <div>
                    <Link to={ "/cursos/" + this.props.courseId }> &laquo; voltar para página do curso</Link>
                    <h1>{ this.props.subject[0].code + ' - ' + this.props.subject[0].name }</h1>
                    <h4> Descrição</h4>
                    <p>{ this.props.subject[0].summary }</p>
                    <h4> Procedimentos </h4>
                    <p>{ this.props.subject[0].procedures }</p>
                    <h4> Roteiro </h4>
                    <p>{ this.props.subject[0].script }</p>
                </div>
            );
        } else {
            return <h4> Curso não encontrado </h4>
        }
    }
}

function mapStateToProps({ subject }) {
    return { subject };
}

const mapDispatchToProps = (dispatch) => {
    return bindActionCreators({ fetchSubject }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(SubjectSelected);