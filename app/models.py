from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    blogs = db.relationship("Blog", backref="user", lazy="dynamic")
    comment = db.relationship("Comments", backref="user", lazy ="dynamic")



    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    def __repr__(self):
        return f'User {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

class contact(db.Model):
    '''
    defines the table instance of our contact table
    '''
    __tablename__= 'contact'

    id = db.Column(db.Integer, primary_key=True)
    Blog_post = db.Column(db.String)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_contact(self):
        '''
        function to save blog
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_contacts(cls):
        '''
        function that clears all the contacts in the form after submission
        '''
        user.all_contacts.clear()

    @classmethod
    def get_users(cls,id):
        '''
        function that gets particular users when requested by date application
        '''
        contacts = Contact.query.order_by(Contact.date_posted.desc()).all()
        return contacts

class worker(db.Model):
    '''
    worker class that create instance of worker
    '''
    __tablename__ = 'worker'

    #add columns
    id = db.Column(db. Integer, primary_key=True)
    worker_name = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    worker_id = db.Column(db.Integer, db.ForeignKey("worker.id"))
