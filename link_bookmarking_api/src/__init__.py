from flask import Flask, jsonify
import os
from src.auth import auth
from src.bookmarks import bookmarks

""" creating aan instance of flask"""
def  create_app(test_config= None):
    """a function to set up our app,
    create some config 
    and return it to us
    """
    app = Flask(__name__,instance_relative_config=True)
    if test_config is None:
        
        app.config.from_mapping(SECRETE_KEY=os.environ.get("SECRETE_KEY"),
                                )
    else:
        app.config.from_mapping(test_config)
        '''register the auth and bookmarks method to enable it for lookup'''

    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)

    return app   
  