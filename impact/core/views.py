from flask import render_template, request, Blueprint
from impact.models import Post

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    blog_posts = Post.query.order_by(Post.date.desc()).paginate(page=page,per_page=3)
    return render_template('index.html', blog_posts=blog_posts)

@core.route('/about')
def about():
    return render_template('about.html')