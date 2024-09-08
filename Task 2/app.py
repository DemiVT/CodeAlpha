from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/examples')
def examples():
    return render_template('examples.html')

@app.route('/tips')
def tips():
    return render_template('tips.html')

@app.route('/reporting')
def reporting():
    return render_template('reporting.html')

if __name__ == "__main__":
    app.run(debug=True)
