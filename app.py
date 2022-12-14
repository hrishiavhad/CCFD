from flask import Flask ,render_template , request
import pandas
import numpy 
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
app= Flask(__name__)
model=pickle.load(open('CCF_predict.pkl','rb'))

@app.route('/')

def home():
    result= ""
    return render_template('index.html',**locals())

@app.route('/predict',methods=['POST','GET'])
def predict():
    TIME =float(request.form['TIME'])
    V1 = float(request.form['V1'])
    V2 = float(request.form['V2'])
    V3 = float(request.form['V3'])
    V4 = float(request.form['V4'])
    V5 = float(request.form['V5'])
    V6 = float(request.form['V6'])
    V7 = float(request.form['V7'])
    V8 = float(request.form['V8'])
    V9 = float(request.form['V9'])
    V10= float(request.form['V10'])
    V11= float(request.form['V11'])
    V12= float(request.form['V12'])
    V13= float(request.form['V13'])
    V14= float(request.form['V14'])
    V15= float(request.form['V15'])
    V16= float(request.form['V16'])
    V17= float(request.form['V17'])
    V18= float(request.form['V18'])
    V19= float(request.form['V19'])
    V20= float(request.form['V20'])
    V21= float(request.form['V21'])
    V22= float(request.form['V22'])
    V23= float(request.form['V23'])
    V24= float(request.form['V24'])
    V25= float(request.form['V25'])
    V26= float(request.form['V26'])
    V27= float(request.form['V27'])
    V28= float(request.form['V28'])
    Amount= float(request.form['Amount'])

    result =model.predict([[TIME,V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,
                                                    V21,V22,V23,V24,V25,V26,V27,V28,Amount]])[0]
    
    if  result ==0:
        return('normal transition')
    else:
        return('froud transition')                                                  
                                            
    return render_template('index.html',**locals())

  

if __name__=="__main__":
     app.run(host='0.0.0.0',port=2000)
    
