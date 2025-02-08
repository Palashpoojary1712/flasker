from flask import Flask,render_template
app= Flask(__name__)

#create a route decorator
@app.route('/')
#def index():
 #  return "<h1>hello world</h1>"
  
def index():
    first_name="palash"
    stuff="this is a  <strong> bold </strong>  text"
    pizza=['olives','bread','cheese','tomato']
    return render_template("index.html",first_name=first_name, stuff=stuff,pizza=pizza )
   
#localhost:5000/user/palash'''
#@app.route('/user/<name>')
#def user(name):
 #  return "<h1> hello {}</h1>".format(name)
#ef user(name):
    return render_template("user.html",user_name=name)

#invalid url  
 
@app.errorhandler(404)
def not_found_error(e):  # Changed function name to avoid conflict
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_error(e):  # Changed function name to be more descriptive
    return render_template("500.html"), 500
