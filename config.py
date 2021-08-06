import os

basedir = os.path.abspath(os.path.dirname(__file__))
# Windows - C:\Users\bstan\Documents\codingtemple-jun-2021\week6\day2\intro_to_flask_jun
# Mac - /home/bstanton/Document/codingtemple-jun-2021/week6/day2/intro_to_flask_jun

class Config:
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False