from flask import Flask,render_template, request,jsonify
import pickle

from artifacts.utils import icp
app= Flask(__name__)




@app.route('/')
def home():
    result= ' '
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    data=request.form
    icp_obj=icp(data)
    rest=icp_obj.predict()

    return render_template('index.html',result=rest)


if __name__=='__main__':
   app.run(debug=True) 