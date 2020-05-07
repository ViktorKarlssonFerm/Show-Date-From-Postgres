from uuid import UUID

from asyncpg_connection import AsyncpgConnection
from comment_model import CommentModel


class CommentManager:

    @staticmethod
    async def get_comments():
        try:
            conn = await AsyncpgConnection.get_connection()
            sql = '''SELECT * FROM comments'''

            results = await conn.fetch(sql)
            await conn.close()

            comments = []
            for result in results:
                print(result["created_at"])
                comment = CommentModel(result["id"], result["content"], result["created_at"], result["user_name"])
                comments.append(comment.to_json())

            return comments

        except Exception as e:
            print(e)

    @staticmethod
    async def create_comment(comment: CommentModel):
        try:
            conn = await AsyncpgConnection.get_connection()
            sql = '''INSERT INTO comments(id, content, created_at, user_name) VALUES ($1, $2, (SELECT current_timestamp), $3)'''

            await conn.execute(sql, comment.get_id(), comment.get_content(), comment.get_user_name())
            await conn.close()

        except Exception as e:
            print(e)
