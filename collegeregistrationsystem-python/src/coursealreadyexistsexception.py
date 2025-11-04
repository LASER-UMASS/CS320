class CourseAlreadyExistsException(Exception):
    """Should be raised when a course already exists in the college registration system."""
    
    def __init__(self, message):
        super().__init__(message)

