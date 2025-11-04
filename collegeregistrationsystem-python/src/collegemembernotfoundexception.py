class CollegeMemberNotFoundException(Exception):
    """Should be raised when a college member is not found in the college registration system."""
    
    def __init__(self, message):
        super().__init__(message)

