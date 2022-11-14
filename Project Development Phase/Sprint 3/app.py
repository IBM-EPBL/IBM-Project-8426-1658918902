from flask import Flask, render_template, request

import pickle

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
    
    model = pickle.load(open('liver_analysis.pkl','rb'))
    
    prediction = model.predict(data)[0]
    
    if(prediction == 1):
        return render_template('chance.html')
    else:
        return render_template('noChance.html')
if __name__ == '__main__':
    app.run()

