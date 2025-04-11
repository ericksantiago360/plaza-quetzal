import pytest
from app import create_app, db

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app('testing')
    
    # Create the database and load test data
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()

def test_home_page(client):
    """Test that the home page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Plaza Comercial Quetzal' in response.data

def test_about_page(client):
    """Test that the about page loads successfully."""
    response = client.get('/about')
    assert response.status_code == 200
    assert b'Sobre Nosotros' in response.data

def test_services_page(client):
    """Test that the services page loads successfully."""
    response = client.get('/services')
    assert response.status_code == 200
    assert b'Servicios' in response.data

def test_contact_page(client):
    """Test that the contact page loads successfully."""
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'Contacto' in response.data

def test_coworking_page(client):
    """Test that the coworking page loads successfully."""
    response = client.get('/coworking')
    assert response.status_code == 200
    assert b'Coworking' in response.data

def test_gastronomia_page(client):
    """Test that the gastronomy page loads successfully."""
    response = client.get('/gastronomia')
    assert response.status_code == 200
    assert b'Gastronomia' in response.data

def test_artesanias_page(client):
    """Test that the crafts page loads successfully."""
    response = client.get('/artesanias')
    assert response.status_code == 200
    assert b'Artesanias' in response.data 