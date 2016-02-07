"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):

    __tablename__ = "models"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    year = db.Column(db.Integer,
                     nullable=False)
    brand_name = db.Column(db.String(50),
                           db.ForeignKey('brands.name'))
    # I'm not completely happy with this, since 'name'
    # is not the primary key in the brands table, but
    # brand_id does not exist in the models table.

    name = db.Column(db.String(50),
                     nullable=False)

    brand = db.relationship('Brand', backref='models')

    def __repr__(self):
        """Show info about models."""

        return "<Model id=%s brand = %s name = %s>" % (
            self.id, self.brand_name, self.name)


class Brand(db.Model):

    __tablename__ = "brands"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    founded = db.Column(db.Integer)
    headquarters = db.Column(db.String(50))
    discontinued = db.Column(db.Integer)

    def __repr__(self):
        """Show info about brands."""

        return "<Brand id=%s, name = %s>" % (
            self.id, self.name)

# End Part 1
##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
