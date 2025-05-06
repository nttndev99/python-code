from flask import Blueprint, flash, redirect, render_template, request, url_for
from app.forms.forms import CreatePostForm
from app.services.blog_service import *
from app.services.smtplib_service import send_email
blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def index():
    all_posts = get_all_posts()
    return render_template("index.html", all_posts=all_posts)

@blog_bp.route("/post/<int:index>")
def show_post(index):
    blog_post = get_post_by_id(index)
    if blog_post is None:
        return render_template("404.html"), 404
    return render_template("post.html", post=blog_post)


@blog_bp.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        create_new_post(
            form.title.data, 
            form.subtitle.data, 
            form.body.data)
        return redirect(url_for('blog.index'))
    else:
        print(form.errors)
    return render_template('make-post.html', form=form)

@blog_bp.route('/update-post/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    form = CreatePostForm()
    post = get_post_by_id(post_id)
    if not post:
        return redirect(url_for('tasks.index'))
    if request.method == 'GET':
        form.title.data = post.title
        form.subtitle.data = post.subtitle
        form.body.data = post.body
    if form.validate_on_submit():
        update_post(post_id, form.title.data, form.subtitle.data, form.body.data)
        return redirect(url_for('blog.index'))
    return render_template('make-post.html', form=form, is_update=True)

@blog_bp.route('/delete/<int:post_id>')
def delete(post_id):
    delete_post(post_id)
    return redirect(url_for('blog.index'))

@blog_bp.route('/about')
def about():
    return render_template("about.html")

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
            return render_template("contact.html", msg_sent=True)
    else:   
        return render_template("contact.html", msg_sent=False)