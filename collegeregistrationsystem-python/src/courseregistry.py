from src.course import Course, CourseSection
from src.coursealreadyexistsexception import CourseAlreadyExistsException
from src.coursenotfoundexception import CourseNotFoundException

class CourseRegistry:
    map_id_to_course = None

    def __init__(self):
        self.map_id_to_course = {}

    def __get_next_id(self):
        return len(self.map_id_to_course) + 1
    
    def add_course(self, title, number_of_credits):
		# Check the pre-conditions
        current_course = None
        for current_course in self.map_id_to_course.values():
            if (current_course.get_title() == title):
                raise CourseAlreadyExistsException("The course registry already contains a course titled \"" + title + "\".");
		# This is the factory method design pattern.
        new_course = Course(self.__get_next_id(), title, number_of_credits)
        self.map_id_to_course[new_course.get_id()] = new_course
        return new_course
    
    def add_course_section(self, course_id, course_section_enrollment_cap):
		# Check the pre-conditions
        existing_course = self.get_course(course_id)
        return existing_course.add_course_section(course_section_enrollment_cap)
    
    def get_course(self, course_id):
        # Check the pre-conditions
        if (not (course_id in self.map_id_to_course.keys())):
            raise CourseNotFoundException("A course with ID " + str(course_id) + " does not exist.");
        return self.map_id_to_course.get(course_id)

    def get_course_listing(self):
        #TODO) Shallow copy?
        return list(self.map_id_to_course.values())