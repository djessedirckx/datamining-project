import pandas as pd
import numpy as np
import time

# Read training data
training_file_path = "../Data/train.json"
data = pd.read_json(training_file_path, orient='columns')

# Extract X (ingredients) and y (cuisine)
X = data['ingredients']
y = data['cuisine']

# Create a unique set of ingredients
ingredient_set = set()
for ingredients in X:
    for ingredient in ingredients:
        ingredient_set.add(ingredient)
        
# Convert set to list to create indexes
ingredients_list = list(ingredient_set)

# Create a unique set of cuisines
cuisine_set = set()
for cuisine in y:
    cuisine_set.add(cuisine)
    
# Convert set to list to create indexes
cuisine_list = list(cuisine_set)

# Add a column for every ingredient to the dataframe
i = 0
start = time.time()
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
end = time.time()

print('Execution time: {}'.format(end - start))

# Drop ingredients column
data = data.drop(['ingredients'],axis=1)

# Write file to json
data.to_json(r'training_binary.json')
