# try:
#     a = int("saroj")
# except Exception as e  :
#     print(e)
    
    
# decorators in python 

def test(func):
    def wrapper():
        print("before the func")
        
        func()
        
        print("after the func")
        
    return wrapper


@test
def hello():
    print("hello function")
    
hello()


evens  = [num for num in range(10) if num % 2 == 0 ]

print(evens)


names = ["Alice", "Bob", "Charlie"]

name_dict = {name : len(name) for name in names if len(name) > 3  }
print(name_dict)