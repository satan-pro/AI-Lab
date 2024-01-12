import math

# Function to compute Euclidean distance
def euclidean_distance(x, y):
    return math.sqrt((x - y) ** 2)

# Function to perform Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Create two lists X and Y with numerical values
X = [2, 4, 7, 10, 5]
Y = [1, 5, 9, 8, 4]

# Compute Euclidean distances for corresponding values in X and Y
distances = [euclidean_distance(x, y) for x, y in zip(X, Y)]

# Display the unsorted distances
print("Unsorted Distances:", distances)

# Sort the distances using Bubble Sort
bubble_sort(distances)

# Display the sorted distances
print("Sorted Distances:", distances)
