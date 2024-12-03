from flask import Flask, render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return "Home Page of Flask app"


@app.route('/successres/<int:score>')
def successres(score):
    res=''
    if score>=50:
        res='Passed'
    else:
        res='Failed'
    exp={'score':score, 'res':res}

    return render_template('result2.html',results=exp)

@app.route('/submit',methods=['GET','POST'])
def submit():
    total=0
    avg=0
    if request.method=="POST":
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total=science+maths+c+data_science

        avg=total/4
        

    else:
        return render_template('getresult.html')

        #wanna redirect to someother route after i click submit
    return redirect(url_for('successres',score=avg))

if __name__=="__main__":
    app.run(debug=True)