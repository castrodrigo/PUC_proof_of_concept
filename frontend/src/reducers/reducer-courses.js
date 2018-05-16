import { FETCH_COURSES } from "../actions/index";

export default function(state=[], action){
    switch (action.type) {
        case FETCH_COURSES:
            return [ action.payload.data, ...state];
    }
    return state;
}