from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "jackbauer"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['languages'] = request.form['languages']
    session['comment'] = request.form['comment']
    return redirect('/success')


@app.route('/success')
def success():
    return render_template("result.html")


if __name__=="__main__":
    app.run(debug=True)
