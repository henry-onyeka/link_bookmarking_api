from flask import Blueprint
'''to acccess the bookmarks method'''
bookmarks =Blueprint("bookmarks",__name__, url_prefix="/api/v1/bookmarks")

@bookmarks.get("/")
def getall():
    return  {"bookmaarks":[]}