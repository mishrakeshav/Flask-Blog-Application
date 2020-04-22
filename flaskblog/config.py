import os

class Config:
    SECRET_KEY = "fb40965f2a290c9e3cf71459eb611fe5"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ''
