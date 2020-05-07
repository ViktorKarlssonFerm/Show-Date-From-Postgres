import json
from uuid import uuid4

from tornado.web import RequestHandler

from comment_manager import CommentManager
from comment_model import CommentModel


class NewCommentHandler(RequestHandler):

    async def post(self):
        try:
            _id = uuid4()
            content = self.get_argument("text", "")
            user_name = self.get_argument("user_name", "")
            comment = CommentModel(_id, content, None, user_name)

            await CommentManager.create_comment(comment)

            self.write(json.dumps({
                'success': True,
                'message': 'Comment was successfully made'
            }))

        except Exception as e:
            print(e)

            self.write(json.dumps({
                'success': False,
                'message': 'Comment could not be created'
            }))


class GetCommentHandler(RequestHandler):

    async def post(self):
        try:
            comment_list = await CommentManager.get_comments()

            if comment_list is not None:
                self.write(json.dumps({
                    'success': True,
                    'values': comment_list
                }))

        except Exception as e:
            print(e)

            self.write(json.dumps({
                'success': False,
                'message': 'Could not get comments'
            }))
