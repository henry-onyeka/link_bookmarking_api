from flask import Blueprint
'''auth should be the name . while the url prefix  should be the link to call up a particular function 
depending on the method assigned by the function'''
auth =Blueprint("auth",__name__, url_prefix="/api/v1/auth")

@auth.post("/signup")
def signup():
    return  "User Created"

@auth.get("/me")
def me():
    return {"User" : "Me myself"}

@auth.get("/login")
def login():
    return "logged in successfully"