from sqlalchemy import create_engine, text


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
        "drop_old_table": text("DROP TABLE IF EXISTS student"),
        "insert": text("INSERT INTO students (name, email) VALUES (:name, :email)"),
        "select_by_email": text("SELECT * FROM students WHERE email = :email"),
        "update_name": text("UPDATE students SET name = :new_name WHERE email = :email"),
        "delete_by_email": text("DELETE FROM students WHERE email = :email")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create_table(self):
        conn = self.__db.connect()
        trans = conn.begin()
        try:
            conn.execute(self.__scripts["create_table"])
            trans.commit()
        except:
            trans.rollback()
            raise
        conn.close()

    def drop_table(self):
        conn = self.__db.connect()
        trans = conn.begin()
        try:
            conn.execute(self.__scripts["drop_table"])
            trans.commit()
        except:
            trans.rollback()
            raise
        conn.close()

    def drop_old_table(self):
        conn = self.__db.connect()
        trans = conn.begin()
        try:
            conn.execute(self.__scripts["drop_old_table"])
            trans.commit()
        except:
            trans.rollback()
            raise
        conn.close()

    def add_student(self, name, email):
        conn = self.__db.connect()
        trans = conn.begin()
        try:
            conn.execute(self.__scripts["insert"], {"name": name, "email": email})
            trans.commit()
        except:
            trans.rollback()
            raise
        conn.close()

    def get_student_by_email(self, email):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select_by_email"], {"email": email})
        student = result.mappings().all()
        conn.close()
        return student

    def update_student_name(self, email, new_name):
        conn = self.__db.connect()
        trans = conn.begin()
        try:
            conn.execute(self.__scripts["update_name"], {"email": email, "new_name": new_name})
            trans.commit()
        except:
            trans.rollback()
            raise
        conn.close()

    def delete_student(self, email):
        conn = self.__db.connect()
        trans = conn.begin()
        try:
            conn.execute(self.__scripts["delete_by_email"], {"email": email})
            trans.commit()
        except:
            trans.rollback()
            raise
        conn.close()
