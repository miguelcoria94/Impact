from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from impact import db
from impact.models import User, Post
from impact.users.forms import RegisterForm, LoginForm, UpdateUserForm
from impact.users.picture_handler import add_profile_pic

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

        

    if form.validate_on_submit():

        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

            # flash(u'Please make sure your passwords match!', 'error')

        useremailcheck = User.query.filter_by(email=form.email.data).first()
        usernamecheck = User.query.filter_by(username=form.username.data).first()

        
        if useremailcheck != None:
            flash(u'The email you entered is already taken!', 'error')
            return render_template('register.html', form=form)

        if usernamecheck != None:
            flash(u'The username you entered is already taken!', 'error')
            return render_template('register.html', form=form)

        db.session.add(user)
        db.session.commit()
        flash(u'Your account was successfully created!', 'success')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()


        if user == None:
            flash(u'There was a problem finding your account!', 'error')
            return render_template('login.html', form=form)

        if user.check_password(form.password.data) is False:
            flash(u'Incorrect email or password!', 'error')
            return render_template('login.html', form=form)

            
        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('Welcome Back!', 'success')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('core.index')

            return redirect(next)


    return render_template('login.html', form=form)


@users.route('/logout')
def logout():
    logout_user()
    flash(u'Your account was successfully logged out!', 'success')
    return redirect(url_for("core.index"))



@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():

    form = UpdateUserForm()


    if form.validate_on_submit():

        email = User.query.filter_by(email=form.email.data).first()
        user = User.query.filter_by(username=form.username.data).first()

        if form.avatar.data:
            username = current_user.username
            pic = add_profile_pic(form.avatar.data, username)
            current_user.profile_image = pic

        if form.username.data == current_user.username and form.email.data == current_user.email:
            flash('Your account is already up to date!', 'success')
            db.session.commit()
            return redirect(url_for('users.account'))

        if user is not None and email is not None:
            flash('Your account could not be updated', 'error')
            db.session.commit()
            return redirect(url_for('users.account'))



        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(u'Your account has been successfully updated!', 'success')
        return redirect(url_for('users.account'))

    
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email


    profile_image = url_for('static', filename='profile_pics/' + current_user.profile_image)
    return render_template('account.html', profile_image=profile_image, form=form)

@users.route("/<username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).order_by(Post.date.desc()).paginate(page=page, per_page=5)
    return render_template(('user_posts.html'), posts=posts, user=user)

