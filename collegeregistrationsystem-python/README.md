# Overview:

This is an initial prototype of the backend for the college registration system for Greenville Community College:
- src: Contains the code for this application (as python source files)
- tests: Contains the test suite for the application (as a python source file)
- requirements.txt: Contains the testing build dependencies (as a python requirements file)

# Building:

You need to have the following installed:
- python 3 or higher
- pip 22 or higher

Here are the step-by-step instructions:

1. Set the python path to be able to find the application and its test suite:
   
    `export PYTHONPATH=$PWD` on MacOS/Linux
   
    `$env:PYTHONPATH="$PWD"` on Windows (Powershell)
   
2. Create a new testing virtual environment:
   
    `python -m venv env_testing`

3. Activate the testing virtual environment:

    `source env_testing/bin/activate` on MacOS/Linux
   
    `env_testing\Scripts\Activate` on Windows (Powershell)
   
4. Install the testing build dependencies:
   
    `pip install -r requirements.txt`

# Testing:

The college registration system test suite is contained in this file:
    `tests/test_collegeregistrationsystem.py`
It contains 15 test cases. You are responsible for implementing the 6 test cases marked with:
    `#TODO`

## Run all of the test cases in your test suite

    `pytest --verbose tests/test_collegeregistrationsystem.py` on MacOS/Linux

    `pytest --verbose tests\test_collegeregistrationsystem.py` on Windows (Powershell)

Initially 6 test cases should fail (i.e. the TODOs) and 9 test cases should pass.

Your final test suite needs to have all test cases passing.

## Generate a code coverage report of the test suite

1. Run the code coverage tool

    `coverage run -m pytest --verbose tests/test_collegeregistrationsystem.py` on MacOS/Linux

    `coverage run -m pytest --verbose tests\test_collegeregistrationsystem.py` on Windows (Powershell)

2. Generate the code coverage tool's report

   `coverage report`

3. Convert this report to HTML

   `coverage html`

4. Open the report (found in htmlcov/index.html) in your web browser
   
