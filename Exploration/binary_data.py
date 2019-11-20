import pandas as pd
import numpy as np
import time

# Read training data
training_file_path = "../Data/train.json"
data = pd.read_json(training_file_path, orient='columns').head(500)

# Extract X (ingredients)
X = data['ingredients']

# Create a unique set of ingredients
ingredient_set = set()
for ingredients in X:
    for ingredient in ingredients:
        ingredient_set.add(ingredient)
        
# Convert set to list to create indexes
ingredients_list = list(ingredient_set)

# Add a column for every ingredient to the dataframe
i = 0
for ingredient in ingredients_list:
    i = i + 1
    
    if i % 1000 ==0:
        print(i)
    scores = []
    
    # Check whether recipe contains ingredient or not
    for rec_ing in data['ingredients']:
        if ingredient in rec_ing:
            scores.append(1)
        else:
            scores.append(0)
    
    data[ingredient] = scores

# Drop ingredients column
data = data.drop(['ingredients'],axis=1)

# Write file to csv
data.to_csv(r'training_binary.csv')

print(len(data.columns))