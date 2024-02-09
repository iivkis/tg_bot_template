from psycopg2._psycopg import connection, cursor

from internal.domain.user import User


class UserRepository():
    def __init__(self, conn: connection):
        self._conn = conn

    def create(self, telegram_id: int):
        with self._conn.cursor() as cursor:
            try:
                cursor.execute("""
                    INSERT INTO users (telegram_id)
                    VALUES (%s)
                """, (telegram_id,))
                self._conn.commit()
            except Exception as e:
                self._conn.rollback()
                raise e
    def get(self, telegram_id: int) -> User | None:
        with self._conn.cursor() as cursor:
            cursor.execute("""
                SELECT *
                FROM users
                WHERE telegram_id = %s
            """, (telegram_id,))
            result = cursor.fetchone()
            if result is None:
                return None
            return User(
                telegram_id=result[0],
            )

    def get_list(self, limit: int, offset: int = 0) -> list[User]:
        with self._conn.cursor() as cursor:
            cursor.execute("""
                SELECT *
                FROM users
                LIMIT %s
                OFFSET %s
            """, (limit, offset))
            result = cursor.fetchall()
            return [User(
                telegram_id=row[0],
            ) for row in result]
