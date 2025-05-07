
from app.models.post import Posts
from app.extensions import db
from app.models.comment import Comment


def create_comment(text, author, parentpost):
    comment = Comment(title=text, author=author, parentpost=parentpost)
    db.session.add(comment)
    db.session.commit()
    