import React, {Component} from 'react';
import {MDBBtn, MDBListGroup} from 'mdbreact';
import GradeEntryListItem from '../components/GradeEntryListItem';
import {GradeEntry} from '../api/types';
import {GradeEntryStats} from '../api/courseInstance';


interface GradeEntryListProps {
    gradeEntries: GradeEntry[];
    openCreateGradeEntryForm: () => void;
    editGradeEntry: (gradeEntryId: number) => void;
    gradeEntryStats: GradeEntryStats[];
}

/**
 * List view for grade entries.
 */
class GradeEntryList extends Component<GradeEntryListProps, {}> {
    render() {
        return (
            <div>
                <MDBListGroup>
                    {this.props.gradeEntries.map((gradeEntry, i) => (
                        <GradeEntryListItem
                            key={gradeEntry.id}
                            name={gradeEntry.name}
                            id={gradeEntry.id}
                            lastUpdated={gradeEntry.last_updated}
                            stats={this.props.gradeEntryStats[i]}
                            editGradeEntry={this.props.editGradeEntry}
                        />
                    ))}
                </MDBListGroup>
                <div className={'text-right mt-2'}>
                    <MDBBtn
                        color={'secondary'}
                        onClick={() => this.props.openCreateGradeEntryForm()}
                        className={'mr-0 btn heavy-rain-gradient'}
                        style={{fontSize: '16px', color: 'black'}}
                    >
                        Add Grade Entry
                    </MDBBtn>
                </div>
            </div>
        );
    }
}

export default GradeEntryList;