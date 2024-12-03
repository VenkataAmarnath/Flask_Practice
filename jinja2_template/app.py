# Building url dynamically
# variable ruls
#Jinja2 template engine

###Jinja 2 template Engine
"""
There are multiple ways to read datasource from backend in html page

{{  }} expressions to print output in html
{%...%} conditional statements , for loops and all (ex: when reading dict)
{# .....#} for comments


"""

from flask import Flask, render_template,request,redirect,url_for

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

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name1=request.form['Name']
        return f"Hello {name1} !!!!"
       
    return render_template('form.html')

#variable rule
@app.route("/success/<score>")  #http://127.0.0.1:5000/success/51
def success(score):
    return "The marks is "+score

#variable rule
@app.route("/successint/<int:score>")  #http://127.0.0.1:5000/successint/51
def successint(score):
    #return "The marks is"+score # can only concatinate and return a string
    return "The marks is int"+str(score)

@app.route("/builddynamicurl/<int:score>")
def builddynamicurl(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="Fail"
    # return this res to result.html
    return render_template("result.html",result=res)


@app.route("/builddynamicurl2/<int:score>")
def builddynamicurl2for(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="Fail"
        exp={'score':score,"result":res}
    # return this res to result.html
    return render_template("result2.html",result=exp)


@app.route("/builddynamicurl3if/<int:score>")
def builddynamicurl3if(score):
    return render_template("result3.html",result=score)

@app.route('/fail/<int:score>')
def fail(score):


    return render_template('fail.html',result=score)

if __name__=="__main__":
    app.run(debug=True)