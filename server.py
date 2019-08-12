from flask import Flask, render_template, request, redirect, session # added request

import random 

#secret key required for session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

# our index route will handle rendering our form
@app.route('/')
def index():

    if 'ranum' in session:
        pass
    else:
        session["ranum"]=random.randint(1, 100)
        session['num1']=999
    
    return render_template("index.html")
        
@app.route('/num', methods=['POST'])
def return_result():
    
    session['ranum']

    num1= request.form['num1']
    num1=int(num1)
    session['num1']=num1

    if(session["ranum"]==num1):
        session['result']="win"
    elif(num1>session["ranum"]):
        session['result']="tohigh"
    else:
        session['result']='tolow'

    return redirect('/')

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)  