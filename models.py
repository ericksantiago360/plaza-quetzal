from datetime import datetime
from app import db

class ContactMessage(db.Model):
    """Model for contact form messages."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20))
    subject = db.Column(db.String(200))
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<ContactMessage {self.name}>'

class Event(db.Model):
    """Model for cultural events."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200))
    image_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Event {self.title}>'

class Workshop(db.Model):
    """Model for workshops and classes."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    instructor = db.Column(db.String(100))
    date = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.String(50))
    price = db.Column(db.Float)
    capacity = db.Column(db.Integer)
    image_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Workshop {self.title}>'

class Restaurant(db.Model):
    """Model for restaurants in the gastronomic area."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    cuisine_type = db.Column(db.String(100))
    price_range = db.Column(db.String(50))
    opening_hours = db.Column(db.String(200))
    image_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Restaurant {self.name}>'

class Artisan(db.Model):
    """Model for artisans in the crafts market."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    craft_type = db.Column(db.String(100))
    location = db.Column(db.String(200))
    image_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Artisan {self.name}>'

class CoworkingSpace(db.Model):
    """Model for coworking spaces."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    capacity = db.Column(db.Integer)
    amenities = db.Column(db.Text)
    price_per_hour = db.Column(db.Float)
    price_per_day = db.Column(db.Float)
    price_per_month = db.Column(db.Float)
    image_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<CoworkingSpace {self.name}>' 