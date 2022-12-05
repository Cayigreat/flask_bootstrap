from app.auth import bp
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user
from app.models.user import User
from app.extensions import db

@bp.route('/')
def index():
    users = User.query.all()
    return render_template('auth/index.html', users= users)

@bp.route('/register', methods = ('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_confirm = request.form['password_confirm']

    if not username:
            flash('El nombre del usuario es obligatorio')
    elif not email:
            flash('El email es obligatorio') 
    elif not password == password_confirm:
            flash('La contraseña no coincide')     
    else:
            user= User(username = username, email = email, password_hash = password)    
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.index'))
    return render_template('auth/register.html')   

@bp.route('/login', methods = ('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = request.form['remember_me']      

        if not password:
            flash('La contraseña es obligatoria')
        elif not email:
            flash('El email es obligatorio')           
        else:
            user= User.query.filter_by(email=email).first()
            if user and user.verify_password(password):
                login_user(user, remember)
                next = request.args.get('next')   if next is None:
                    next = url_for('main.index')
                return redirect(next)        
            flash('usuario o password incorrecto')        
return render_template('auth/login.html') 