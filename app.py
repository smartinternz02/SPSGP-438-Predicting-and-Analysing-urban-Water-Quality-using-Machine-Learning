import numpy as np
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('water_pickle.pkl', 'rb'))
@app.route('/')

def home():
    return render_template("home.html")

@app.route('/login', methods=['POST'])
def login():
    year = request.form["year"]
    do = request.form["do"]
    ph = request.form["ph"]
    co = request.form["co"]
    bod = request.form["bod"]
    na = request.form["na"]
    tc = request.form["tc"]
    total = [[float(ph), float(do), float(bod), float(tc), float(na), float(co)]]
    y_pred = model.predict(total)
    y_pred = y_pred[[0]]
    y_pred1 = float(y_pred)
    y_pred = int(y_pred)
    if(y_pred >= 95 and y_pred<=100):
        return render_template("home.html", showcase="Excellent, the predicted value is: "+str(y_pred1))
    elif(y_pred >= 89 and y_pred<=94):
        return render_template("home.html", showcase="Very Good, the predicted value is: "+str(y_pred1))
    elif(y_pred >= 78 and y_pred<=88):
        return render_template("home.html", showcase="Good, the predicted value is: "+str(y_pred1))
    elif(y_pred >= 65 and y_pred<=79):
        return render_template("home.html", showcase="Fair, the predicted value is: "+str(y_pred1))
    elif(y_pred >= 45 and y_pred<=64):
        return render_template("home.html", showcase="Marginal, the predicted value is: "+str(y_pred1))
    else:
        return render_template("home.html", showcase="Poor, the predicted value is: "+str(y_pred1))

if __name__=='__main__':
    app.run(debug=True, port=5000)