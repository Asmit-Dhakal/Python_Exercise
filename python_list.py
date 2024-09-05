fam=[1,2,3,4]
print(fam)

family=['liz','ema',1,'hello']
print(family)
hello =type(family)
print(hello)

# Multiple List
fam2 = [
    ["ram",1.2],
    ["b",1.3],
    ["c",1,4]
]
print(fam2)

# list slicing
slice  = ['ram','sam','Hari',"sita",'Gita',"1.68",1.89,2.46]
print(slice[3:5]) # 3 include and exclude 5

print(slice[:4]) #

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
print(house[4][1])
# Subset the house list
print(house[-1][1])