from django.test import TestCase
from.models import Student
import datetime
from.forms import StudentForm
from django.urls import reverse
from django.test import Client
client=Client()

# Create your tests here.
class StudentTestCase(TestCase):
	def setUp(self):
		self.student = Student(
			first_name="Joy",
			last_name="Wahome",
			date_of_birth=datetime.date(1998,8,25),
			registration_number="123",
			place_of_residence="Nairobi",
			phone_number="123456789",
			email="joy@akirachix.com",
			guardian_phone="12345",
			id_number=1111111,
			date_joined=datetime.date.today(),)

	def test_full_name_contains_first_name(self):
		self.assertIn(self.student.first_name,self.student.full_name())

	def test_full_name_contains_last_name(self):
		self.assertIn(self.student.last_name,self.student.full_name())

	def test_is_always_above_18(self):
		self.assertFalse(self.student.clean() < 18)

	def test_is_always_below_30(self):
		self.assertFalse(self.student.clean() > 30)

class CreateStudentTestCase(TestCase):
	def setUp(self):
		self.data={"first_name":"Joy",
			"last_name":"Wahome",
			"date_of_birth":datetime.date(1998,8,25),
			"registration_number":"123",
			"place_of_residence":"Nairobi",
			"phone_number":"123456789",
			"email":"joy@akirachix.com",
			"guardian_phone":"12345",
			"id_number":1111111,
			"date_joined":datetime.date.today(),}

		self.bad_data={"first_name":"Joy",
			"last_name":"Wahome",
			"date_of_birth":datetime.date(1998,8,25),
			"registration_number":"123",
			"place_of_residence":"Nairobi",
			"phone_number":"123456789",
			"email":"",
			"guardian_phone":"12345",
			"id_number":1111111,
			"date_joined":datetime.date.today(),}

	def test_student_form_accepts_valid_data(self):
		form = StudentForm(self.data)
		self.assertTrue(form.is_valid())

	def test_student_form_rejects_invalid_data(self):
		form = StudentForm(self.bad_data)
		self.assertFalse(form.is_valid())

	def test_add_student_view(self):
		url=reverse("add_student")
		request=client.post(url, self.data)
		self.assertEqual(request.status_code,200)

	def test_accept_add_student_view(self):
		url=reverse("add_student")
		request=client.post(url, self.bad_data)
		self.assertEqual(request.status_code,400)
























