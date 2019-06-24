from django.urls import path
from.views import add_student, list_students

urlpatterns = [
	path("add/",add_student,name="add_student"),
	path("list/",list_students,name="list_students"),
]