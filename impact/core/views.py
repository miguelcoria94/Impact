from flask import render_template, request, Blueprint
from impact.models import Post

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    blog_posts = Post.query.order_by(Post.date.desc()).paginate(page=page,per_page=4)
    latest_post = Post.query.order_by(Post.date.desc()).first()
    return render_template('index.html', blog_posts=blog_posts, latest_post=latest_post)

@core.route('/development')
def development():
    return render_template('development.html')