import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from Fblog import app, db, bcrypt, mail
from Fblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm
from Fblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message

# Dummy Data
#posts = [
#    {
#        'author': "Enda Lynch",
#        'title': "Blog post 1",
#        "content": "First Post Content",
#        "date_posted": "April 13th 2023"
#    },
#    {
#        'author': "Colm Lynch",
#        'title': "Blog post 2",
#        "content": "Second Post Content",
#        "date_posted": "April 14th 2023"
#    }
#]



#root page(Homepage)
@app.route("/") 
@app.route("/home") 
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = page, per_page=3) #allows me to define how many posts per page - orders them from newest to oldest
    return render_template('home.html', posts = posts) # posts variable within the template is equal to the dummy data

#About page
@app.route("/about") 
def about():
    return render_template('about.html', title = 'About')

#Register Page
@app.route("/register", methods = ['GET', 'POST']) 
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit(): #
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Account Created! Login Now!!','success') # send flash message ('success' is a bootstrap class)
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form = form)

#login Page
@app.route("/login", methods = ['GET', 'POST']) 
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit(): #send flash message
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): #compares password from db to password passed into the form
            login_user(user, remember = form.remember.data)#login using flask_login extension
            next_page = request.args.get('next')
            return redirect(next_page) if next_page  else redirect(url_for('home')) # Turnary conditional - redirect to next page if it exists - if not return home
        else:
            flash('Login Unsuccessful - Please Check Username and Password', 'danger') # danger is a bootstrap class
    return render_template('login.html', title='Login', form = form)

#logout route - for use when user is logged in
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


#Save Profile Pic function
def save_pic(form_picture):
    random_hex = secrets.token_hex(8) #base of filename
    _, f_ext = os.path.splitext(form_picture.filename) # finds the filename and extension uploaded (separetly)so it is saved as same
    picture_fn = random_hex + f_ext
    picture_pa = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    
    output_pic_size = (125, 125) # resizing imgage before saving if pic uploaded is big - for efficency
    i = Image.open(form_picture)
    i.thumbnail = (output_pic_size)
    i.save(picture_pa)       #THIS CODE IS NOT WORKING FOR ME!!!!!!!!!!!!!!!!!!!!!!!

    return picture_fn


#Accounts route
@app.route("/account", methods = ['GET', 'POST'])
@login_required
def account():
     form = UpdateAccountForm()
     if form.validate_on_submit():
         if form.picture.data:
             picture_file = save_pic(form.picture.data)
             current_user.image_file = picture_file
             if form.picture.data:
                old_pic = current_user.image_file
                picture_file = save_pic(form.picture.data)
                current_user.image_file = picture_file
                if old_pic != 'default.jpg':
                    os.remove(os.path.join(app.root_path, 'static/profile_pics', old_pic)) # deletes old picture to save space (not default.jpg)
         current_user.username = form.username.data #Updates current users username
         current_user.email = form.email.data       #Updates current users email
         db.session.commit()
         flash ('Your Account has been Updated!!', 'success') 
         return redirect(url_for('account'))
     elif request.method == 'GET':                 # populates form with the curret username and password (befor update)
         form.username.data = current_user.username
         form.email.data = current_user.email
     image_file = url_for('static', filename = 'profile_pics/' + current_user.image_file)
     return render_template('account.html', title='Account', image_file=image_file, form=form)


#Posting on App - new post
@app.route("/post/new", methods = ['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data, content = form.content.data, author = current_user)
        db.session.add(post)
        db.session.commit()
        flash ('Your Post has been Created!!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form = form, legend = 'New Post')

#Posting on App - ID the posts
@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title = post.title, post = post)

# Update posts by ID
@app.route("/post/<int:post_id>/update", methods = ['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your Post has been updated', 'success')
        return redirect(url_for('post', post_id = post.id))
    elif request.method == 'GET':
        form.title.data = post.title #Changes title using legend
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form = form, legend = 'Update Post')

# Delete posts by ID
@app.route("/post/<int:post_id>/delete", methods = ['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your Post has been Deleted', 'success')
    return redirect(url_for('home'))

#Show all posts for a specific username
@app.route("/user/<string:username>") 
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page = page, per_page=3) #allows me to define how many posts per page - orders them from newest to oldest
    return render_template('user_posts.html', posts = posts, user=user) # posts variable within the template is equal to the dummy data

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender = 'noreply@demo.com', recipients = [user.email] )
    msg.body = f''' To Reset Your Password, Click On This Link:
{url_for('reset_token', token = token, _external=True)}

If you did not make this request please ignore and no changes will be made to your account
'''
    mail.send()

#Reset user password - page to enter email to request a password reste
@app.route("/reset_password", methods = ['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An Email has been send to reset you password', 'info')
        return redirect (url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)



#Reset user password with the active token
@app.route("/reset_password/<token>", methods = ['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an expired or invalid token', 'warning') #'warning' is a bootstrap class
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit(): #
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_pw
        db.session.commit()
        flash('Password has been updated!','success') # send flash message ('success' is a bootstrap class)
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
