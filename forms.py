from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email, Length, Optional, NumberRange

class ContactForm(FlaskForm):
    """Form for contact messages."""
    name = StringField('Nombre', validators=[
        DataRequired(message='El nombre es requerido'),
        Length(min=2, max=100, message='El nombre debe tener entre 2 y 100 caracteres')
    ])
    email = StringField('Email', validators=[
        DataRequired(message='El email es requerido'),
        Email(message='Ingrese un email válido')
    ])
    phone = StringField('Teléfono', validators=[
        Optional(),
        Length(min=10, max=20, message='El teléfono debe tener entre 10 y 20 caracteres')
    ])
    subject = StringField('Asunto', validators=[
        Optional(),
        Length(max=200, message='El asunto no puede exceder los 200 caracteres')
    ])
    message = TextAreaField('Mensaje', validators=[
        DataRequired(message='El mensaje es requerido'),
        Length(min=10, max=1000, message='El mensaje debe tener entre 10 y 1000 caracteres')
    ])

class EventForm(FlaskForm):
    """Form for creating and editing events."""
    title = StringField('Título', validators=[
        DataRequired(message='El título es requerido'),
        Length(max=200, message='El título no puede exceder los 200 caracteres')
    ])
    description = TextAreaField('Descripción', validators=[
        DataRequired(message='La descripción es requerida'),
        Length(max=1000, message='La descripción no puede exceder los 1000 caracteres')
    ])
    date = DateTimeField('Fecha', validators=[
        DataRequired(message='La fecha es requerida')
    ])
    location = StringField('Ubicación', validators=[
        Optional(),
        Length(max=200, message='La ubicación no puede exceder los 200 caracteres')
    ])

class WorkshopForm(FlaskForm):
    """Form for creating and editing workshops."""
    title = StringField('Título', validators=[
        DataRequired(message='El título es requerido'),
        Length(max=200, message='El título no puede exceder los 200 caracteres')
    ])
    description = TextAreaField('Descripción', validators=[
        DataRequired(message='La descripción es requerida'),
        Length(max=1000, message='La descripción no puede exceder los 1000 caracteres')
    ])
    instructor = StringField('Instructor', validators=[
        Optional(),
        Length(max=100, message='El nombre del instructor no puede exceder los 100 caracteres')
    ])
    date = DateTimeField('Fecha', validators=[
        DataRequired(message='La fecha es requerida')
    ])
    duration = StringField('Duración', validators=[
        Optional(),
        Length(max=50, message='La duración no puede exceder los 50 caracteres')
    ])
    price = FloatField('Precio', validators=[
        Optional(),
        NumberRange(min=0, message='El precio no puede ser negativo')
    ])
    capacity = IntegerField('Capacidad', validators=[
        Optional(),
        NumberRange(min=1, message='La capacidad debe ser al menos 1')
    ])

class RestaurantForm(FlaskForm):
    """Form for creating and editing restaurants."""
    name = StringField('Nombre', validators=[
        DataRequired(message='El nombre es requerido'),
        Length(max=100, message='El nombre no puede exceder los 100 caracteres')
    ])
    description = TextAreaField('Descripción', validators=[
        DataRequired(message='La descripción es requerida'),
        Length(max=1000, message='La descripción no puede exceder los 1000 caracteres')
    ])
    cuisine_type = StringField('Tipo de Cocina', validators=[
        Optional(),
        Length(max=100, message='El tipo de cocina no puede exceder los 100 caracteres')
    ])
    price_range = StringField('Rango de Precios', validators=[
        Optional(),
        Length(max=50, message='El rango de precios no puede exceder los 50 caracteres')
    ])
    opening_hours = StringField('Horario', validators=[
        Optional(),
        Length(max=200, message='El horario no puede exceder los 200 caracteres')
    ])

class ArtisanForm(FlaskForm):
    """Form for creating and editing artisans."""
    name = StringField('Nombre', validators=[
        DataRequired(message='El nombre es requerido'),
        Length(max=100, message='El nombre no puede exceder los 100 caracteres')
    ])
    description = TextAreaField('Descripción', validators=[
        DataRequired(message='La descripción es requerida'),
        Length(max=1000, message='La descripción no puede exceder los 1000 caracteres')
    ])
    craft_type = StringField('Tipo de Artesanía', validators=[
        Optional(),
        Length(max=100, message='El tipo de artesanía no puede exceder los 100 caracteres')
    ])
    location = StringField('Ubicación', validators=[
        Optional(),
        Length(max=200, message='La ubicación no puede exceder los 200 caracteres')
    ])

class CoworkingSpaceForm(FlaskForm):
    """Form for creating and editing coworking spaces."""
    name = StringField('Nombre', validators=[
        DataRequired(message='El nombre es requerido'),
        Length(max=100, message='El nombre no puede exceder los 100 caracteres')
    ])
    description = TextAreaField('Descripción', validators=[
        DataRequired(message='La descripción es requerida'),
        Length(max=1000, message='La descripción no puede exceder los 1000 caracteres')
    ])
    capacity = IntegerField('Capacidad', validators=[
        Optional(),
        NumberRange(min=1, message='La capacidad debe ser al menos 1')
    ])
    amenities = TextAreaField('Amenidades', validators=[
        Optional(),
        Length(max=1000, message='Las amenidades no pueden exceder los 1000 caracteres')
    ])
    price_per_hour = FloatField('Precio por Hora', validators=[
        Optional(),
        NumberRange(min=0, message='El precio por hora no puede ser negativo')
    ])
    price_per_day = FloatField('Precio por Día', validators=[
        Optional(),
        NumberRange(min=0, message='El precio por día no puede ser negativo')
    ])
    price_per_month = FloatField('Precio por Mes', validators=[
        Optional(),
        NumberRange(min=0, message='El precio por mes no puede ser negativo')
    ]) 