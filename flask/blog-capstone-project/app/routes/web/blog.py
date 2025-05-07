from datetime import datetime
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user
from app.forms.forms import CommentForm, CreatePostForm
from app.services.blog_service import *
from app.services.comment_service import create_comment
from app.services.smtplib_service import send_email
from functools import wraps
from flask import abort
blog_bp = Blueprint('blog', __name__)

#Create admin-only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        #Otherwise continue with the route function
        return f(*args, **kwargs)        
    return decorated_function
  
  
@blog_bp.route('/')
def index():
    all_posts = get_all_posts()
    return render_template("blog_templates/index.html", all_posts=all_posts)

@blog_bp.route("/post/<int:index>", methods=["GET", "POST"])
def show_post(index):
    requested_post = get_post_by_id(index)
    # Add the CommentForm to the route
    comment_form = CommentForm()
    # Only allow logged-in users to comment on posts
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("user.login"))
        create_comment(
            text=comment_form.comment_text.data,
            comment_author=current_user,
            parent_post=requested_post
        )
    if requested_post is None:
        return render_template("404.html"), 404
    return render_template("blog_templates/post.html", post=requested_post, urrent_user=current_user, form=comment_form)


@blog_bp.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    current_time = datetime.now()
    time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    form = CreatePostForm()
    if form.validate_on_submit():
        create_new_post(
            form.title.data, 
            form.subtitle.data, 
            time_str,
            form.img_url.data,
            form.body.data,
            current_user)
        return redirect(url_for('blog.index'))
    else:
        print(form.errors)
    return render_template('blog_templates/make-post.html', form=form)

@blog_bp.route('/update-post/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    current_time = datetime.now()
    time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    form = CreatePostForm()
    post = get_post_by_id(post_id)
    if not post:
        return redirect(url_for('tasks.index'))
    if request.method == 'GET':
        form.title.data = post.title
        form.subtitle.data = post.subtitle
        time_str
        form.img_url.data = post.img_url
        form.body.data = post.body
        current_user
    if form.validate_on_submit():
        update_post(post_id, form.title.data, form.subtitle.data, time_str, form.img_url.data, form.body.data, current_user)
        return redirect(url_for('blog.index'))
    return render_template('blog_templates/make-post.html', form=form, is_update=True)

@blog_bp.route('/delete/<int:post_id>')
@admin_only
def delete(post_id):
    delete_post(post_id)
    return redirect(url_for('blog.index'))

@blog_bp.route('/about')
def about():
    return render_template("blog_templates/about.html")

@blog_bp.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
            name = request.form["name"]
            email = request.form["email"]
            phone = request.form["phone"]
            message = request.form["message"]
            print(name, email, phone, message)
            # send email
            data = request.form
            send_email(data["name"], data["email"], data["phone"], data["message"])
            return render_template("blog_templates/contact.html", msg_sent=True)
    else:   
        return render_template("blog_templates/contact.html", msg_sent=False)