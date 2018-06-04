from django.shortcuts import render

from django.views.generic import FormView
from django.http import JsonResponse

from .forms import NewCourseForm
from django_mooc.utils.views import FormViewUtil


class NewCourseView(FormViewUtil):
    form_class = NewCourseForm
    template_name = "django_mooc/courses/forms/new_course.html"

    def form_valid(self, form):
        instance = form.save(self.request.user)
        return JsonResponse({"message": "success", "id": instance.id })

