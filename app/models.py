from . import db
from werkzeug.security import generate_password_hash


class Property (db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text())
    rooms = db.Column(db.String(10))
    bathrooms = db.Column(db.String(10))
    price = db.Column(db.String(50))
    ptype = db.Column(db.String(80))
    location = db.Column(db.String(300))
    photo = db.Column(db.String(300))

    def __init__(self, title, description,rooms,bathrooms,price,ptype,location,photo):
        self.title = title
        self.description=description
        self.rooms=rooms
        self.bathrooms=bathrooms
        self.price=price
        self.ptype=ptype
        self.location=location
        self.photo=photo


     
    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property  %r>' % (self.title)