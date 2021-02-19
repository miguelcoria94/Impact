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
        blog_post = Post(title=form.title.data, text=form.text.data, user_id=current_user.id)

        db.session.add(blog_post)
        db.session.commit()
        return redirect(url_for('core.index'))

    return render_template('create_post.html', form=form)

@blog_posts.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    blog_post = Post.query.get_or_404(blog_post_id)

    return render_template("blog_post.html", title=blog_post.title, date=blog_post.date, post=blog_post)