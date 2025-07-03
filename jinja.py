##Building url dynamically
##variable rule
##jinja 2 template engine
'''
jinja2 template engine basically read data drom the data source and show output in the html page side side'''

##integration of flask with html
from flask import Flask,render_template,request,redirect,url_for
'''It create the instance of the flask class 
which will be your WSGI(Web server gateway interface)

way to read data from data source
{{}} -->expression to print output on html
{%...%}-->for conditional statement,for loops
{#...#}-->this is for comments

 
'''

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


##variable rule
@app.route("/success/<int:score>")
def success(score):
    return "the marks you got is : " + str(score)


##building url dynamically
@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',results=res)

@app.route("/successres/<int:score>")
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    exp={'score':score,'result':res}

    return render_template('result1.html',results=exp)


##if conditon -->for sucess
@app.route("/successif/<int:score>")
def successif(score):
   
    return render_template('result.html',results=score)


##if failed
@app.route("/failed/<int:score>")
def fail(score):
   
    return render_template('result.html',results=score)

@app.route("/getresult",methods=['GET','POST'])
def get_result():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        math=float(request.form['math'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])

        total_score=(science+math+c+datascience)/4

        return redirect(url_for('successres',score=total_score ))

##giving the entery point to the WSGI APP
if __name__=="__main__":
    app.run(debug=True)
  