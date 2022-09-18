from flask import Flask,render_template, request
import pickle
import numpy as np

app= Flask(__name__)
#load the model
model=pickle.load(open('savemodel.sav','rb'))


@app.route('/')
def home():
    result= ''
    return render_template('index.html',**locals())

@app.route('/predict',methods=['POST','GET'])
def predict():

    '''if result[0] == 0:
        result = "Iris - Setosa"
        print("Iris - Setosa")
    if result[0] == 1:
        result = "Iris - Veriscolor"
        print("Iris - Versicolor")
    if result[0] == 2:
        result = "Iris - Virgininca"
        print("Iris - Virginica")'''


    sepal_length=float(request.form['sepal_length'])
    sepal_width=float(request.form['sepal_width'])
    petal_length=float(request.form['petal_length'])
    petal_width=float(request.form['petal_width'])
    result=model.predict([[sepal_length,sepal_width,petal_length,petal_width]])[0]
    return render_template('index.html',**locals())

   


if __name__=='__main__':
   app.run(debug=True) 