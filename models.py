from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#


class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = db.Column("genres", db.ARRAY(db.String()))
    website = db.Column(db.String(240))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='venue',
                            lazy=True, cascade="all, delete-orphan")

    def __init__(self, name, city, state, address, phone, image_link, facebook_link, genres, website, seeking_talent, seeking_description, shows):
        self.name = name
        self.city = city
        self.state = state
        self.address = address
        self.phone = phone
        self.image_link = image_link
        self.facebook_link = facebook_link
        self.genres = genres
        self.website = website
        self.seeking_talent = seeking_talent
        self.seeking_description = seeking_description
        self.shows = shows

    def __repr__(self):
        return f'Venue ID {self.id} : Venue Name: {self.name}'


class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = db.Column("genres", db.ARRAY(db.String()))
    website = db.Column(db.String(240))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='artist', lazy=True)

    def __init__(self, name, city, state, phone, image_link, facebook_link, genres, website, seeking_talent, seeking_description, shows):
        self.name = name
        self.city = city
        self.state = state
        self.phone = phone
        self.image_link = image_link
        self.facebook_link = facebook_link
        self.genres = genres
        self.website = website
        self.seeking_talent = seeking_talent
        self.seeking_description = seeking_description
        self.shows = shows

    def __repr__(self):
        return f'Artist ID {self.id} : Artist Name: {self.name}'


class Show(db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey(
        'venue.id', ondelete='CASCADE'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey(
        'artist.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __init__(self, venue_id, artist_id, start_time):
        self.venue_id = venue_id
        self.artist_id = artist_id
        self.start_time = start_time

    def __repr__(self):
        return f'Show ID {self.id}'
