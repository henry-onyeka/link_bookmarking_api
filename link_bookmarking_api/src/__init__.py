from flask import Flask, jsonify
import os

""" creating aan instance of flask"""
def  create_app(test_config= None):
    """a function to set up our app,
    create some config 
    and return it to us
    """
    app = Flask(__name__,instance_relative_config=True)
    if test_config is None:
        
        app.config.from_mapping(SECRETE_KEY=os.environ.get"SECRETE_KEY",
                                )
    else:
         app.config.from_mapping(test_config)
    @app.get("/")
    def index():
        return  'hell0 gamers'

    @app.get("/hello")
    def sayHello():
        return jsonify({
        "say hi": 'whatsup guys'
    })
    return app   
  


    if __name__ == '__main__':
        app.run(port=8000)  # Runs the app on port 8000