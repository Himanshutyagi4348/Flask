from flask import Flask
'''It create the instance of the flask class 
which will be your WSGI(Web server gateway interface)'''

##initializing WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to my first app"

@app.route("/index")
def funct():
    return "this is the another route tyagi himanshu"

##giving the entery point to the WSGI APP
if __name__=="__main__":
    app.run(debug=True)
