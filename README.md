### App to predict the success/failure of a mobile app idea

Using this Kaggle dataset: https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps

I ran initial analysis in model.ipynb and then deployed the model using pickle and a flask app in model.py and server.py

#### Setup instructions
* export FLASK_APP=server.py 
* flask run
* http://127.0.0.1:5000/good (example of good prediction)
* http://127.0.0.1:5000/bad (example of bad prediction)