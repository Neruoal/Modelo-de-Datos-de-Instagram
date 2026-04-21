from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum

db = SQLAlchemy()

class MediaType(Enum):
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    firstname: Mapped[str] = mapped_column(String, nullable=False)
    lastname: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email
        }

class Follower(db.Model):
    id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True)
    user: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user
        }
    
class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
        }

class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(200), nullable=True)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey('post.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "author_id": self.author_id,
            "post_id": self.post_id
        }

class Media (db.model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[MediaType] = mapped_column(SQLAlchemyEnum(MediaType), nullable=False)
    url: Mapped[str] = mapped_column(String, unique=True)
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey('post.id'), unique=True)

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type.value,
            "url": self.url,
            "post_id": self.post_id
        }