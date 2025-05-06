from app.models.post import Posts
from app.extensions import db
from bleach import clean

#----- Get id of the post -----#
def get_post_by_id(post_id):
    return Posts.query.get_or_404(post_id)

#----- Get all posts -----#
def get_all_posts():
    result = db.session.execute(db.select(Posts))
    posts = result.scalars().all()
    return posts

#----- Create posts -----#
def create_new_post(title, subtitle, body):
    safe_body = clean(body)  # cleanify the body content (CKEditor)
    new_post = Posts(title=title, subtitle=subtitle, body=safe_body)
    db.session.add(new_post)
    db.session.commit()
    
#----- Update post -----#  
def update_post(post_id, title, subtitle, body):
    post = Posts.query.get(post_id)
    if post:
        post.title = title
        post.subtitle = subtitle
        post.body = body
        db.session.commit()
        
#----- Delete post -----#   
def delete_post(post_id):
    post = Posts.query.get_or_404(post_id)
    if post:
        db.session.delete(post)
        db.session.commit()




