""" website """
from flask import Flask, Blueprint, render_template, request, redirect, url_for
from flask import flash, jsonify
from web_site.models.User_model import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from web_site  import db, app
from web_site import models
from web_site.views import app_views

app_login = Blueprint('app_login', __name__)


@app_login.route('/login', strict_slashes=False, methods=['GET', 'POST'])
def login_method():
    """method to log in"""
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password1 = data.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password1:
                flash('LOGGED IN!', category="success")
                login_user(user, remember=True)
                return jsonify({'success': True, 'redirect': url_for('app_views.home')})
            else:
                flash('incorrect account details', category="error")
        else:
            flash('No Record', category="error")
    return render_template("login.html", user=current_user)

@app_login.route('/logout', strict_slashes=False)
def logout_method():
    """logs user out"""
    logout_user()
    return redirect(url_for('app_login.login_method'))

@app_login.route('/sign-up', strict_slashes=False, methods=['GET','POST'])
def sign_up_method():
    if request.method == 'POST':
        data = request.get_json()
        name1 = data.get('name')
        surname1 = data.get('surname')
        email1 = data.get('email')
        password1 = data.get('password')

        user = User.query.filter_by(email=email1).first()
        if user:
            flash('Email already exists.')
        else:
            new_user = User(email=email1, name=name1,surname=surname1, password=password1)
            db.session.add(new_user)
            db.session.commit()
            db.session.refresh(new_user)

            db.session.close()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return jsonify({'success': True, 'redirect': url_for('app_login.login_method')})

    return render_template("Register.html", user=current_user)
