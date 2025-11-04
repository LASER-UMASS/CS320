import datetime

from src.collegemember import CollegeMember

class Student(CollegeMember):
    """Represents a Student as a CollegeMember with the following valid identifiers: id, first name, last name, email address, date of birth, and home address."""
    date_of_birth = None
    home_address = ""

    def __init__(self, id, first_name, last_name, email_address, date_of_birth, home_address):
        """Creates a new Student as a CollegeMember with the following identifiers: id, first name, last name, email address, date of birth, home address. If any identifier is invalid, raises a TypeError."""
        super().__init__(id, first_name, last_name, email_address)
        self.set_date_of_birth(date_of_birth)
        self.set_home_address(home_address)

    def set_date_of_birth(self, date_of_birth):
        # Check the pre-conditions for the input validation
        if (date_of_birth == None):
            raise TypeError("A Student must have a valid date of birth (i.e. non-none).")
        self.date_of_birth = date_of_birth

    def get_date_of_birth(self):
        return self.date_of_birth

    def set_home_address(self, home_address):
        # Check the pre-conditions for the input validation
        if ((home_address == None) or (home_address.strip() == "")):
            raise TypeError("The Student home address must be not none or empty.")
        self.home_address = home_address.strip()

    def get_home_address(self):
        return self.home_address
    
    def __eq__(self, other):
        if (super().__eq__(other) == False):
            return False
        
        if (self.date_of_birth != other.date_of_birth):
            return False
        
        if (self.home_address != other.home_address):
            return False
        
        return True

    def get_str_attributes(self):
        str_attributes = super().get_str_attributes()
        str_attributes.update({ "data_of_birth": self.get_date_of_birth(), "home_address": self.get_home_address() })
        return str_attributes
    
#st = Student(1, "Jane", "Doe", "jdoe@gcc.edu", datetime.date(2007, 10, 31), "1 Main Street, GCC, MA, 12345")
#print(str(st))