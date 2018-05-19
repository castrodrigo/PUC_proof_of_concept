import axios from 'axios';

import {ENDPOINT, ROUTE_COURSES, ROUTE_SUBJECTS} from '../constants'

export const FETCH_COURSE = 'FETCH_COURSE';
export const FETCH_COURSES = 'FETCH_COURSES';
export const FETCH_SUBJECT = 'FETCH_SUBJECT';
export const FETCH_SUBJECTS = 'FETCH_SUBJECTS';
export const FETCH_USERS = 'FETCH_USERS';


export function fetchCourses() {
    const url = `${ROUTE_COURSES}`;
    const request = axios.get(url);

    return {
        type: FETCH_COURSES,
        payload: request
    }
}

export function fetchCourse(id) {
    const url = `${ROUTE_COURSES}${id}`;
    const request = axios.get(url);

    return {
        type: FETCH_COURSE,
        payload: request
    }
}

export function fetchSubjects() {
    const url = `${ROUTE_SUBJECTS}`;
    const request = axios.get(url);

    return {
        type: FETCH_SUBJECTS,
        payload: request
    }
}

export function fetchSubject(id) {
    const url = `${ROUTE_SUBJECTS}${id}`;
    const request = axios.get(url);

    return {
        type: FETCH_SUBJECT,
        payload: request
    }
}
