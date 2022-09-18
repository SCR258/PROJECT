import numpy as np
import pickle

class icp():
    def __init__(self,data):
        self.data = data

    def load_model(self):
        with open('savemodel.sav','rb') as file:

             self.model= pickle.load(file)     




    def predict(self):

        self.load_model()
        
        sepal_length=float(self.data['sepal_length'])
        sepal_width=float(self.data['sepal_width'])
        petal_length=float(self.data['petal_length'])
        petal_width=float(self.data['petal_width'])
        
        array = np.array([[sepal_length,sepal_width,petal_length,petal_width]])  
       
        print(array)
        print("*"*50)
        
        result= self.model.predict(array)
        

        if result == 0:
            spacies="Iris - Setosa"
        if result == 1:
            spacies="Iris - Veriscolor"
        if result== 2:
            spacies="Iris - Virgininca"

       
        
        return spacies