import datetime
import unittest

from src.student import Student

from tests.constants import STUDENT_FIRST_ID
from tests.constants import STUDENT_1_FIRSTNAME_VALID
from tests.constants import STUDENT_1_LASTNAME_VALID
from tests.constants import STUDENT_1_DATEOFBIRTH_VALID
from tests.constants import STUDENT_1_EMAILADDRESS_VALID
from tests.constants import STUDENT_1_HOMEADDRESS_VALID
from tests.constants import STUDENT_1_HOMEADDRESS_INVALID

class CollegeMemberTest(unittest.TestCase):
    # Create a test fixture of a well-formed Student
    student = None

    def setUp(self):
        self.student = Student(STUDENT_FIRST_ID, STUDENT_1_FIRSTNAME_VALID, STUDENT_1_LASTNAME_VALID, STUDENT_1_EMAILADDRESS_VALID, STUDENT_1_DATEOFBIRTH_VALID, STUDENT_1_HOMEADDRESS_VALID)
        return super().setUp()
    
    def tearDown(self):
        self.student = None
        return super().tearDown()
    
    def check_create_student_postconditions(self):
        # Check the post-conditions
        self.assertIsNotNone(self.student)
        self.assertEqual(self.student.get_id(), STUDENT_FIRST_ID)
        self.assertEqual(self.student.get_first_name(), STUDENT_1_FIRSTNAME_VALID)
        self.assertEqual(self.student.get_last_name(), STUDENT_1_LASTNAME_VALID)
        self.assertEqual(self.student.get_email_address(), STUDENT_1_EMAILADDRESS_VALID)
        self.assertEqual(self.student.get_date_of_birth(), STUDENT_1_DATEOFBIRTH_VALID)
        self.assertEqual(self.student.get_home_address(), STUDENT_1_HOMEADDRESS_VALID)
    
    def test_create_student_violates_preconditions(self):
        # Call the unit under test
        with self.assertRaises(TypeError):
            Student(STUDENT_FIRST_ID, STUDENT_1_FIRSTNAME_VALID, STUDENT_1_LASTNAME_VALID, STUDENT_1_EMAILADDRESS_VALID, STUDENT_1_DATEOFBIRTH_VALID, STUDENT_1_HOMEADDRESS_INVALID)
        # Check the post-conditions
        #
        # Since the new home adddress is invalid, should raise TypeError (See the with statement)

    def test_create_student_satisfies_preconditions(self):
        # Call the unit under test (See setUp method)
        #
        # Check the post-conditions
        self.check_create_student_postconditions()

    def test_update_student_violates_preconditions(self):
        # Perform the setup and check pre-conditions
        self.check_create_student_postconditions()
        new_home_address = STUDENT_1_HOMEADDRESS_INVALID
        self.assertIsNotNone(new_home_address)
        self.assertTrue(new_home_address.strip() == "")
        # Call the unit under test
        with self.assertRaises(TypeError):
            self.student.set_home_address(new_home_address)
        # Check the post-conditions
        #
        # Since the new home adddress is invalid, should raise TypeError (See the with statement)

    def test_update_student_satisfies_preconditions(self):
        # Perform the setup and check pre-conditions
        self.check_create_student_postconditions()
        new_home_address = "3 Elm Street, Smalltown, MA, 01234"
        self.assertIsNotNone(new_home_address)
        self.assertTrue(new_home_address.strip() != "")
        # Call the unit under test
        self.student.set_home_address(new_home_address)
        # Check the post-conditions
        self.assertEqual(self.student.get_home_address(), new_home_address)

    def test_equal_student_against_none(self):
        # Perform setup and check pre-conditions
        student_none = None
        self.assertIsNone(student_none)
        # Call the unit under test
        equal_result = (self.student == student_none)
        # Check the post-conditions
        self.assertFalse(equal_result)

    def test_equal_student_against_itself(self):
        # Perform setup and check pre-conditions
        self.check_create_student_postconditions()
        # Call the unit under test
        equal_result = (self.student == self.student)
        # Check the pre-conditions
        self.assertTrue(equal_result)

