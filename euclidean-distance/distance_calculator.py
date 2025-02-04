import math

def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Define the points
point1 = (2, 3)
point2 = (10, 8)

# Calculate Euclidean distance
distance = calculate_euclidean_distance(point1, point2)

# Print the result
print(f"The Euclidean distance between {point1} and {point2} is {distance:.3f}")