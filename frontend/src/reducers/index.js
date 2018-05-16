import { combineReducers } from 'redux';
import CourseReducer from './reducer-course';
import CoursesReducer from './reducer-courses';
import SubjectReducer from './reducer-subject';
import SubjectsReducer from './reducer-subjects';

const rootReducer = combineReducers({
  course: CourseReducer,
  courses: CoursesReducer,
  subject: SubjectReducer,
  subjects: SubjectsReducer  
});

export default rootReducer;
