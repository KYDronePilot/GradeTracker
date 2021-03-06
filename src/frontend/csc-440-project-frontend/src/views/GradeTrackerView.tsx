import React, {Component} from 'react';
import {connect} from 'react-redux';
import {MDBContainer, MDBListGroup} from 'mdbreact';
import {allInstances, indexInstances} from '../utils/objectification_utils';
import SemesterListItem from '../components/SemesterListItem';
import AddSemesterForm from '../containers/AddSemesterForm';
import {GradeTrackerBreadcrumb} from '../components/layout/breadcrumbs';
import {Category, CourseInstance, GradeEntry, Semester} from '../api/types';
import {generateRawGradeTrackerInfoStructure, getOverallStats, SemesterStats} from '../api/courseInstance';
import {removeStudentSemesterRelationship} from '../actions/semesterActions';
import {GradeTrackerButton} from '../components/Common';

interface mapStateToPropsTypes {
    semesters: {
        semester: Semester;
        stats: SemesterStats;
    }[];
}

interface GradeTrackerViewProps extends mapStateToPropsTypes {
    removeSemester: (semesterId: number) => void;
}

interface GradeTrackerViewState {
    addFormVisible: boolean;
}

function mapStateToProps(state: any): mapStateToPropsTypes {
    // IDs of the semesters that the user is enrolled in
    const userSemesterIDs: number[] = state.auth.user.semesters;
    // Get semesters that the user is enrolled in
    const semesters = indexInstances(state.semester.semesters, userSemesterIDs);
    // TODO: Shrinking scope of categories and grade entries could give a speed improvement
    const courseInstances: CourseInstance[] = allInstances(state.courseInstance.courseInstances);
    const categories: Category[] = allInstances(state.category.categories);
    const gradeEntries: GradeEntry[] = allInstances(state.gradeEntry.gradeEntries);
    const gradeTrackerStats = getOverallStats(generateRawGradeTrackerInfoStructure(
        semesters,
        courseInstances,
        categories,
        gradeEntries
    ));

    return {
        semesters: semesters.map((_, i) => ({
            semester: semesters[i],
            stats: gradeTrackerStats.semesterStats[i]
        }))
    };
}

class GradeTrackerView extends Component<GradeTrackerViewProps, GradeTrackerViewState> {
    constructor(props: GradeTrackerViewProps) {
        super(props);
        this.state = {
            addFormVisible: false
        };
    }

    render() {
        const props = this.props;

        return (
            <div>
                <AddSemesterForm
                    visible={this.state.addFormVisible}
                    toggleVisible={() => this.setState(state => ({addFormVisible: !state.addFormVisible}))}
                />
                <GradeTrackerBreadcrumb/>
                <MDBContainer>
                    <h1 className={'font-weight-bold'}>Enrolled Semesters</h1>
                    <MDBListGroup>
                        {props.semesters.map(({semester, stats}) => (
                            <SemesterListItem
                                key={semester.id}
                                lastUpdated={semester.last_updated}
                                id={semester.id}
                                season={semester.season}
                                year={semester.year}
                                removeSemester={props.removeSemester}
                                gpa={stats.gpa}
                            />
                        ))}
                    </MDBListGroup>
                    <div className={'text-right mt-2'}>
                        <GradeTrackerButton
                            onClick={() => this.setState({addFormVisible: true})}
                            className={'mr-0'}
                        >
                            Add Semester
                        </GradeTrackerButton>
                    </div>
                </MDBContainer>
            </div>
        );
    }
}

export default connect(
    mapStateToProps,
    {removeSemester: removeStudentSemesterRelationship}
)(GradeTrackerView);
