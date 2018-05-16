import { FETCH_SUBJECTS } from "../actions/index";

export default function(state=[], action){
    switch (action.type) {
        case FETCH_SUBJECTS:
            return [ action.payload.data, ...state];
    }
    return state;
}