from django.db import models

from django_mooc.utils.models import DateTimeBase, Slugged
from django_mooc.courses.models import Course
# from django_mooc.courses import models as courses_models


class AssignmentType(DateTimeBase):
    # course = models.ForeignKey(courses_models.Course)
    course = models.ForeignKey('courses.Course')
    title = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=50, unique=True)
    weight_of_total_grade = models.IntegerField()
    total_number = models.IntegerField()
    number_of_droppable = models.IntegerField()



