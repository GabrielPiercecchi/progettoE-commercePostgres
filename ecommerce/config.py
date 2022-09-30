import os

APP_ENV = os.getenv('APP_ENV', 'development')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'gabriel')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'StrongPassword')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'postgres')
TEST_DATABASE_NAME = os.getenv('DATABASE_NAME', 'postgres@localhost')

