# use condition in code and function

# Function pour determiner si un candidat peut concourir a la presidentielle, depend de L'age et de son origin
def can_run_for_president(age , origin_of_country=False):
    """function which determinate if a candidate can run for presidential election, depends of the years old and origin.

    Returns:
        can_run_for_president(67)
        >> False
        can_run_for_president(45, True)
        >> True
    """
    return (origin_of_country and (age >= 35))


# Examiner la nature du nombre (positif , negatif ou nulle)
def inspect(x):
    """Examinate the type of number in paramter either (Positive , negative or zero)

        inspect(45)
        >> 45 is positive
        inspect(-2)
        >> -2 is negatie
    """
    if(x > 0):
        print(x , 'is positive')
    elif (x < 0):
        print(x , 'is negative')
    elif (x == 0):
        print(x , 'is zero')
    else:
        print("I don't this type")



inspect(109)
inspect(-9)
inspect(00)

# print(can_run_for_president(45 , True))
# print(can_run_for_president(34 , True))