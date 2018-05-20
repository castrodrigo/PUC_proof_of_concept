import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { fetchSubject } from '../actions/index';

class SubjectInfo extends Component {
    constructor(props) {
        super(props)
        this.state = {subjectData: ''}
    }

    componentDidMount() {
        this.props.fetchSubject(this.props.id);
    }

    render() {
        this.state['subjectData'] = this.props.subject;
        if (typeof this.props.subject[0] !== 'undefined'){
            const subject = this.props.subject[0];
            const id = this.props.id;
            const courseId = this.props.courseId;
            const semester = this.props.semester;
            return (
                <li key={ id }>
                    <Link to={'/disciplinas/' + id + "?course=" + courseId}>
                        {subject.code}::{subject.name} - {semester}º período
                    </Link>    
                </li>
            );
        } else {
            return <li> Loading... </li>
        }
    }
}

function mapStateToProps({ subject }) {
    return { subject };
}

const mapDispatchToProps = (dispatch) => {
    return bindActionCreators({ fetchSubject }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(SubjectInfo);