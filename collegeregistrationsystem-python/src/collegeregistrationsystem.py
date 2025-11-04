from src.collegememberregistry import CollegeMemberRegistry
from src.courseregistry import CourseRegistry
from src.coursealreadyexistsexception import CourseAlreadyExistsException

class CollegeRegistrationSystem:
    """Manages the CollegeRegistrationSystem of college members and courses for Greenville Community College."""
    college_member_registry = None
    course_registry = None

    def __init__(self):
        """Creates a new CollegeRegistrationSystem with no college members or courses added yet."""
        self.college_member_registry = CollegeMemberRegistry()
        self.course_registry = CourseRegistry()

    def add_faculty(self, first_name, last_name, email_address, department, degree):
        """Creates a new Faculty from the valid input parameters and adds them to the CollegeMemberRegistry.

        Pre-conditions:
            The first name cannot be none or empty.
            The last name cannot be none or empty.
            The email address cannot be none or empty.
            The department cannot be none.
            The degree cannot be none.

        Returns:
            A new Faculty created from the valid input parameters and added to the CollegeMemberRegistry

        Raises:
            TypeError if any input parameters are invalid
        """
        # This uses the factory method design pattern.
        return self.college_member_registry.add_faculty(first_name, last_name, email_address, department, degree)
    
    def add_student(self, first_name, last_name, date_of_birth, email_address, home_address):
        """Creates a new Student from the valid input parameters and adds them to the CollegeMemberRegistry.
           
        Pre-conditions:
            The first name cannot be none or empty.
            The last name cannot be none or empty.
            The date of birth cannot be none.
            The email address cannot be none or empty.
            The home address cannot be none or empty.

        Returns:
            A new Student created from the valid input parameters and added to the CollegeMemberRegistry

        Raises:
            TypeError if any input parameters are invalid
        """
		# This uses the factory method design pattern.
        return self.college_member_registry.add_student(first_name, last_name, date_of_birth, email_address, home_address)
    
    def get_college_member(self, college_member_id):
        """Retrieves the CollegeMember with the given ID if they already exist in the CollegeMemberRegistry.
        
        Returns:
            A CollegeMember with the given ID if they already exist in the CollegeMemberRegistry

        Raises:            
            CollegeMemberNotFoundException if a CollegeMember with the given ID does not exist
        """
        return self.college_member_registry.get_college_member(college_member_id)
    
    def get_college_member_listing(self):
        """Retrieves a list of all existing college members."""
        return self.college_member_registry.get_college_member_listing()
    
    def add_course(self, title, number_of_credits):
        """Creates a new Course from the valid input parameters and adds it to the CourseRegistry.
        
        Pre-conditions:
            The title cannot be none or empty.
            The number of credits cannot be negative.

        Returns:
            A new Course created from the valid input parameters and added to the CourseRegistry

        Raises:
            TypeError if any input parameters are invalid
            CourseAlreadyExistsException if another course with the same title already exists in the CourseRegistry
        """
        # This uses the factory method design pattern.
        return self.course_registry.add_course(title, number_of_credits)

    def add_course_section(self, course_id, course_section_enrollment_cap):
        """Creates a new CourseSection from the valid input parameters and adds it to the given Course.
        
        Pre-conditions:
            The course section enrollment cap is non-negative.

        Returns:
            A new CourseSection created from the valid input parameters and adds it to the given Course.
        
        Raises:
            TypeError if any input parameters are invalid
            CourseNotFoundException if a Course with the given ID cannot be found in the CourseRegistry
        """
        return self.course_registry.add_course_section(course_id, course_section_enrollment_cap)
    
    def get_course(self, course_id):
        """Retrieves the Course with the given ID if it already exists in the CourseRegistry.
        
        Returns:
            The Course with the given ID if it already exists in the CourseRegistry

        Raises:
            CourseNotFoundException if a course with the given ID does not exist
        """
        return self.course_registry.get_course(course_id)
    
    def get_course_listing(self):
        """Retrieves a list of all existing courses."""
        return self.course_registry.get_course_listing()
    
    def assign_faculty(self, course_id, course_section_num, faculty_id):
        """Assigns the given Faculty to teach the specified CourseSection.

        Raises:
            CollegeMemberNotFoundException if a Faculty with the given ID cannot be found in the CollegeMemberRegistry
            CourseNotFoundException if a Course with the given ID cannot be found in the CourseRegistry
            CourseSectionNotFoundException if a CourseSection with the given section number cannot be found in the Course
            FacultyOnLeaveException if the Faculty is scheduled to be on leave and cannot teach the CourseSection
        """
        existing_course = self.course_registry.get_course(course_id)
        existing_course_section = existing_course.get_course_section(course_section_num)
        existing_faculty = self.college_member_registry.get_college_member(faculty_id)
        existing_course_section.assign_faculty(existing_faculty)

    def enroll(self, course_id, course_section_num, student_id):
        """Enrolls the given Student in the specified CourseSection if that CourseSection is not already full.
        
        Returns:
            True if the given Student is successfully enrolled in the requested CourseSection and False otherwise

        Raises:
            CollegeMemberNotFoundException if a Student with the given ID cannot be found in the CollegeMemberRegistry
            CourseNotFoundException if a Course with the given ID cannot be found in the CourseRegistry
            CourseSectionNotFoundException if a CourseSection with the given section number cannot be found in the Course
            CourseSectionFullException if the CourseSection is already full and not allowing additional enrollments by Students
        """        
        existing_course = self.course_registry.get_course(course_id)
        existing_course_section = existing_course.get_course_section(course_section_num)
        existing_student = self.college_member_registry.get_college_member(student_id)
        return existing_course_section.enroll(existing_student)
    
    def drop(self, course_id, course_section_num, student_id):
        """Drops the given Student from the specified CourseSection if that Student is enrolled in that CourseSection.
        
        Returns:
            True if the given Student successfully drops the requested CourseSection and False otherwise

        Raises:
            CollegeMemberNotFoundException if a Student with the given ID cannot be found in the CollegeMemberRegistry
            CourseNotFoundException if a Course with the given ID cannot be found in the CourseRegistry
            CourseSectionNotFoundException if a CourseSection with the given section number cannot be found in the Course
        """
        existing_course = self.course_registry.get_course(course_id)
        existing_course_section = existing_course.get_course_section(course_section_num)
        existing_student = self.college_member_registry.get_college_member(student_id)
        return existing_course_section.drop(existing_student)