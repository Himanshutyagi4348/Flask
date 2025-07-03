##integration of flask with html
from flask import Flask,render_template,request
'''It create the instance of the flask class 
which will be your WSGI(Web server gateway interface)'''

##initializing WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Learning gets and post methods</h1></html>"

@app.route("/index",methods=['GET'])
def funct():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/submit",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name} !!!'
    return render_template('form.html')

##giving the entery point to the WSGI APP
if __name__=="__main__":
    app.run(debug=True)
