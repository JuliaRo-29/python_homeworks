import pytest
from models.student_table import models_student_table


DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"

@pytest.fixture(scope="module")
def student_table():
    table = StudentTable(DATABASE_URL)
    table.drop_old_table()
    table.drop_table()
    table.create_table()
    yield table
    table.drop_table()
