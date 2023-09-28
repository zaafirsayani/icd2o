length_of_wall= float(input("Enter the length of one wall (in meters): "))
width_of_wall= float(input("Enter the width of one wall (in meters): "))
height_of_house= float(input("Enter the height of the house (in meters): "))
cost_per_brick= float(input("Enter the cost per brick (in dollars): "))
dimensions_of_brick= float(input("Enter the dimensions of a standard brick (length width height, in meters): "))
wall_surface_area= float(f"{length_of_wall*width_of_wall*height_of_house}")
bricks_required= length_of_wall/
total_cost_bricks= bricks_required*cost_per_brick

print(length_of_wall)
print(width_of_wall)
print(height_of_house)
print(cost_per_brick)
print(dimensions_of_brick)
print()
print()
print("House Details: ")
print(f"- Wall Surface area: {wall_surface_area} square meters")