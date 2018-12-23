# this program is testing various python concets
#  12/22/18 (pdf, jc)
#
####### begin variable declaration #######
# 
py_var= 10+10
weight = 74.2
height = 1.79

bmi = weight/height **2
in_str1 = 'the output'
in_str2 = "is:"
####### endvariable declaration #######
#
# begin main body of code
print ("My first python program that adds two numbers:")
print ((2+3), (int)(py_var))
print (123.25,(int)(123.56))
print ("#this is 4 to the 3rd power:",4 ** 3)
print ("this is 4 times 3 is:",4*3)
print ("this should yield the remainder of 8/3",8%3)

#print ("the bmi is:", (weight/(height **2)))
#print ('this bmi is:',  weight/height)
print (in_str1,in_str2,bmi)

# moving onto the following course module:
# https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-2-python-lists?ex=1
# create a list of lists
fam_list = [
    ['den',5.1],
    ['bob', 5.9],
    ['patti',5.6],
    ['kevin',5.8], 
    ['maureen',5.4]
    ]
# https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-2-python-lists?ex=6
print ("family contains the following:", fam_list)
#
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
areas = [hall, kit, "living room", liv, bed, "bathroom", bath]
print ("area list members are:",areas)
# this is where we left off:
# https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-2-python-lists?ex=7
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas [3] + areas [7]

# Print the variable eat_sleep_area
print ("Sum of ",areas [2]," and ",areas[6]," is: ",eat_sleep_area )
#
# https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-2-python-lists?ex=10
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
down_str = areas [6:]

# Alternative slicing to create upstairs
up_str = areas [:6]
print ("upstairs contains:",up_str)
print ("downstairs contains:",down_str)
#
# https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-2-python-lists?ex=13
# Correct the bathroom area
old_area_list = list (areas)
# old_area_list = areas
areas [9] = 8.75
# Change "living room" to "chill zone"
areas [4] = "chill zone"
print ("old list was:",old_area_list)
print ("new list is:", areas)