from src.collegemembernotfoundexception import CollegeMemberNotFoundException
from src.faculty import Faculty
from src.student import Student

class CollegeMemberRegistry:
    map_id_to_college_member = None

    def __init__(self):
        self.map_id_to_college_member = {}

    def __get_next_id(self):
        return len(self.map_id_to_college_member) + 1
    
    def __add_college_member(self, college_member):
        self.map_id_to_college_member[college_member.get_id()] = college_member

    def add_faculty(self, first_name, last_name, email_address, department, degree):
		# This is the factory method design pattern.
        new_faculty = Faculty(self.__get_next_id(), first_name, last_name, email_address, department, degree)
        self.__add_college_member(new_faculty)
        return new_faculty
    
    def add_student(self, first_name, last_name, email_address, date_of_birth, home_address):
        # This is the factory method design pattern.
        new_student = Student(self.__get_next_id(), first_name, last_name, date_of_birth, email_address, home_address)
        self.__add_college_member(new_student)
        return new_student
    
    def get_college_member(self, college_member_id):
        college_member = self.map_id_to_college_member.get(college_member_id);
        if (college_member == None):
            raise CollegeMemberNotFoundException("The college member registry does not contain a college member with ID " + str(college_member_id) + ".")
        return college_member
    
    def get_college_member_listing(self):
        #TODO) Shallow copy?
        return list(self.map_id_to_college_member.values())