import { FETCH_COURSE } from "../actions/index";

export default function(state=[], action){
    switch (action.type) {
        case FETCH_COURSE:
            return [ action.payload.data, ...state];
    }
    return state;
}