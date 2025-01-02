print("Hello world")

name = "michel"
last_name = "Yandaki"

def say_hello(name: str, last_name: str) -> str:
    return 'Hello ' + name + ' ' + last_name


def main():
    print(say_hello(name , last_name))
    
main()