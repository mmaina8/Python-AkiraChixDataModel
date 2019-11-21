from django.test import TestCase
from student.models import Student
from course.models import Course
from teacher.models import Teacher
import datetime

class StudentCourseTeacherTestCase(TestCase):
	def setUp(self):
		self.student_a=Student.objects.create(first_name="Joy",
			last_name="Wahome",
			date_of_birth=datetime.date(1998,8,25),
			registration_number="123",
			place_of_residence="Nairobi",
			phone_number="123456789",
			email="joy@akirachix.com",
			guardian_phone="12345",
			id_number=1111111,
			date_joined=datetime.date.today(),)

		self.student_b=Student.objects.create(first_name="Ivy",
			last_name="Wahome",
			date_of_birth=datetime.date(1996,5,24),
			registration_number="1234",
			place_of_residence="Nairobi",
			phone_number="123456789",
			email="ivy@akirachix.com",
			guardian_phone="123456",
			id_number=2222222,
			date_joined=datetime.date.today(),)

		self.python=Course.objects.create(name="python",
			duration_in_months=10,
			course_number="1",
			description="Learn Python",)

		self.javascript=Course.objects.create(name="javascript",
			duration_in_months=10,
			course_number="2",
			description="Learn JS",)

		self.hardware=Course.objects.create(name="hardware",
			duration_in_months=10,
			course_number="3",
			description="Build hardware",)

		self.teacher_a=Teacher.objects.create(first_name="James",
			last_name="Mwai",
			date_of_birth=datetime.date(1998,8,25),
			registration_no="123",
			place_of_residence="Nairobi",
			phone_number="123456789",
			email="james@akirachix.com",
			id_number=1111111,
			profession="Consultant",)

		self.teacher_b=Teacher.objects.create(first_name="Barre",
			last_name="Yassin",
			date_of_birth=datetime.date(1998,8,25),
			registration_no="123",
			place_of_residence="Nairobi",
			phone_number="123456789",
			email="barre@akirachix.com",
			id_number=1111111,
			profession="Consultant",)

	def test_student_can_join_many_courses(self):
		self.assertEqual(self.student_a.course.count(),0)
		self.student_a.course.add(self.python)
		self.assertEqual(self.student_a.course.count(),1)
		self.student_a.course.add(self.javascript)
		self.assertEqual(self.student_a.course.count(),2)
		self.student_a.course.add(self.hardware)
		self.assertEqual(self.student_a.course.count(),3)

	def test_course_can_have_many_students(self):
		self.python.students.add(self.student_a,self.student_b)
		self.assertEqual(self.python.students.count(),2)

	def test_teacher_can_have_many_courses(self):
		self.python.teacher=self.teacher_a
		self.javascript.teacher=self.teacher_a
		self.assertEqual(self.python.teacher,self.javascript.teacher)
		
	def test_course_cannot_have_many_teachers(self):
		self.python.teacher=self.teacher_a
		self.assertEqual(self.python.teacher.first_name,"James")
		self.python.teacher=self.teacher_b
		self.assertEqual(self.python.teacher.first_name,"Barre")

	# def test_course_teacher_is_in_student_teachers_list(self):
	# 	self.python.teacher=self.teacher_b
	# 	self.student_b.course.add(self.python)
	# 	teachers=self.student_b.teachers()
	# 	self.assertTrue(self.teacher_b in teachers)


		