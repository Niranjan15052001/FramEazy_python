from flask import Flask,render_template,request,redirect,session,Response
from flask.helpers import url_for
import numpy as np
import pickle
import wikipedia as w
from wikipedia.exceptions import WikipediaException
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
        t=list(n,p,k,temp,humidity,ph,rainfall)
        crop=restiremodel(t)
        return Response("You are recommended to grow "+ crop)





        #return 
    
    
    return render_template('home.html')



    return render_template('home.html')  
@app.route("/debug",methods=['POST','GET'])
def debug():
    
    text = request.form["Sample"]
    k=text.split(" ")
    lists=[]
    for i in range(len(k-1)):
        lists.append(float(k[i]))
    crop=restiremodel(lists)

    return Response(crop)
@app.route("/model",methods=['POST','GET'])
def model():
    
    text = request.form["data"]
    k=text.split(" ")
    print(k)

    #print(text)
    return "received"
@app.route('/wiki',methods=['POST','GET'])
def wiki():
    #data=request.form['data']
    #data=data.split(" ")
    #crop=data[0]
    #lang=data[1]
    crop="kidneybeans"
    lang="en"
    #w.set_lang(lang)
    res=w.summary(crop)
    final=""
    try:
        res_crop=w.summary(crop+' plant')
    except WikipediaException:
        res_crop=""
    final=res
    if res_crop:
        final=final+"\n"+res_crop
    return Response(final)

def restiremodel(data):
    std= pickle.load(open('stdscaler.pkl', 'rb'))
    a=np.array([data])
    a=std.transform(a)
    model=pickle.load(open('votingclassfier.pkl', 'rb'))
    predict=model.predict(a)
    encode=pickle.load(open('Crop_label_encoder.pkl', 'rb'))
    crop=encode.inverse_transform(predict)
    print(crop)
    return crop[0]

if __name__=='__main__':
    app.run(host='192.168.43.181' , port=5000,debug=True)

