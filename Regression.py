'''
Scikit-learn library is focused on modeling the data.
We will use Supervised Learning algorithms − particularly  Linear Regression
for modeling of data
For installing: pip install -U scikit-learn

REFERENCES:
https://heartbeat.fritz.ai/implementing-multiple-linear-regression-using-sklea  rn-43b3d3f2fe8b
https://datatofish.com/multiple-linear-regression-python/
https://www.w3schools.com/python/python_ml_multiple_regression.asp
https://towardsdatascience.com/simple-and-multiple-linear-regression-in-python-c928425168f9
https://medium.com/pursuitnotes/multiple-linear-regression-model-in-7-steps-with-python-c6f40c0a527

TRAIN-TEST MODEL (70-30)
Mean Actual Error - predict error of predictions and actuals (ACCURACY MEASURE)
To compare predictions with actual values : ROOT MEAN SQUARE ERROR

'''
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error


def getCSV (filename):
    global df
    
    print('Reading Data.....',filename)
    
    d = pd.read_csv (filename)
    df=d
    print('*'*75)
    print("File Retrieved Sucessfully!!!!")
    print('*'*75)
    
def TrainTestModel(linreg):
    #global linreg    
    #Separate the features and label
    x=df[['Temperature','Humidity']]
    y=df[['Rainfall']]

    ##########################################
    #                         TRAIN TEST MODEL
    ##########################################

    print('*'*75)
    print('\t\t\tTRAIN TEST EXAMPLE: ')
    print('*'*75)
    #Split the data set into train set and split set
    x_train,x_test, y_train,y_test = train_test_split(x,y,test_size=0.33,random_state=42)
    
    #print('Before fit : \n', x_train, '\n and \n',y_train)
    #Fit the model to the training data
    model =linreg.fit(x_train,y_train)
    #Predict
    y_pred=linreg.predict(x_test)
    #print('Y PREDICTION : ')
    #print(y_pred)

    #Score
    print('SCORE: ',linreg.score(x_test,y_test))
          
    #Calculate mean absolute error
    mae=mean_absolute_error(y_test,y_pred)
    print('MAE : ',mae)

    #Calculate mean squared error
    mse=mean_squared_error(y_test,y_pred)
    rmse=np.sqrt(mse)
    print('RSME : ',rmse)

    return model



    
