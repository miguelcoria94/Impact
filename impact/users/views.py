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

        db.session.add(user)
        db.session.commit()
        flash("Account successfully created!")
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)

@users.login('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = )
