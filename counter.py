from flask import Flask, render_template, redirect, session,request 
app=Flask(__name__)
app.secret_key='it is a secret'

@app.route('/')
def homepage():
    session['visit_times']+=1
    return render_template('counter.html',times=session['visit_times'])
@app.route('/process', methods=['POST'])
def countTwoTimes():
    print('*'*50)
    print('two time')
    session['visit_times']+=1
    return redirect('/')
@app.route('/reset',methods=['POST'])
def reset():
    print('*'*50)
    print('reset')
    session['visit_times']=0
    return redirect('/')
if __name__=='__main__':
    app.run(debug=True)