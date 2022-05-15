from flask import Flask, render_template, redirect, url_for, session, request
# from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager
# from flask_uploads import UploadSet, configure_uploads, IMAGES
# install Flask-WTF
# from SignIn import signIn
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# photos = UploadSet('photos', IMAGES)

# app.config['UPLOADED_PHOTOS_DEST'] = 'images'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['DEBUG'] = True
# app.config['SECRET_KEY'] = 'mysecret'
# #db.init_app(app)

# configure_uploads(app, photos)

#db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# manager = Manager(app)
# manager.add_command('db', MigrateCommand)


@app.route('/')
def profile():
    return render_template('AboutMe.html')


@app.route('/cert')
def cert():
    return render_template('certificates.html')


@app.route('/Mentors')
def Mentors():
    return render_template('Mentors.html')


@app.route('/admin')
def admin():
    return render_template('admin/index.html', admin=True)


@app.route('/admin/add')
def add():
    return render_template('admin/view.html', admin=True)


@app.route('/SignIn')
def signIn():
    #form = signIn()
    return render_template('admin/SignIn.html', signIn=True)


if __name__ == '__main__':
    app.run(debug=True)