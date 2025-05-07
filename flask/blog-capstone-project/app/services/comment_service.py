
from app.models.post import Posts
from app.extensions import db
from app.models.comment import Comment


def create_comment(text, comment_author, parent_post):
    comment = Comment(text=text, comment_author=comment_author, parent_post=parent_post)
    db.session.add(comment)
    db.session.commit()
    