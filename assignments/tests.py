from django.test import TestCase
from .models import Student, Class, create_user_profile
# Create your tests here.

class TestTest(TestCase):
    def test_easy(self):
        self.assertEqual(1, 1)

class StudentModelTests(TestCase):
    def test_student_created(self):
        name = "Peter Babadook"
        bio = "CS student who loves 2 code!"
        id = "pb2ce"
        #sex = "M"
        test_student = Student(name=name, bio=bio, id=id)
        self.assertIsInstance(test_student, (Student))

    def test_insert_student(self):
        name = "Johnny Appleseed"
        bio = "History is great"
        id = "ja3fe"
        #sex = "M"
        test_student = Student(name=name, bio=bio)
        #create_user_profile(name, bio)
        test_student = Student(name="Johnny Appleseed", bio=bio)
        self.assertNotEqual(test_student.name, "Johnny K Appleseed")

class ClassModelTests(TestCase):
    def test_class_created(self):
        prefix = "CS"
        course_number = "2150"
        professor = "Aaron Bloomfield"
        semester = "F19"
        test_class = Class(prefix=prefix, course_number=course_number, professor=professor, semester=semester)
        self.assertIsInstance(test_class, (Class))

    def test_insert_class(self):
        prefix = "CS"
        course_number = "2150"
        professor = "Aaron Bloomfield"
        semester = "F19"
        test_class = Class(prefix=prefix, course_number=course_number, professor=professor, semester=semester)
        self.assertEqual(test_class.semester, "F19")

    def test_find_bad_class(self):
        prefix = "CS"
        course_number = "2150"
        professor = "Aaron Bloomfield"
        semester = "F19"
        test_class = Class(prefix=prefix, course_number=course_number, professor=professor, semester=semester)
        self.assertEqual(1, len(test_class.course_number) - len(test_class.semester))