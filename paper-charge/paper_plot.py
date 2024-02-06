import matplotlib.pyplot as plt

# paper area and distance from balloon
area = [5, 10, 23.375, 46.75]
distance = [1.63, 3.26, 2.26, 1.86]

# Plotting the relationship between voltage and current
plt.figure(figsize=(10, 6))
plt.scatter(area, distance, color='blue')
plt.title('Area vs. Distance')
plt.xlabel('Area (square inches)')
plt.ylabel('Distance (inches)')
plt.grid(True)

# Display the plot
plt.show()