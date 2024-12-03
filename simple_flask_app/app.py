from flask import Flask

# Initialising FLask app, 
# It creates an instance of flask class, it will be our WSGI application.

# __name__ nparameter cannot be skipped
app=Flask(__name__)

# Creating a basic route for home page of my flask app
# @app.route is decorator, first param is rule(in the form of string), we gave '/' here, it defines my home page
# as soon as I go to the route, it will call the function associated with the route as defined below.
@app.route('/')
def home():
    return "Welcome to Flask"

# creating another simple route 
@app.route("/index")
def index():
    return "Welcome to index page"

# This works as entry point to any .py file and execution starts from here
if __name__=="__main__":
    # Imp of debug = True: it makes app update parallelly if we update code while app is in running state.
    app.run(debug=True)
    # here local host is given, if we want to host it on any cloud we can give host as 0.0.0.0