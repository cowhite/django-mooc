from django.shortcuts import render

from django.http import JsonResponse
from django.views.generic import FormView


class FormViewUtil(FormView):
    def form_invalid(self, form):
        res = super(FormViewUtil, self).form_invalid(form)
        res.render()
        return JsonResponse({ "error": True, "html": res.rendered_content })

