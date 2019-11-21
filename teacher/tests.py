from django.test import TestCase
from.models import Teacher
import datetime
from.forms import TeacherForm
from django.urls import reverse
from django.test import Client
client=Client()

# Create your tests here.
class CreateTeacherTestCase(TestCase):
	def setUp(self):
		self.data={"first_name":"James",
			"last_name":"Mwai",
			"date_of_birth":datetime.date(1998,8,25),
			"registration_no":"123",
			"place_of_residence":"Nairobi",
			"phone_number":"123456789",
			"email":"james@akirachix.com",
			"id_number":1111111,
			"profession":"Consultant",}

		self.bad_data={"first_name":"Joy",
			"last_name":"Wahome",
			"date_of_birth":datetime.date(1998,8,25),
			"registration_no":"123",
			"place_of_residence":"Nairobi",
			"phone_number":"123456789",
			"email":"",
			"id_number":1111111,
			"profession":"Consultant",}

	def test_teacher_form_accepts_valid_data(self):
		form = TeacherForm(self.data)
		self.assertTrue(form.is_valid())

	def test_teacher_form_rejects_invalid_data(self):
		form = TeacherForm(self.bad_data)
		self.assertFalse(form.is_valid())

	def test_add_teacher_view(self):
		url=reverse("add_teacher")
		request=client.post(url, self.data)
		self.assertEqual(request.status_code,200)

	def test_accept_add_teacher_view(self):
		url=reverse("add_teacher")
		request=client.post(url, self.bad_data)
		self.assertEqual(request.status_code,400)
