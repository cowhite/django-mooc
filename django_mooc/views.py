from django.shortcuts import render

def sample(request):
    return render(request, "django_mooc/sample.html", {})