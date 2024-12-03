from flask import Flask,render_template

app=Flask(__name__)


@app.route("/")
def home():
    return "<html><H1>Welcom to Flask with HTML integration course</H1></html>"
# best practise is to redirect to html page rather than writing all html code here itself, for that we use render_template

# render_templete responsible for redirecting to a html page
# create templates folder and place ur html pages in it
@app.route("/html_page")
def html_page():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template("about.html")


if __name__=="__main__":
    app.run(debug=True)