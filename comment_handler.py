
import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler

from comment_manager import CommentManager


class NewCommentHandler(RequestHandler):

    async def post(self):
        try:
            print(self.get_argument("text", ""))
            print(self.get_argument("user_id", ""))
            text = self.get_argument("text", "")
            user_id = int(self.get_argument("user_id", ""))

            await CommentManager.create_comment(text, user_id)

        except Exception as e:
            print(e)


class GetCommentHandler(RequestHandler):
    print("potato")
