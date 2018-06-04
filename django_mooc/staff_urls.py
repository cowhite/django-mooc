from django.conf.urls import url, include

from django.views import generic as generic_views
from django.contrib.admin.views.decorators import staff_member_required

from django_mooc.courses import views as course_views

urlpatterns = [
	url(r'^$', staff_member_required(generic_views.TemplateView.as_view(
		template_name="django_mooc/course_admin_full.html")),
        name="course-admin-full"),

    url(r'^new_course/$',
        staff_member_required(course_views.NewCourseView.as_view()),
        name="new-course"),
]
