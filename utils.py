import os
from datetime import datetime
from werkzeug.utils import secure_filename
from flask import current_app

def allowed_file(filename, allowed_extensions):
    """Check if the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def save_file(file, folder, allowed_extensions):
    """Save an uploaded file to the specified folder."""
    if file and allowed_file(file.filename, allowed_extensions):
        filename = secure_filename(file.filename)
        # Add timestamp to filename to prevent duplicates
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{timestamp}_{filename}"
        
        # Create folder if it doesn't exist
        upload_folder = os.path.join(current_app.static_folder, folder)
        os.makedirs(upload_folder, exist_ok=True)
        
        # Save file
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return filename
    return None

def format_currency(amount):
    """Format a number as currency."""
    return f"${amount:,.2f}"

def format_date(date):
    """Format a datetime object as a string."""
    return date.strftime('%d/%m/%Y %H:%M')

def get_pagination_info(page, per_page, total):
    """Calculate pagination information."""
    total_pages = (total + per_page - 1) // per_page
    has_prev = page > 1
    has_next = page < total_pages
    return {
        'current_page': page,
        'total_pages': total_pages,
        'has_prev': has_prev,
        'has_next': has_next,
        'prev_page': page - 1 if has_prev else None,
        'next_page': page + 1 if has_next else None,
        'total_items': total
    }

def send_email(subject, recipients, body):
    """Send an email using Flask-Mail."""
    from flask_mail import Message
    from app import mail
    
    msg = Message(
        subject=subject,
        recipients=recipients,
        body=body
    )
    mail.send(msg)

def validate_image_file(file):
    """Validate an image file."""
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return allowed_file(file.filename, allowed_extensions)

def get_file_extension(filename):
    """Get the file extension from a filename."""
    return filename.rsplit('.', 1)[1].lower() if '.' in filename else None

def generate_thumbnail(image_path, size=(200, 200)):
    """Generate a thumbnail from an image."""
    from PIL import Image
    
    try:
        with Image.open(image_path) as img:
            img.thumbnail(size)
            thumbnail_path = f"{image_path}_thumb.{get_file_extension(image_path)}"
            img.save(thumbnail_path)
            return thumbnail_path
    except Exception as e:
        current_app.logger.error(f"Error generating thumbnail: {str(e)}")
        return None 