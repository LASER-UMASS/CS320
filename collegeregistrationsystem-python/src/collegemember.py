class CollegeMember:
    """Represents a CollegeMember by their valid id, first name, last name, and email address."""
    id = -1
    first_name = ""
    last_name  = ""
    email_address = ""

    def __init__(self, id, first_name, last_name, email_address):
        """Creates a new CollegeMember with the given identifiers: id, first name, last name, email address. If any identifier is invalid, raises a TypeError."""
        # Check the pre-conditions for the input validation
        if (id < 1):
            raise TypeError("The CollegeMember must have a postive id.")
        self.id = id
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email_address(email_address)

    def get_id(self):
        return self.id

    def set_first_name(self, first_name):
        # Check the pre-conditions for the input validation
        if ((first_name == None) or (first_name.strip() == "")):
            raise TypeError("The CollegeMember first name must be not none or empty.")
        self.first_name = first_name.strip()

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name):
        # Check the pre-conditions for the input validation
        if ((last_name == None) or (last_name.strip() == "")):
            raise TypeError("The CollegeMember last name must be not none or empty.")
        self.last_name = last_name.strip()

    def get_last_name(self):
        return self.last_name

    def set_email_address(self, email_address):
        # Check the pre-conditions for the input validation
        if ((email_address == None) or (email_address.strip() == "")):
            raise TypeError("The CollegeMember email address must be not none or empty.")
        self.email_address = email_address.strip()

    def get_email_address(self):
        return self.email_address
    
    def __eq__(self, other):
        if (other == None):
            return False
        
        if (self is other):
            return True
        
        if (self.id != other.id):
            return False
        
        if (self.first_name != other.first_name):
            return False
        
        if (self.last_name != other.last_name):
            return False
        
        if (self.email_address != other.email_address):
            return False
        
        return True

    def get_str_attributes(self):
        """Gets the CollegeMember attributes to be returned by the __str__ method."""
        str_attributes = {
           "id": self.get_id(),
           "first_name": self.get_first_name(),
           "last_name": self.get_last_name(),
           "email_address": self.get_email_address() 
        }
        return str_attributes

    def __str__(self):
        return self.__class__.__name__ + str(self.get_str_attributes())  
 
# cm1 = CollegeMember(1, "Amber", "Conboy", "aconboy@gcc.edu")
# print(str(cm1))
# print("equals yourself: " + str((cm1 == cm1)))
# cm1Clone = CollegeMember(1, "Amber", "Conboy", "aconboy@gcc.edu")
# print("equals your clone: " + str((cm1 == cm1Clone)))
# cm2 = CollegeMember(2, "Ben", "Conboy", "bconboy@gcc.edu")
# print(str(cm2))
# print('equals: ' + str(cm1 == cm2))         
