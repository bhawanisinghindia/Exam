from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.output import *
from pywebio.input import *
import argparse
from pywebio import start_server 
app=Flask(__name__)

def exam():
    info = input_group("Espressif Systems Online Exam",
                   [input('Name  ', name='name'),
                    input('ID NO. ',name='id'),
                    input('Age ', name='age', type=NUMBER),
                   actions('Start Exam', ['YES'],name='confirm')])

    q1 = radio("What is full form of VLSI ?",["Very Large Scale Integration","land pata nahi"])
    q2 = radio("What is electronics ?",["Analog","digital","land pata nahi"])
    q3 = radio("What is semi-conductor ?",["Conductor of a bus","conductor which is cut into half","land pata nahi"])
    q4 = radio("Who is Best",["Sonu","Arora"])

    c = 0
    if q1 == "Very Large Scale Integration":
        c+=1

    if q2 == "land pata nahi":
        c+=1

    if q3 == "land pata nahi":
        c+=1

    if q4 == "Sonu":
        c+=1
        put_text("Your Score is "+str(c))
        put_markdown("""# you are selected""")
        

    if q4 == "Arora":
        put_markdown("""# Gaand maara...""")

app.add_url_rule('/tool', 'webio_view', webio_view(exam), methods=['GET','POST','OPTIONS'])

if __name__=='__exam__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--port",type=int,default=8080)
    args = parser.parse_args()
    
    start_server(exam,port=args.port)