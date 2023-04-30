#from flask import Blueprint
#
#users = Blueprint('users', __name__)
#
#
##Register Page
#@app.route("/register", methods = ['GET', 'POST']) 
#def register():
#    if current_user.is_authenticated:
#        return redirect(url_for('home'))
#    form = RegistrationForm()
#    if form.validate_on_submit(): #
#        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#        user = User(username = form.username.data, email = form.email.data, password = hashed_pw)
#        db.session.add(user)
#        db.session.commit()
#        flash('Account Created! Login Now!!','success') # send flash message ('success' is a bootstrap class)
#        return redirect(url_for('login'))
#    return render_template('register.html', title='Register', form = form)
#
##login Page
#@app.route("/login", methods = ['GET', 'POST']) 
#def login():
#    if current_user.is_authenticated:
#        return redirect(url_for('home'))
#    form = LoginForm()
#    if form.validate_on_submit(): #send flash message
#        user = User.query.filter_by(email=form.email.data).first()
#        if user and bcrypt.check_password_hash(user.password, form.password.data): #compares password from db to password passed into the form
#            login_user(user, remember = form.remember.data)#login using flask_login extension
#            next_page = request.args.get('next')
#            return redirect(next_page) if next_page  else redirect(url_for('home')) # Turnary conditional - redirect to next page if it exists - if not return home
#        else:
#            flash('Login Unsuccessful - Please Check Username and Password', 'danger') # danger is a bootstrap class
#    return render_template('login.html', title='Login', form = form)
#
##logout route - for use when user is logged in
#@app.route("/logout")
#def logout():
#    logout_user()
#    return redirect(url_for('home'))
#
##Accounts route
#@app.route("/account", methods = ['GET', 'POST'])
#@login_required
#def account():
#     form = UpdateAccountForm()
#     if form.validate_on_submit():
#         if form.picture.data:
#             picture_file = save_pic(form.picture.data)
#             current_user.image_file = picture_file
#             if form.picture.data:
#                old_pic = current_user.image_file
#                picture_file = save_pic(form.picture.data)
#                current_user.image_file = picture_file
#                if old_pic != 'default.jpg':
#                    os.remove(os.path.join(app.root_path, 'static/profile_pics', old_pic)) # deletes old picture to save space (not default.jpg)
#         current_user.username = form.username.data #Updates current users username
#         current_user.email = form.email.data       #Updates current users email
#         db.session.commit()
#         flash ('Your Account has been Updated!!', 'success') 
#         return redirect(url_for('account'))
#     elif request.method == 'GET':                 # populates form with the curret username and password (befor update)
#         form.username.data = current_user.username
#         form.email.data = current_user.email
#     image_file = url_for('static', filename = 'profile_pics/' + current_user.image_file)
#     return render_template('account.html', title='Account', image_file=image_file, form=form)
#
#
#
##Show all posts for a specific username
#@app.route("/user/<string:username>") 
#def user_posts(username):
#    page = request.args.get('page', 1, type=int)
#    user = User.query.filter_by(username=username).first_or_404()
#    posts = Post.query.filter_by(author=user)\
#        .order_by(Post.date_posted.desc())\
#        .paginate(page = page, per_page=3) #allows me to define how many posts per page - orders them from newest to oldest
#    return render_template('user_posts.html', posts = posts, user=user) # posts variable within the template is equal to the dummy data
#
#
##Reset user password - page to enter email to request a password reste
#@app.route("/reset_password", methods = ['GET', 'POST'])
#def reset_request():
#    if current_user.is_authenticated:
#        return redirect(url_for('home'))
#    form = RequestResetForm()
#    if form.validate_on_submit():
#        user = User.query.filter_by(email=form.email.data).first()
#        send_reset_email(user)
#        flash('An Email has been send to reset you password', 'info')
#        return redirect (url_for('login'))
#    return render_template('reset_request.html', title='Reset Password', form=form)
#
#
#
##Reset user password with the active token
#@app.route("/reset_password/<token>", methods = ['GET', 'POST'])
#def reset_token(token):
#    if current_user.is_authenticated:
#        return redirect(url_for('home'))
#    user = User.verify_reset_token(token)
#    if user is None:
#        flash('That is an expired or invalid token', 'warning') #'warning' is a bootstrap class
#        return redirect(url_for('reset_request'))
#    form = ResetPasswordForm()
#    if form.validate_on_submit(): #
#        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#        user.password = hashed_pw
#        db.session.commit()
#        flash('Password has been updated!','success') # send flash message ('success' is a bootstrap class)
#        return redirect(url_for('login'))
#    return render_template('reset_token.html', title='Reset Password', form=form)
