from flask import Flask
from flask.templating import render_template
app = Flask(__name__)
@app.route('/')
def checkerBoard():
    return render_template('index.html')

@app.route('/4')
def checkerBoard4():
    return render_template('index4.html')

@app.route('/<int:x>/<int:y>')
def checkerBoardxy(x, y):
    # x = int(x)
    # y = int(y)
    return render_template('index_xy.html', x=x, y=y)

if __name__ == ("__main__"):
    app.run(debug=True)