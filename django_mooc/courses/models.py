from django.db import models

from django_mooc.utils.models import DateTimeBase, Slugged


class Course(DateTimeBase, Slugged):
    pass


class Section(DateTimeBase, Slugged):
    course = models.ForeignKey(Course)
    order = models.IntegerField()


class SubSection(DateTimeBase, Slugged):
    course_section = models.ForeignKey(Section)
    order = models.IntegerField()


class Unit(DateTimeBase):
    sub_section = models.ForeignKey(SubSection)
    order = models.IntegerField()


