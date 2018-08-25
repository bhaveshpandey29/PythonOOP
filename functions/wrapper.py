def wrapper(func):
    def inner():
        print("Before function execution")
        func()
        print("after function execution")
    return inner

@wrapper #printMe = wrapper(printMe)
def printMe():
    print("hello! nice to meet you")
    #printMe()

@wrapper
def demo():
    print("demo print")
    #demo()