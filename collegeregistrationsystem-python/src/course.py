import copy

from src.coursesectionnotfoundexception import CourseSectionNotFoundException
from src.coursesectionfullexception import CourseSectionFullException
from src.faculty import Faculty
from src.facultyonleaveexception import FacultyOnLeaveException

class Course:
    id = 0
    title = ""
    number_of_credits = 0
    course_section_listing = None
	
    def __init__(self, id, title, number_of_credits):
	    # Check the pre-conditions
        if (id < 1):
            raise TypeError("The course ID must be positive.")
        if ((title == None) or (title.strip() == "")):
            raise TypeError("The course title must not be none or empty.")
        if (number_of_credits < 0):
            raise TypeError("The course must be worth zero or more credits.")
        self.id = id
        self.title = title
        self.number_of_credits = number_of_credits
        self.course_section_listing = []

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_number_of_credits(self):
        return self.number_of_credits
    
    def add_course_section(self, course_section_enrollment_cap):
        # This is the factory design pattern.
        new_course_section = CourseSection(self, len(self.course_section_listing) + 1, course_section_enrollment_cap)
        self.course_section_listing.append(new_course_section)
        return new_course_section
    
    def get_course_section(self, course_section_number):
        course_section = None
        for current_course_section in self.course_section_listing:
            if (current_course_section.get_section_number() == course_section_number):
                course_section = current_course_section
                break
        if (course_section == None):
            raise CourseSectionNotFoundException("The course with ID " + str(self.get_id()) + " does not have a section with number " + str(course_section_number) + ".")
        return course_section

    def get_course_section_listing(self):
        # Support information hiding with encapsulation
        #
        # Return a shallow copy
        return copy.copy(self.course_section_listing)

    def __eq__(self, other):
        if (other == None):
            return False
		
        if (self is other):
            return True
        
        if (self.id != other.id):
            return False

        if (self.title != other.title):
            return False

        if (self.number_of_credits != other.number_of_credits):
            return False
		
        return True
    
class CourseSection:
    course = None
    section_number = 0
    enrollment_cap = 0
    assigned_faculty = None
    enrolled_students_listing = None

    def __init__(self, course, section_number, enrollment_cap):
        """For the given course, creates a new course section with the given section number and enrollment cap. If the course isn't specified or either number isn't positive, raises a TypeError."""
		# Check pre-conditions
        if (course == None):
            raise TypeError("The course cannot be none.")
        if (section_number < 1):
            raise TypeError("The course section number must be positive.");
        if (enrollment_cap < 1):
            raise TypeError("The course section enrollment cap must be positive.");
        self.course = course
        self.section_number = section_number
        self.enrollment_cap = enrollment_cap
        self.assigned_faculty = None
        self.enrolled_students_listing = []

    def get_course(self):
        return self.course
    
    def get_section_number(self):
        return self.section_number
    
    def get_enrollment_cap(self):
        return self.enrollment_cap
    
    def assign_faculty(self, assigned_faculty):
        """Assigns the given faculty to teach the course section. If the faculty isn't specified, raises a TypeError. If they are on leave, raises a FacultyOnLeaveException."""
        # Check pre-conditions
        if (assigned_faculty == None):
            raise TypeError("The faculty cannot be none.")
        if (assigned_faculty.get_is_on_leave()):
            raise FacultyOnLeaveException("Faculty with id " + str(assigned_faculty.get_id()) + " is on leave.")
        self.assigned_faculty = assigned_faculty

    def get_assigned_faculty(self):
        return self.assigned_faculty
    
    def find(self, student):
        for i in range(len(self.enrolled_students_listing)):
            current_student = self.enrolled_students_listing[i]
            if (current_student == student):
                return i
            
        return -1

    def enroll (self, new_student):
        """Enrolls the given student in the course section returning True if they were enrolled and False otherwise. Raises TypeError if the student is None. Raises CourseSectionFullException if the enrollment cap has already been reached."""
		# Check the pre-conditions
        if (new_student == None):
            raise TypeError("The new student cannot be none.")
        if (len(self.enrolled_students_listing) == self.enrollment_cap):
            raise CourseSectionFullException("For course " + str(self.get_course().get_id()) + ", section " + str(self.get_section_number) + " is full.")
        found = self.find(new_student)
        if (found == -1):
            self.enrolled_students_listing.append(new_student)
            return True
        else:
            return False
        
    def drop(self, student):
        """Drops the student from the course section returning True if they were enrolled and returning False otherwise."""
        found = self.find(student)
        if (found != -1):
            self.enrolled_students_listing.pop(found)
            return True
        else:
            return False
        
    def get_enrolled_students_listing(self):
        # Support information hiding with encapsulation
        #
        # Return a shallow copy of the enrolled students listing
        return copy.copy(self.enrolled_students_listing)
       