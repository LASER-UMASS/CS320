class CourseNotFoundException(Exception):
    """Should be raised when a course cannot be found in the college registration system."""
    
    def __init__(self, message):
        super().__init__(message)

