from flask import Flask, render_template, request, redirect, session
import random
app= Flask (__name__)
app.secret_key = 'VeryVerySecret'

@app.route('/', methods = ['GET'])
def index():
    if 'number' not in session:
        session['number'] = random.randrange(0,101)
    return render_template('index.html')

@app.route('/action', methods = ['POST'])
def action():
    print(type(request.form['input']))
    if int(request.form['input']) == session['number']:
        session.clear()
        print('Correct!')
    elif int(request.form['input']) < session['number']:
        print('Too Low!') 
    elif int(request.form['input']) > session['number']:
        print('Too High!') 
    return redirect('/')





if __name__=='__main__':
    app.run(debug=True)