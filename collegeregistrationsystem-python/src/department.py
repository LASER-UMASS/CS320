from enum import Enum

class Department(Enum): 
	ART = 1,
	BUSINESS = 2,
	COMPUTER_SCIENCE = 3,
	ENGLISH = 4,
	MATH = 5
	
# print(str(Department.ART))
# print("equals yourself: " + str(Department.ART == Department.ART))
# print("equals someone else: " + str(Department.ART == Department.COMPUTER_SCIENCE))
