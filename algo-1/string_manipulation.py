# String Manipulation

# Name
name = input("Your name :")
# Age
age = input("Your Age :")

# Day
day = eval(input("Your Day (1-31) :"))
# Managemet error on day
while (day > 31 or day <= 0):
    print("Saisie incorrect :")
    day = eval(input("Your Day (1-31) :"))
    

# Months 
months = eval(input("Your Months (1-12) :"))
# Management error month
while(months > 12 or months <= 0):
    print("Saisie incorrecte")
    months = eval(input("Your Months (1-12) :"))
    
# Year
year = input("Year : ")

# Join day, months and year : day-months-year
birth = '-'.join([str(age) , str(months) , year])

print("Data ")
print('---------')
print("Name : {}\nAge :{}\nBirthday :{}".format(name , age , birth))