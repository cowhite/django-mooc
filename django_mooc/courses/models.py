from django.db import models

from django_mooc.utils.models import DateTimeBase, Slugged

# from django_mooc.assignments import models as assignment_models

class Course(DateTimeBase, Slugged):
    organization = models.CharField(max_length= 255)

class Section(DateTimeBase, Slugged):
    course = models.ForeignKey(Course)
    order = models.IntegerField()
    release_date = models.DateTimeField(auto_now= True)
    hide_from_learners = models.BooleanField(default= False)


class SubSection(DateTimeBase, Slugged):
    course_section = models.ForeignKey(Section)
    order = models.IntegerField()
    release_date = models.DateTimeField(auto_now= True)
    # grade_as = models.ForeignKey(assignment_models.AssignmentType)
    grade_as = models.ForeignKey('assignments.AssignmentType')
    due_date = models.DateTimeField(null= True, blank= True)


class Unit(DateTimeBase):
    sub_section = models.ForeignKey(SubSection)
    order = models.IntegerField()
    hide_from_learners = models.BooleanField(default= False)


