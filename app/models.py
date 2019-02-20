class User(UserMixin,db.Model):
    __tablename__ = 'users'
    Cleaning= db.relationship("Cleaning", backref="user", lazy="dynamic")
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
class Emplo(db.Model):
    '''
    comment class that create instance of comment
    '''
    __tablename__ = 'comment'

    #add columns
    id = db.Column(db. Integer, primary_key=True)
    comment_name = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    cleaning_id = db.Column(db.Integer, db.ForeignKey("cleaning.id"))

    def save_comment(self):
        '''
        save the comment per blog
        '''
        db.session.add(self)
        db.session.commit()
