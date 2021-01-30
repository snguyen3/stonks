from flask import Flask, render_template, request, redirect
import random
import time

app = Flask(__name__, template_folder=".", static_folder=".")

@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def dashboard():
    data = {}
    for i,t in enumerate(['NASDAQ','GME','BTC','DOGE']):
        data[t] = {}
        data[t]['prices'] = [(time.time()-random.randint(0,10), random.uniform(1,100)) for i in range(50)]
        data[t]['sentiments'] = [(time.time()-random.randint(0,10), random.uniform(-1, 1)) for i in range(50)]

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
