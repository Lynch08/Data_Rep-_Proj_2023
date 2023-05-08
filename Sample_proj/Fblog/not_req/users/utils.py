#
#
##Save Profile Pic function
#def save_pic(form_picture):
#    random_hex = secrets.token_hex(8) #base of filename
#    _, f_ext = os.path.splitext(form_picture.filename) # finds the filename and extension uploaded (separetly)so it is saved as same
#    picture_fn = random_hex + f_ext
#    picture_pa = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
#    
#    output_pic_size = (125, 125) # resizing imgage before saving if pic uploaded is big - for efficency
#    i = Image.open(form_picture)
#    i.thumbnail = (output_pic_size)
#    i.save(picture_pa)       #THIS CODE IS NOT WORKING FOR ME!!!!!!!!!!!!!!!!!!!!!!!
#
#    return picture_fn
#
#
#def send_reset_email(user):
#    token = user.get_reset_token()
#    msg = Message('Password Reset Request', sender = 'noreply@demo.com', recipients = [user.email] )
#    msg.body = f''' To Reset Your Password, Click On This Link:
#{url_for('reset_token', token = token, _external=True)}
#
#If you did not make this request please ignore and no changes will be made to your account
#'''
#    mail.send(msg)