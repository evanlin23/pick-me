import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import requests

#working on restaurant reccomender here

#current overall project structure outlined here -- location code will be finalized, along
# with how we are pulling from google-form type survey on home page for users to provide data

# model definition
class RestaurantRecommendationModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        # input_size (int): size of the input features.
        # hidden_size (int): size of the hidden layer.
        # output_size (int): size of the output layer.
        super(RestaurantRecommendationModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()
        
    def forward(self, x):
        out = self.fc1(x)
        out = self.sigmoid(out)
        out = self.fc2(out)
        return out

# test parameters for user preferences -- fill in w/real data once user preference form is built
def get_user_preferences():
    cuisine = float(cuisine)
    price = float(price)
    atmosphere = float(atmosphere)
    
    return np.array([cuisine, price, atmosphere])

# i think float tensor would work for restaurant reccomendation
def recommend_restaurant(model, user_preferences):
    # convert user preferences to float tensor
    user_preferences_tensor = torch.FloatTensor(user_preferences)
    # ensure the model is in evaluation mode
    model.eval()
    # disable gradient computation for efficiency
    with torch.no_grad():
        # forward pass to get prediction
        output = model(user_preferences_tensor)
        # find the index of the maximum predicted value
        _, predicted_index = torch.max(output, 0)
    # return the index of the recommended restaurant
    return predicted_index.item()

# temp location api code
def get_nearby_restaurants(latitude, longitude, radius=1000, type='restaurant', key='YOUR_API_KEY'):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius={radius}&type={type}&key={key}"
    response = requests.get(url)
    data = response.json()
    if 'results' in data:
        return [place['name'] for place in data['results']]
    else:
        return []

# model parameters
input_size = 3
hidden_size = 5
output_size = 2

# instantiate model
model = RestaurantRecommendationModel(input_size, hidden_size, output_size)

# work on model training here
def train_model():
    pass

# pull user preferences
user_preferences = get_user_preferences()

# test location data here
user_latitude = 37.6721
user_longitude = -132.4323

# find nearby restaurants
nearby_restaurants = get_nearby_restaurants(user_latitude, user_longitude)

# display nearby restaurants
print("Nearby Restaurants:")
for i, restaurant in enumerate(nearby_restaurants, 1):
    print(f"{i}. {restaurant}")

# make rec (dummy rec)
recommended_restaurant = np.random.choice([0, 1])

# display recommendation
if recommended_restaurant == 0:
    print("\nwe think you should eat at Restaurant A!")
else:
    print("\nwe think you should eat at Restaurant B!")
