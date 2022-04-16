from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '' # set a secret key for security purposes
@app.route('/')
def incrementOne():
    if 'counter' in session:
        print('key exists!')
        session['counter'] = int(session['counter']) + 1
    else:
        print("key 'key_name' does NOT exist")
        session['counter'] = 1
    session['counter_two'] = 1
    return redirect('/index')
    
    
@app.route('/increment_two')
def incrementTwo():
    if 'counter' in session:
        print('key exists!')
        session['counter'] = int(session['counter']) + 2
    else:
        print("key 'key_name' does NOT exist")
        session['counter'] = 2
    return redirect('/index')

@app.route('/click_two', methods=['POST'])
def clickTwo():
    if 'counter' in session:
        print('key exists!')
        session['counter'] = int(session['counter']) + 2
    else:
        print("key 'key_name' does NOT exist")
        session['counter'] = 2
    return redirect('/index')

@app.route('/click_reset', methods=['POST'])
def clickReset():
    session.clear()		# clears all keys
    return redirect('/')

@app.route('/set_increment', methods=['POST'])
def setIncrement():
    if 'counter_two' in session:
        print('key exists!')
        session['counter_two'] = int(session['counter_two']) + int(request.form['value'])
    else:
        print("key 'key_name' does NOT exist")
        session['counter_two'] = 0
    return redirect('/index')


@app.route('/destroy_session')
def destroySession():
    session.clear()		# clears all keys
    return redirect('/')

@app.route('/index')
def index():
    return render_template("index.html", counter = int(session['counter']), counter2 = int(session['counter_two']))

if __name__ == "__main__":
    app.run(debug=True)