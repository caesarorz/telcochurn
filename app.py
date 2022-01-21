from flask import Flask, render_template, request
import pandas as pd
from catboost import CatBoostClassifier


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'



list_prediction = ['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges', 'gender_Male', 'Partner_Yes', 'Dependents_Yes', 
'PhoneService_Yes', 'MultipleLines_No phone service', 'MultipleLines_Yes', 'InternetService_Fiber optic', 'InternetService_No', 
'OnlineSecurity_No internet service', 'OnlineSecurity_Yes', 'OnlineBackup_No internet service', 'OnlineBackup_Yes', 'DeviceProtection_No internet service', 
'DeviceProtection_Yes', 'TechSupport_No internet service', 'TechSupport_Yes', 'StreamingTV_No internet service', 'StreamingTV_Yes', 
'StreamingMovies_No internet service', 'StreamingMovies_Yes', 'Contract_One year', 'Contract_Two year', 'PaperlessBilling_Yes', 
'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check', 'Tenure Cohort_12-24 months', 
'Tenure Cohort_24-48 months', 'Tenure Cohort_Over 48 months']


def generate_data(data):
    thedict = {}
    for i,j in zip(list_prediction, data):
        thedict[i] = j
    return thedict


def process_data(data):
    prediction = [0]*len(list_prediction)
    for i, j in data.items():
        for x in list_prediction:
            if i.lower() in x.lower():
                if j == x:
                    theindex = list_prediction.index(j)
                    prediction[theindex] = 1
                if j.isnumeric():
                    if 'tenure' in i:
                        theindex = list_prediction.index('tenure')
                        prediction[theindex] = j
                        if int(j) >= 12 and int(j) < 24:
                            theindex = list_prediction.index('Tenure Cohort_12-24 months')
                            prediction[theindex] = 1
                            
                        elif int(j) >= 24 and int(j) < 48:
                            theindex = list_prediction.index('Tenure Cohort_24-48 months')
                            prediction[theindex] = 1
                            
                        elif int(j) >= 48:
                            theindex = list_prediction.index('Tenure Cohort_Over 48 months')
                            prediction[theindex] = 1     
                    else:
                        theindex = list_prediction.index(i)
                        prediction[theindex] = j
                        
    return prediction




@app.route('/', methods=['get', 'post'])
def index():
    clf2 = CatBoostClassifier()
    clf2.load_model(fname="catboost.model", format="cbm")
    
    prediction = []
    if request.method == 'POST':
        prediction = process_data(request.form)
        show_results = generate_data(prediction)
        prediction = clf2.predict(prediction)
        return render_template('index.html', prediction=prediction, results=show_results)
    return render_template('index.html')



if __name__ == '__main__':
    app.run()