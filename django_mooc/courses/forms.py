from django import forms

from .models import *


class NewCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'organization')

    def save(self, created_by):
        instance = super(NewCourseForm, self).save(commit=False)
        instance.created_by = created_by
        instance.save()
        return instance
