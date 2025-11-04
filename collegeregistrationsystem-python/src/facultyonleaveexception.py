class FacultyOnLeaveException(Exception):
    """Should be raised when a faculty member is on leave in the college registration system."""
    
    def __init__(self, message):
        super().__init__(message)

