from flask import Flask,render_template,request,url_for,redirect
app=Flask(__name__)
@app.route('/')
def form():
    return render_template('form.html')

@app.route('/result/<int:score>')
def result(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('index.html',results=res,marks=score)

@app.route('/getres',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        math=float(request.form['math'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])
        
        total_score=(science+math+c+datascience)/4
    return redirect(url_for('result',score=total_score))
  
if __name__=="__main__":
    app.run()