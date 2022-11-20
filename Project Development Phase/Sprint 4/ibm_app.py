from flask import Flask,render_template,request
app =Flask(__name__)

@app.route('/index') # slash is the url binding to render this page
def page_index():
   return render_template("index.html")

import pickle
model=pickle.load(open('model.pkl','rb'))

@app.route('/home') # slash is the url binding to render this page
def page():
   return render_template("home.html")
   
@app.route('/y_predict',methods=["GET/POST"])
def login():
        a=request.form('Temp')
        b=request.form('DO')
        c=request.form('PH')
        d=request.form('Conductivity')
        e=request.form('BOD')
        f=request.form('NI')
        g=request.form('Fec_col')
        h=request.form('Tot_col')
        
      t=[[float(a),float(b),float(c),float(d),float(e),float(f),float(g),float(h)]]
      
    Prediction = model.predict(t)
    if (Prediction==1):
        return render_template("home.html",y="The Water Quality is good and say for drink"+str(Prediction))
    else:
        return render_template("home.html",y="The Water Quality is bad and don't drink"+str(Prediction))
    
        
   
   
   
if __name__ =="__main__":
 app.run(debug= False)
