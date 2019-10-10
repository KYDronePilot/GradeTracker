import React, {Component} from 'react';
import {connect} from 'react-redux';
import PropTypes from 'prop-types';
import {MDBContainer} from 'mdbreact';
import GradeEntries from '../grade_entries/GradeEntries';
import {allInstances} from '../../actions/utils';
import {editCategory} from '../../actions/categoryActions';

function mapStateToProps(state) {
    return {
        gradeEntries: state.gradeEntry.gradeEntries
    };
}

class CategoryView extends Component {
    static propTypes = {
        category: PropTypes.object.isRequired,
        gradeEntries: PropTypes.object.isRequired,
        editCategory: PropTypes.func.isRequired
    };

    constructor(props) {
        super(props);
        this.state = {};
        this.editCategory = this.editCategory.bind(this);

        this.gradeEntries = this.gradeEntries.bind(this);
    }

    /**
     * Get associated grade entries.
     */
    gradeEntries() {
        const gradeEntries = allInstances(this.props.gradeEntries);
        return gradeEntries.filter(gradeEntry => gradeEntry.category === this.props.category.id);
    }

    editCategory(e) {
        e.preventDefault();
        this.props.editCategory(this.props.category, this.props.category.course_instance);
    }

    render() {
        return (
            <MDBContainer>
                <h1>{this.props.category.name}</h1>
                <small className={'text-muted'}>
                    <a onClick={this.editCategory}>Edit</a>
                </small>
                <GradeEntries gradeEntries={this.gradeEntries()} category={this.props.category}/>
            </MDBContainer>
        );
    }
}

export default connect(
    mapStateToProps,
    {editCategory}
)(CategoryView);