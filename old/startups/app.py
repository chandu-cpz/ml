from flask import Flask,render_template,request
import pickle
app=Flask(__name__)
import numpy as np
model=pickle.load(open("startup.pkl",'rb'))

@app.route('/')
def start():
    return render_template('index.html')


@app.route('/login',methods=['POST'])
def login():
  p=request.form['rd']
  q=request.form['as']
  r=request.form['ms']
  s=request.form['s']
  if(s=='cal'):
    s=0
  elif (s=='flo'):
     s=1
  else:
     s=2
  t=[[float(p),float(q),float(r),float(s)]]
  output=model.predict(t)

  return render_template("index.html",y="The Preicted Profit is "+str(output[0]))

if __name__=='__main__':
  app.run(debug=True)
