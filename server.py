from flask import Flask
import pickle as pickle

app = Flask(__name__)
filename = 'app_success_model'
loaded_model = pickle.load(open(filename, 'rb'))

@app.route('/good')
def good_example_func():
    good_example = [[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,50,4990,0]]
    bad_example = [[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,50,499,0]]
    prediction = loaded_model.predict(good_example)[0]
    if prediction == 0:
        return "I predict a failure"
    elif prediction == 1:
        return "I predict success"
@app.route('/bad')
def bad_example_func():
    good_example = [[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,50,4990,0]]
    bad_example = [[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,50,499,0]]
    prediction = loaded_model.predict(bad_example)[0]
    if prediction == 0:
        return "I predict a failure"
    elif prediction == 1:
        return "I predict success"
