import { FETCH_SUBJECT } from "../actions/index";

export default function(state=[], action){
    switch (action.type) {
        case FETCH_SUBJECT:
            return [ action.payload.data, ...state];
    }
    return state;
}