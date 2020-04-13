import pandas as pd
import numpy as np
import pickle as pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

app_metrics = pd.read_csv('AppleStore.csv')
app_description_data = pd.read_csv('appleStore_description.csv')
app_metrics['description'] = app_description_data['app_desc']

unique_genres = app_metrics['prime_genre'].unique()

app_metrics['size_mb'] = round(app_metrics['size_bytes'] / (1024*1024),1)
app_metrics['successful'] = np.where(app_metrics['rating_count_tot'] > 300, 1, 0)
app_metrics['app_is_free'] = np.where(app_metrics['price'] == 0,1,0)
app_metrics['length_of_title'] = app_metrics['track_name'].str.len()
app_metrics['length_of_description'] = app_metrics['description'].str.len()

def create_dummy_variables(dataframe, heading):
    unique_genres = dataframe[heading].unique()
    for x in unique_genres:
        dataframe[x] = np.where(dataframe[heading] == x, 1, 0)
    
create_dummy_variables(app_metrics, 'prime_genre')


# Create the model
selected_features = ['Games', 'Productivity', 'Weather', 'Shopping', 'Reference', 'Finance', 'Music',
 'Utilities', 'Travel', 'Social Networking', 'Sports', 'Business',
 'Health & Fitness', 'Entertainment', 'Photo & Video', 'Navigation',
 'Education', 'Lifestyle', 'Food & Drink', 'News', 'Book', 'Medical','Catalogs','length_of_title', 'length_of_description', 'app_is_free']

X = app_metrics[selected_features]
y = app_metrics['successful']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

app_success_model = LogisticRegression(max_iter=4000)
app_success_model.fit(X_train, y_train)

filename = 'app_success_model'
model = app_success_model

pickle.dump(model, open(filename, 'wb'))

