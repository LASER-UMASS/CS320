from src.collegemember import CollegeMember
from src.degree import Degree
from src.department import Department

class Faculty(CollegeMember): 
    department = None
    degree = None
    is_on_leave = False

    def __init__(self, id, first_name, last_name, email_address, department, degree):
        super().__init__(id, first_name, last_name, email_address)
        self.set_department(department)
        self.set_degree(degree)
        self.set_is_on_leave(False)
	
    def set_department(self, department):
	    # Check pre-conditions
        if (department == None):
            raise TypeError("The faculty must be associated with an existing department.")
        self.department = department
	
    def get_department(self):
        return self.department

    def set_degree(self, degree):
        # Check the pre-conditions
        if (degree == None):
            raise("The faculty must have an existing degree.")
        self.degree = degree
	
    def get_degree(self):
        return self.degree
    
    def set_is_on_leave(self, is_on_leave):
        self.is_on_leave = is_on_leave

    def get_is_on_leave(self):
        return self.is_on_leave
	
    def get_str_attributes(self): 
        str_attributes = super().get_str_attributes()
		
        str_attributes.update( 
            { "department":  self.get_department(),
		      "degree": self.get_degree(),
		      "is_on_leave": self.get_is_on_leave() })
		
        return str_attributes
	
    def __eq__(self, other):
        if (super().__eq__(other) == False):
            return False
		
        if (self.get_department() != other.get_department()):
            return False
          
        if (self.get_degree() != other.get_degree()):
            return False
		
        if (self.get_is_on_leave() != other.get_is_on_leave()):
            return False
		
        return True
    
#f1 = Faculty(1, "Heather", "Conboy", "hconboy@gcc.edu", Department.COMPUTER_SCIENCE, Degree.PHD)
#print(str(f1))