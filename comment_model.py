
from datetime import datetime
from uuid import UUID


class CommentModel:

    def __init__(self, _id: UUID, content: str, created_at: datetime, user_name: str):
        self._id = _id
        self._content = content
        self._created_at = created_at
        self._user_name = user_name

    def get_id(self):
        return self._id

    def set_id(self, _id: UUID):
        self._id = _id

    def get_content(self):
        return self._content

    def set_content(self, content: str):
        self._content = content

    def get_created_at(self):
        return self._created_at

    def set_created_at(self, created_at: datetime):
        self._created_at = created_at

    def get_user_name(self):
        return self._user_name

    def set_user_name(self, user_name: str):
        self._user_name = user_name

    def to_json(self):
        json_dict = {
            "id": str(self._id),
            "content": self._content,
            "created_at": str(self._created_at),
            "user_name": self._user_name
        }

        return json_dict

