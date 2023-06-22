# Loops and lists Comprehension


# 1 - Case
# Use loop for print each element of a lists.
# # Lists of planets
planets = [
    "Mars" , "Mercury" , "Pluton" , "Jupiter" , "Saturne" , "Uranus" , "La planete Terre"
]

for planet in planets:
    print(planet , end='\n')


# 2 - Case
# Use loop and tuple
myTuple = (2 , 48 , 22 , 100, 4)

# Multiple each element of tuple
product = 1

for mult in myTuple:
    product = mult * product

print('Product' , product)

# 3 - Case 
# Read each element of an suite of words
# print each word who is in Upper Case

phrase = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'

# Check for each element of the phrase if this element is Upper or not. If this case is true, then print this element
for word in phrase:
    if (word.isupper()):
        print(word , end='')


# 4 - Case
# use range function in Loop
for n in range(5):
    print("Loop n-",n)
# made the same result with While loop
n = 0
while n < 5:
    print("Loop n-",n)
    n += 1
    
# Lists comprehension
# Understand the behavior of Lists and Loop in Pyhton
# example how fill a list efficiently

# 1 - A lists of power of 0 to 10
testListsPow = [n**2 for n in range(10)]

print(testListsPow) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 2 - A list of planet who are superior than 5
testListsPlan = [planet.upper() for planet in planets if len(planet) > 5]
print(testListsPlan)

# Lists of number negative or positive
numbers = [1 , -3 , 8, -63  , -12 , 9]

# Function who count element who is negative
def count_negatives(lists):
    
    numbers_negatives = 0
    
    # Read each element of the lists
    for num in lists:
        # Compare element, if element is negative then incrementation of numbers_negatives
        if(num < 0):
            numbers_negatives += 1
            
    return numbers_negatives

# Made this function without all these code

def new_count_negatives(lists):
    # Count element negative
    return len([num for num in lists if num < 0])

print(count_negatives(numbers))
print(new_count_negatives(numbers))
