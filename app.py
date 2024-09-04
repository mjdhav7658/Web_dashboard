from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        file = request.files['file']
        if file:
            df = pd.read_excel(file)
            data = df.to_html(index=False, classes="table table-striped")
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
