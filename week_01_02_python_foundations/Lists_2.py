house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]
house[4][1] = 12   
house = house + [["garage", 15.0]]
del(house[3])
print(house)