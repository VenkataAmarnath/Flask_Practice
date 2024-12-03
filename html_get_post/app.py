# htpp verbs

# GET, POST, PUT, DELETE

from flask import Flask, render_template,request

app=Flask(__name__)

@app.route("/")
def home():
    return "Home Page of Flask app"


# second param is methods, by default methods value is 'GET'
@app.route("/index",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/about",methods=['GET'])
def about():
    return render_template("about.html")



@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name1=request.form['Name']
        return f"Hello {name1} !!!!"
       
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)