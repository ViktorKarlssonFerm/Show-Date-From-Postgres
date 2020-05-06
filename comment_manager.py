from asyncpg_connection import AsyncpgConnection


class CommentManager:

    @staticmethod
    async def get_comments():
        try:
            conn = await AsyncpgConnection.get_connection()
            sql = '''SELECT * FROM comments'''

            await conn.fetch(sql)
            await conn.close()

        except Exception as e:
            print(e)

    @staticmethod
    async def create_comment(text: str, user_id: int):
        try:
            conn = await AsyncpgConnection.get_connection()
            sql = '''INSERT INTO comments(text, created_at, user_id) VALUES ($1, (SELECT current_timestamp), $2)'''

            await conn.execute(sql, text, user_id)

        except Exception as e:
            print(e)
