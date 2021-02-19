from flask import render_template, url_for, flash, request, redirect, Blueprint
from flask_login import current_user, login_required
from impact import db
from impact.models import Post
from impact.posts.forms import PostForm

blog_posts = Blueprint('blog_post', __name__)

@blog_posts.route('/create', methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm()

    if form.validate_on_submit():
        blog_post = Post(title=)