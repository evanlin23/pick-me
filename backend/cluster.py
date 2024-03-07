import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import pairwise_distances_argmin_min

# Load the CSV file
df = pd.read_csv('fast_food_restaurants.csv')

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words='english')

# Transform restaurant names into TF-IDF vectors
X = vectorizer.fit_transform(df['Restaurant'])

# Perform k-means clustering
num_clusters = 5  # You can adjust the number of clusters as needed
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(X)

# Function to recommend a restaurant based on input cuisine
def recommend_restaurant(cuisine):
    # Transform input cuisine into a TF-IDF vector
    cuisine_vector = vectorizer.transform([cuisine])
    
    # Find the cluster closest to the input cuisine
    closest_cluster = kmeans.predict(cuisine_vector)[0]
    
    # Find the restaurant closest to the centroid of the closest cluster
    centroid = kmeans.cluster_centers_[closest_cluster]
    closest_restaurant_idx = pairwise_distances_argmin_min(centroid, X)[0][0]
    recommended_restaurant = df.iloc[closest_restaurant_idx]['Restaurant']
    
    return recommended_restaurant

# Example usage:
cuisine_input = input("Enter a cuisine: ")
recommended_restaurant = recommend_restaurant(cuisine_input)
print("Recommended restaurant for", cuisine_input, "is:", recommended_restaurant)
