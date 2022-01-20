from crypt import methods
from flask import Flask, render_template, request, jsonify
import joblib as job
import pandas as pd

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/', methods=['get'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['post'])
def predict():
    if request.method == 'POST':
        gender = request.form.getlist('gender') # 
        senior = request.form.getlist('senior') # 
        partner = request.form.getlist('partner') # 
        phone = request.form.getlist('phone') # 
        multilines = request.form.getlist('multilines') # XX 
        internetservice = request.form.getlist('internetservice') # XX 
        security = request.form.getlist('security') # XX 
        backup = request.form.getlist('backup')           # XX 
        protection = request.form.getlist('protection') # XX 
        support = request.form.getlist('support') # XX 
        streamingtv = request.form.getlist('streamingtv')
        streamingmovies = request.form.getlist('streamingmovies')
        contract = request.form.getlist('contract')
        billing = request.form.getlist('billing')
        payment = request.form.getlist('payment')

        totalcharges = request.form.get("totalcharges") # 
        print(totalcharges)

        montlycharges = request.form.get("tenure") # 
        print(montlycharges)

        tenure = request.form.get("montlycharges") # 
        print(tenure)

        print(gender, senior, partner, phone, multilines,
        internetservice)
        print(security, backup, protection, support, streamingtv)
        print(streamingmovies, contract, billing, payment)
        



if __name__ == '__main__':
    app.run(debug=True)