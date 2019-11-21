# from django.test import TestCase
# from course.models import Course
# from teacher.models import Teacher
# import datetime

# class CourseTeacherTestCase(TestCase):
# 	def setUp(self):
# 		self.teacher_a=Teacher.objects.create(first_name="James",
# 			last_name="Mwai",
# 			date_of_birth=datetime.date(1998,8,25),
# 			registration_no="123",
# 			place_of_residence="Nairobi",
# 			phone_number="123456789",
# 			email="james@akirachix.com",
# 			id_number=1111111,
# 			profession="Consultant")

# 		self.teacher_b=Teacher.objects.create(first_name="Barre",
# 			last_name="Yassin",
# 			date_of_birth=datetime.date(1996,5,24),
# 			registration_no="1234",
# 			place_of_residence="Nairobi",
# 			phone_number="123456789",
# 			email="barre@akirachix.com",
# 			id_number=2222222,
# 			profession="Consultant",)

# 		self.python=Course.objects.create(name="python",
# 			duration_in_months=10,
# 			course_number="1",
# 			description="Learn Python",)

# 		self.javascript=Course.objects.create(name="javascript",
# 			duration_in_months=10,
# 			course_number="2",
# 			description="Learn JS",)

# 		self.hardware=Course.objects.create(name="hardware",
# 			duration_in_months=10,
# 			course_number="3",
# 			description="Build hardware",)


# 	def test_teacher_can_have_many_courses(self):
# 		self.assertEqual(self.teacher_a.courses.count(),0)
# 		self.teacher_a.course.add(self.python)
# 		self.assertEqual(self.teacher_a.courses.count(),1)
# 		self.teacher_a.course.add(self.javascript)
# 		self.assertEqual(self.teacher_a.course.count(),2)
# 		self.teacher_a.course.add(self.hardware)
# 		self.assertEqual(self.teacher_a.course.count(),3)

# 	def test_course_cannot_have_many_teachers(self):
# 		self.python.teacher=self.teacher_a
# 		self.python.teacher=self.teacher_b
# 		self.assertFalse(self.python.teacher==self.teacher_a)
