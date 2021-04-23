from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.output import *
from pywebio.input import *
import argparse
from pywebio import start_server 
app=Flask(__name__)

def main():
    info = input_group("HCL Online Exam for Machine Learning Engineer",
                   [input('Name  ', name='name'),
                    input('ID NO. ',name='id'),
                    input('Age ', name='age', type=NUMBER),
                   actions('Start Exam', ['YES'],name='confirm')])

    q1 = radio("Which of the following is a widely used and effective machine learning algorithm based on the idea of bagging?",
               ["Decision Tree","Regression","Classification","Random Forest"])
    q2 = radio("To find the minimum or the maximum of a function, we set the gradient to zero because:",
               ["The value of the gradient at extrema of a function is always zero","Depends on the type of problem","None of the above"])
    q3 = radio("Which of the following is a disadvantage of decision trees?",
               ["Factor analysis","Decision trees are robust to outliers","Decision trees are prone to be overfit","None of the above"])
    q4 = radio("When performing regression or classification, which of the following is the correct way to preprocess the data?",
               ["Normalize the data -> PCA -> training","PCA -> normalize PCA output -> training","Normalize the data -> PCA -> normalize PCA output -> training"])
    q5 = radio("Which of the following techniques can not be used for normalization in text mining?",
               ["Stemming","Lemmatization","Stop Word Removal","None of the above"])
    c = 0
    if q1 == "Random Forest":
        c+=1

    if q2 == "The value of the gradient at extrema of a function is always zero":
        c+=1

    if q3 == "Decision trees are prone to be overfit":
        c+=1

    if q4 == "Normalize the data -> PCA -> training":
        c+=1

    if q5 == "Stop Word Removal":
        c+=1        
    
    if c>3:
        put_markdown("""# you are passed""")
    
    if c<=3:
        put_markdown("""# you are failed""")
        
app.add_url_rule('/tool', 'webio_view', webio_view(main), methods=['GET','POST','OPTIONS'])


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--port",type=int,default=8080)
    args = parser.parse_args()
    
    start_server(main,port=args.port)
