from petfax import create_app
app = create_app()


# below commented out to be set up in a different file

# # config
# from flask import Flask # importing Flask
# app = Flask(__name__) #instance of Flask created and dunder variable name passed to it

# # index route
# @app.route('/')
# def index():
#     return 'Hello, this is PetFax'

# # pets index route
# @app.route('/pets')
# def pets():
#     return 'These are our pets available for adoption'

