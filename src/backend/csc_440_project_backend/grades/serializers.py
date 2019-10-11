from rest_framework import serializers
from grades.models import Course, CourseInstance, GradeEntry, Category, College, CategoryScoreRequirement, Semester


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseInstance
        fields = '__all__'


class CourseInstanceSearchCourseSerializer(CourseSerializer):
    """
    Serialize courses for use when searching course instances.
    """

    class Meta:
        model = Course
        fields = ('id', 'code', 'name')


class CourseInstanceSearchSerializer(CourseInstanceSerializer):
    """
    Serialize common information needed when searching for a course instance.
    """

    course = CourseInstanceSearchCourseSerializer()

    class Meta:
        model = CourseInstance
        fields = ('id', 'section', 'course')


class GradeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeEntry
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'


class CategoryScoreRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryScoreRequirement
        fields = (
            'id',
            'last_updated',
            'notes',
            'min_a',
            'min_b',
            'min_c',
            'min_d',
            'course_instance',
            'categories'
        )


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ('colleges', 'id', 'last_updated', 'notes', 'season', 'year', 'students')
