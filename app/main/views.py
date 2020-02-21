from flask import render_template, request, redirect, url_for,abort
from . import main
# from .forms import UpdateFrofile,BlogForm
from app.models import User, Turfs
from flask_login import login_required, current_user
from .. import db
from ..email import mail_message

@main.route('/')
def index():
    '''
    view root page of the app which returns the homepage of thapp
    '''
    title = ''
    return render_template('index.html', title = title)

@main.route('/feedback/<blog_id>',methods=['GET','POST'])
def feedback(blog_id):
    blog = Blog.query.get(blog_id)
    feedback = request.form.get('newcomment')
    new_comment = Comment(feedback = feedback, user_id = current_user._get_current_object().id, blog_id=blog_id)
    new_comment.save_comment()
    return redirect(url_for('main.blog',id= blog.id))

@main.route('/profile',methods=['GET','POST'])
def profile():
    form = UpdateProfile()
    if form.validate_on_submit():
        if form.profile_pic.data:
            picture_file= save_pic(form.profile_pic.data)
            current_user.profile_pic_path = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash('Profile Updated Successfully')
        return redirect(url_for('main.profile'))
    elif request.method =='GET':        
        form.bio.data = current_user.bio
    profile_pic_path = url_for('static',filename='photos' + current_user.profile_pic_path)    
    return render_template('account.html',form=form)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@main.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateFrofile(FlaskForm):
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)