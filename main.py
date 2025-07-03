##integration of flask with html
from flask import Flask,render_template
'''It create the instance of the flask class 
which will be your WSGI(Web server gateway interface)'''

##initializing WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to flask cource</h1></html>"

@app.route("/index")
def funct():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')

##giving the entery point to the WSGI APP
if __name__=="__main__":
    app.run(debug=True)
