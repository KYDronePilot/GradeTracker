import {FETCH_GRADE_ENTRIES, ADD_GRADE_ENTRY} from '../actions/types';

const initialState = {
    activeGradeEntries: [],
    activeGradeEntry: {}
};

export default function (state = initialState, action) {
    switch (action.type) {
        case FETCH_GRADE_ENTRIES:
            return {
                ...state,
                activeGradeEntries: action.payload
            };
        default:
            return state;
    }
}