from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/dashboard', methods=['GET'])
def dashboard():
    data = []
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
