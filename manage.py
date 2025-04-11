#!/usr/bin/env python
import os
from flask import Flask
from flask.cli import FlaskGroup
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    return app

cli = FlaskGroup(create_app=create_app)

@cli.command('init-db')
def init_db():
    """Initialize the database."""
    from app import db
    db.create_all()
    print('Database initialized.')

@cli.command('run-tests')
def run_tests():
    """Run the tests."""
    import pytest
    pytest.main(['tests'])

if __name__ == '__main__':
    cli() 