from flask import Flask, jsonify

""" creating aan instance of flask"""
app = Flask(__name__)
'''activating a get method for the root page'''
@app.get("/")
def index():
    return  'hell0 gamers'

@app.get("/hello")
def sayHello():
    return jsonify({
        "say hi": 'whatsup guys'
    })