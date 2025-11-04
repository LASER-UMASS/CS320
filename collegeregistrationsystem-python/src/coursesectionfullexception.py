class CourseSectionFullException(Exception):
    """Should be raised when there is a full course section in the college registration system."""
    
    def __init__(self, message):
        super().__init__(message)

