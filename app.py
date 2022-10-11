from tensorflow.keras.models import load_model

import numpy as np

from random import randint
from sklearn.preprocessing import MinMaxScaler
model = load_model('medical_trial_model.h5')

from flask import Flask,render_template,request

app = Flask(__name__)

app.run(debug=True)

@app.route('/')
@app.route('/register')
def home():
	return render_template('register.html')

@app.route('/register',methods=["POST","GET"])
def register():
	if request.method == 'POST':
		user = request.form.get('fname')
		
		# ---------------------------------
		age = int(user)

		ages = [0,30,60,age,90]
		ages = np.array(ages)

		scaler = MinMaxScaler(feature_range=(0,1))
		scaled_age = scaler.fit_transform(ages.reshape(-1,1))

		prediction = model.predict(x=scaled_age)
		rounded_prediction = np.argmax(prediction,axis=-1)
		health_status = {0:"No Side Effects",1:"Possible to have Side Effects"}

		output = health_status[int(rounded_prediction[3])]
		
		# ----------------------------------------------------------------

		return render_template('register.html',useroutput=output)
