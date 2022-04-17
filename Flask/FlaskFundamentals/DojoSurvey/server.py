from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '' # set a secret key for security purposes
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("index_result.html", name = session['name'], location= session['location'], language = session['language'], comments = session['comments'])
if __name__ == "__main__":
    app.run(debug=True)