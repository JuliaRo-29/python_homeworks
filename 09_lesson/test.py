import pytest
import uuid
from models.student_table import StudentTable


# Дбавления студента
def test_add_student(student_table):
    unique_email = f"test_{uuid.uuid4()}@example.com"
    student_table.add_student("John Doe", unique_email)

    result = student_table.get_student_by_email(unique_email)
    assert len(result) == 1
    assert result[0]["name"] == "John Doe"
    assert result[0]["email"] == unique_email

    student_table.delete_student(unique_email)


# Изменение студента
def test_update_student(student_table):
    unique_email = f"test_{uuid.uuid4()}@example.com"
    student_table.add_student("Jane Doe", unique_email)

    student_table.update_student_name(unique_email, "Jane Smith")

    result = student_table.get_student_by_email(unique_email)
    assert len(result) == 1
    assert result[0]["name"] == "Jane Smith"

    student_table.delete_student(unique_email)


# Удаление студента
def test_delete_student(student_table):
    unique_email = f"test_{uuid.uuid4()}@example.com"
    student_table.add_student("Bob Wilson", unique_email)

    student_table.delete_student(unique_email)

    result = student_table.get_student_by_email(unique_email)
    assert len(result) == 0
