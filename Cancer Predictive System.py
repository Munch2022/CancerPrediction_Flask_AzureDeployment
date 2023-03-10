# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

# loading the trained model; copy the path where u saved downloaded trained model
loaded_model= pickle.load(open('C:/Users\Manjula\Desktop/Deploying_ML_Model_new/trained_model.sav', 'rb')) 


input_data = (6, 4, 2, 3, 1, 2, 5, 2, 1)
input_data_arr= np.asarray(input_data)
inputdata_reshaped= input_data_arr.reshape(1, -1)               # coz it sontains sample(series of values)

prediction = loaded_model.predict(inputdata_reshaped)              # here instead of clf2, im giving the loaded_model as the clf2 model is saved in this variable
print(prediction)

if (prediction[0] == 2):
  print('Its a benign cancer. The patient is not diagnosed with Breast Cancer')
else:
  print('Its a malignant cancer, Consult doctor immediately. The patient is diagnosed with Breast Cancer')



# erlier this was link for saved model: 'C:/Users\Manjula\Desktop/Deploying_ML_model/trained_model.sav', 'rb'
# changed the path of saved model as created another folder for flask version 