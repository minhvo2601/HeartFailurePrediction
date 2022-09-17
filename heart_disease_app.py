import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))  #loading the model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods =['POST'])
def predict():
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    # Predict features
    prediction = model.predict(array_features)

    output = prediction

    if output == 0:
        return render_template('index.html', 
                               result = 'The patient is not likely to have heart disease!')
    else:
        return render_template('index.html', 
                               result = 'The patient is likely to have heart disease!')

if __name__ == "__main__":
    app.run()