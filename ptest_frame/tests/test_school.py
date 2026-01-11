"""
Pytest Test Suite for Classroom Management System (Harry Potter Theme).

This module contains unit tests for the classroom management functionality
implemented in the `source.school` module. The tests are themed around a
Harry Potter classroom scenario and validate core behaviors of the
Classroom, Teacher, and Students classes.

Test Coverage:
- Verifies that students can be added to a classroom.
- Tests adding multiple students using parameterized inputs.
- Validates removal of a student by name.
- Confirms that the classroom teacher can be updated.
- Ensures the classroom course title is set correctly.
- Documents the known defect related to classroom capacity limits.

Fixtures:
- hogwarts_classroom:
  Provides a reusable Classroom instance initialized with:
    - Teacher: Minerva McGonagall
    - Initial students: Harry Potter, Hermione Granger, Ron Weasley
    - Course title: Defence Against the Dark Arts

Pytest Features Used:
- Fixtures: For reusable test setup.
- pytest.mark.parametrize: To test adding multiple students with different inputs.
- pytest.mark.xfail: To document a known failure where the TooManyStudent
  exception is not raised when the classroom exceeds its capacity.
- pytest.mark.gryffindor: Custom marker used to group Harry Potter–themed tests.
- pytest.raises: Used within expected-failure tests to validate exception behavior.
- Assertions: To verify expected outcomes.

Dependencies:
- pytest: Testing framework.
- source.school: Module under test containing Classroom, Teacher, Students,
  and TooManyStudent classes.

Notes:
- The classroom capacity test is intentionally marked as xfail to document
  an existing issue in the application logic.
- Custom markers such as "gryffindor" should be registered in pytest.ini
  to avoid warnings during test execution.

Author:
- Test suite maintained by the QA/Automation team.

"""

import pytest
from source.school import Classroom, Teacher, Students, TooManyStudent


# 🪄 Fixture: Hogwarts Classroom
@pytest.fixture
def hogwarts_classroom():
    teacher = Teacher("Minerva McGonagall")
    students = [
        Students("Harry Potter"),
        Students("Hermione Granger"),
        Students("Ron Weasley"),
    ]
    return Classroom(
        teacher=teacher,
        students=students,
        course_title="Defence Against the Dark Arts",
    )


# ⚡ Parametrize: Add Multiple Students
@pytest.mark.parametrize(
    "student_name",
    [
        "Neville Longbottom",
        "Luna Lovegood",
        "Ginny Weasley",
    ],
)
def test_add_students(hogwarts_classroom, student_name):
    hogwarts_classroom.add_student(Students(student_name))
    assert student_name in [s.name for s in hogwarts_classroom.students]


# 🧨 Expected Failure: Classroom Capacity Bug
@pytest.mark.xfail(reason="TooManyStudent exception is not raised in code")
def test_classroom_capacity_limit(hogwarts_classroom):
    for i in range(10):
        hogwarts_classroom.add_student(Students(f"Student-{i}"))

    with pytest.raises(TooManyStudent):
        hogwarts_classroom.add_student(Students("Draco Malfoy"))


# Remove Student
def test_remove_student(hogwarts_classroom):
    hogwarts_classroom.remove_student("Harry Potter")
    assert "Harry Potter" not in [s.name for s in hogwarts_classroom.students]


# Change Teacher
def test_change_teacher(hogwarts_classroom):
    hogwarts_classroom.change_teacher(Teacher("Severus Snape"))
    assert hogwarts_classroom.teacher.name == "Severus Snape"


# 🏷️ Marked Test: Gryffindor Classroom
@pytest.mark.gryffindor
def test_course_title(hogwarts_classroom):
    assert hogwarts_classroom.course_title == "Defence Against the Dark Arts"
