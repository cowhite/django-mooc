from django.db import models

from django_mooc.utils.models import DateTimeBase, Slugged

from django_mooc.courses import models as courses_models


class CourseComponent(DateTimeBase):
    COMPONENT_TYPE_CHOICE_HTML = 1
    COMPONENT_TYPE_CHOICE_PROBLEM = 2
    COMPONENT_TYPE_CHOICE_VIDEO = 3
    COMPONENT_TYPE_CHOICE_DISCUSSION = 4

    COMPONENT_TYPE_CHOICES = (
        (COMPONENT_TYPE_CHOICE_HTML, "HTML"),
        (COMPONENT_TYPE_CHOICE_PROBLEM, "Problem"),
        (COMPONENT_TYPE_CHOICE_VIDEO, "Video"),
        (COMPONENT_TYPE_CHOICE_DISCUSSION, "Discussion"),
    )

    COMPONENT_TYPE_SUB_CHOICE_RAW_HTML = 1
    COMPONENT_TYPE_SUB_CHOICE_CHECKB0XES = 31
    COMPONENT_TYPE_SUB_CHOICE_MULTIPLE_CHOICE = 32

    COMPONENT_TYPE_HTML_SUB_CHOICES = (
        (COMPONENT_TYPE_SUB_CHOICE_RAW_HTML, "HTML > Raw HTML"),
    )
    COMPONENT_TYPE_PROBLEM_SUB_CHOICES = (
        (COMPONENT_TYPE_SUB_CHOICE_CHECKB0XES, "Problem > Checkboxes(multi select)"),
        (COMPONENT_TYPE_SUB_CHOICE_MULTIPLE_CHOICE, "Problem > Multiple choice(Select only one)"),
    )


    COMPONENT_TYPE_SUB_CHOICES = COMPONENT_TYPE_HTML_SUB_CHOICES + COMPONENT_TYPE_PROBLEM_SUB_CHOICES

    order = models.IntegerField()
    unit = models.ForeignKey(courses_models.Unit)
    component_type = models.IntegerField(choices=COMPONENT_TYPE_CHOICES)
    component_sub_type = models.IntegerField(choices=COMPONENT_TYPE_SUB_CHOICES)



