from flask import Flask, render_template, request

import requests

app = Flask(__name__,template_folder='Template')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def index():
    return render_template('index.html')

@app.route('/data_predict', methods=['post','get'])
def predict(): 
    age = request.form['age'] 
    gender = request.form['gender'] 
    tb = request.form['tb'] 
    db = request.form['db'] 
    ap = request.form['ap'] 
    aa1 = request.form['aa1'] 
    aa2 = request.form['aa2'] 
    tp = request.form['tp'] 
    a  = request.form['a'] 
    agr = request.form['agr'] 
    data = [[float(age), float(gender), float(tb), float(db), float(ap), float(aa1), float(aa2), float(tp), float(a), float(agr)]]
    
    
    # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
    API_KEY = "qE7RzJiXiSjsqvpB7QIK0tDhwAuCqCj79qRL7OZTKO53" 
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": 
    API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}) 
    mltoken = token_response.json()["access_token"] 
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken} 
    # NOTE: manually define and pass the array(s) of values to be scored in the next line 
    payload_scoring = {"input_data": [{"values": data}]} 
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/54ff6f58-4f38-462a-97b7-775c94fc8895/predictions?version=2022-11-13', json=payload_scoring, 
    headers={'Authorization': 'Bearer ' + mltoken}) 
    print("Scoring End Point") 
    print(response_scoring.json())
    pred = response_scoring.json()
    
    prediction = pred['predictions'][0]['values'][0][0]
    print(prediction)
    
    if(prediction == 1):
        return render_template('chance.html')
    else:
        return render_template('noChance.html')

if __name__ == '__main__':
    app.run()

