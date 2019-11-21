from django.tests import TestCase
from student.models import Student
from course.models import Course
from teacher.models import Teacher

class StudentCourseTestCase(TestCase):
	def setUp(self):
		self.student_a=Student(first_name=Joy,
			last_name=Wahome,
			date_of_birth=datetime.date(1998,8,25),
			registration_number=123,
			place_of_residence=Nairobi,
			phone_number=123456789,
			email=joy@akirachix.com,
			guardian_phone=12345,
			id_number=1111111,
			date_joined=datetime.date.today(),)

		self.student_b=Student(first_name=Ivy,
			last_name=Wahome,
			date_of_birth=datetime.date(1996,5,24),
			registration_number=1234,
			place_of_residence=Nairobi,
			phone_number=123456789,
			email=ivy@akirachix.com,
			guardian_phone=123456,
			id_number=2222222,
			date_joined=datetime.date.today(),)

		self.python=Course(name=python,
			duration_in_months=10,
			course_number=1,
			description=Learn to code in Python,)

		self.javascript=Course(name=javascript,
			duration_in_months=10,
			course_number=2,
			description=Learn to code in JS,)

		self.hardware=Course(name=hardware,
			duration_in_months=10,
			course_number=3,
			description=Learn to build hardware,)

		self.teacher=Teacher(first_name=James,
			last_name=Mwai,
			date_of_birth=datetime.date(1998,8,25),
			registration_no=123,
			place_of_residence=Nairobi,
			phone_number=123456789,
			email=james@akirachix.com,
			id_number=1111111,
			profession=Consultant,)

	def test_student_can_join_many_courses(self):
		self.assertEqual(self.student_a.courses.count(),0)
		self.student_a.courses.add(self.python)
		self.assertEqual(self.student_a.courses.count(),1)

		