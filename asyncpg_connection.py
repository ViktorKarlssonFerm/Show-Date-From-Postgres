
import asyncpg


class AsyncpgConnection:

    @staticmethod
    async def get_connection():
        try:
            conn = await asyncpg.connect(user='postgres',
                                         password='postgres',
                                         database='datebase',
                                         port="8888",
                                         command_timeout=60)
            return conn

        except ConnectionError as e:
            print(e)
