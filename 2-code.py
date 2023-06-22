# # help(round)
# help(print)

# My first function in Python

def sayHello(name="Quoicoubeh"):
    
    # Addig Docstring
    """This function allow to display your name after the word Hello

    Returns:
        >> sayHello("Yves")
        Hello Yves
    """
    return "Hello " + name


# function de calcul

def multiple_by_5(number):
    return number * 5

def fn(args , fn):
    """ Call multiple_by_5 in fn

        multiple_by_5 prend en params args
    """
    return fn(args)


# print(sayHello("Michel")  , sayHello("Jean"), sayHello(), sep="\n")
# help(sayHello)

print(fn(65,multiple_by_5)) # 65 * 5