import pytest
from sqlalchemy import create_engine, text
import uuid


class StudentTable:
    __scripts = {
        "create_table": text("""
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                name VARCHAR NOT NULL,
                email VARCHAR NOT NULL UNIQUE
            )
        """),
        "drop_table": text("DROP TABLE IF EXISTS students"),
        "insert": text("INSERT INTO students (name, email) VALUES (:name, :email)"),
        "select_by_email": text("SELECT * FROM students WHERE email = :email"),
        "update_name": text("UPDATE students SET name = :new_name WHERE email = :email"),
        "delete_by_email": text("DELETE FROM students WHERE email = :email")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create_table(self):
        conn = self.__db.connect()
        conn.execute(self.__scripts["create_table"])
        conn.close()

    def drop_table(self):
        conn = self.__db.connect()
        conn.execute(self.__scripts["drop_table"])
        conn.close()

    def add_student(self, name, email):
        conn = self.__db.connect()
        conn.execute(self.__scripts["insert"], {"name": name, "email": email})
        conn.close()

    def get_student_by_email(self, email):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select_by_email"], {"email": email})
        student = result.mappings().all()
        conn.close()
        return student

    def update_student_name(self, email, new_name):
        conn = self.__db.connect()
        conn.execute(self.__scripts["update_name"], {"email": email, "new_name": new_name})
        conn.close()

    def delete_student(self, email):
        conn = self.__db.connect()
        conn.execute(self.__scripts["delete_by_email"], {"email": email})
        conn.close()


DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"


# Фикстура для создания и удаления таблицы
@pytest.fixture(scope="module")
def student_table():
    table = StudentTable(DATABASE_URL)
    table.create_table()
    yield table
    table.drop_table()


# Добавление студента
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
