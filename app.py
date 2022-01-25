from flask import Flask, render_template, request, jsonify
import pandas as pd
from catboost import CatBoostClassifier


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'



list_names = ['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges', 'gender_Male', 'Partner_Yes', 'Dependents_Yes', 
                    'PhoneService_Yes', 'MultipleLines_No phone service', 'MultipleLines_Yes', 'InternetService_Fiber optic', 'InternetService_No', 
                    'OnlineSecurity_No internet service', 'OnlineSecurity_Yes', 'OnlineBackup_No internet service', 'OnlineBackup_Yes', 'DeviceProtection_No internet service', 
                    'DeviceProtection_Yes', 'TechSupport_No internet service', 'TechSupport_Yes', 'StreamingTV_No internet service', 'StreamingTV_Yes', 
                    'StreamingMovies_No internet service', 'StreamingMovies_Yes', 'Contract_One year', 'Contract_Two year', 'PaperlessBilling_Yes', 
                    'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check', 'Tenure Cohort_12-24 months', 
                    'Tenure Cohort_24-48 months', 'Tenure Cohort_Over 48 months']


def process_data(data):
    """
    get the data from the client and transform information into
    a format that the catboost prediction can understand.

    input: data as a dictionary, list_names
    output: data in predict format (see format for prediction) 
    """
    prediction = [0]*len(list_names)
    for i, j in data.items():
        for x in list_names:
            if i.lower() in x.lower():
                if j == x:
                    theindex = list_names.index(j)
                    prediction[theindex] = 1
                if j.isnumeric():
                    if 'tenure' in i:
                        theindex = list_names.index('tenure')
                        prediction[theindex] = j
                        if int(j) >= 12 and int(j) < 24:
                            theindex = list_names.index('Tenure Cohort_12-24 months')
                            prediction[theindex] = 1
                            
                        elif int(j) >= 24 and int(j) < 48:
                            theindex = list_names.index('Tenure Cohort_24-48 months')
                            prediction[theindex] = 1
                            
                        elif int(j) >= 48:
                            theindex = list_names.index('Tenure Cohort_Over 48 months')
                            prediction[theindex] = 1     
                    else:
                        theindex = list_names.index(i)
                        prediction[theindex] = j 
    return prediction


@app.route('/', methods=['get'])
def index():
    return render_template('index.html')


@app.route('/prediction', methods=['post'])
def predict():
    prediction = []
    if request.method == 'POST':
        json_ = request.json
        clf2 = CatBoostClassifier()
        clf2.load_model(fname="catboost.model", format="cbm")
        prediction = process_data(json_)
        prediction = clf2.predict(prediction)
        return jsonify({'prediction': str(prediction)}), 200
    return jsonify({'message', 'Unknown error ocurred.'}), 500


if __name__ == '__main__':
    app.run(debug=True)