class CourseSectionNotFoundException(Exception):
    """Should be raised when a course section cannot be found in the college registration system."""
    
    def __init__(self, message):
        super().__init__(message)

