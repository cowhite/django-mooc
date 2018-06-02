from django.conf.urls import url

from django.views import generic as generic_views

urlpatterns = [
	url(r'^$', generic_views.TemplateView.as_view(
		template_name="django_mooc/course_admin_full.html"), 
	name="course-admin-full")
]
