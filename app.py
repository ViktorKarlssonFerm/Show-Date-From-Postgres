import os
import asyncio

import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler

from comment_handler import NewCommentHandler, GetCommentHandler


class Main(RequestHandler):

    async def get(self):
        await self.render("comments.html")


class App(tornado.web.Application):
    def __init__(self):
        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "static")
        }
        tornado.web.Application.__init__(self, [
            tornado.web.url(r"/", Main),
            tornado.web.url(r"/api/create_comment", NewCommentHandler),
            tornado.web.url(r"/api/get_comments", GetCommentHandler)
        ], **settings)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app = App()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
