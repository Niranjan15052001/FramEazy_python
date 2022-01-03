from flask import Flask,render_template,request,redirect,session,Response
from flask.helpers import url_for
import numpy as np
import pickle
app=Flask(__name__)
@app.route('/',methods = ['POST',"GET"])
def home():
    if request.method=="POST":
        n=float(request.form["ni"])
        p=float(request.form["p"])
        k=float(request.form["k"])
        ph=float(request.form["ph"])
        humidity=float(request.form["humidity"])
        temp=float(request.form["temp"])
        rainfall=float(request.form["rainfall"])
        crop=restiremodel(n,p,k,temp,humidity,ph,rainfall)
        return Response("You are recommended to grow "+ crop)





        #return 
    
    
    return render_template('home.html')



    return render_template('home.html')  
@app.route("/debug",methods=['POST','GET'])
def debug():
    
    text = request.form["Sample"]
    k=text.split(" ")
    print(k)

    #print(text)
    return "received"
@app.route("/model",methods=['POST','GET'])
def model(request):
    
    text = request.form["data"]
    ##print(k)

    print(text)
    return "received"


def restiremodel(n,p,k,temp,humid,ph,rain):
    std= pickle.load(open('stdscaler.pkl', 'rb'))
    a=np.array([[n,p,k,temp,humid,ph,rain]])
    a=std.transform(a)
    model=pickle.load(open('votingclassfier.pkl', 'rb'))
    predict=model.predict(a)
    encode=pickle.load(open('Crop_label_encoder.pkl', 'rb'))
    crop=encode.inverse_transform(predict)
    print(crop)
    return crop[0]
if __name__=='__main__':
    app.run(host='192.168.43.181' , port=5050,debug=True)

