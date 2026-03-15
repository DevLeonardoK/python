#Exception list
#NameError
#ValueError
#ZeroDivisionError
#TypeError
#IndexError
#KeyError
#EOFError
#KeyboardInterrupt
#OSError
#MemoryError
#ConnectionError
#RuntimeError

#default code
#try
    #action
#except
    #exception
    
    
#1 - Denominator and Numerator

"""
try: #try to execute
    numerator = int(input("Numerator: "))
    denominator = int(input("Denominator: "))
    result = numerator/denominator
except (ValueError, TypeError):
    print("Invalid input type")
except ZeroDivisionError:
    print("Division by zero (0) is not allowed")
except KeyboardInterrupt:
    print("Operation interrupted by user")
except Exception as exception:
    print(f"Exception cause:  {exception.__cause__}")
else: #success
    print(f"Result: {result:.1f}")
finally: #success/exception - always happens
    print("come back soon")
    
"""

#2 float and int

def get_int():
    while True:
        try:
            int_number = int(input("Int: "))
        except (ValueError, TypeError):
            print("Invalid input type")
        else:
            return int_number
    
def get_real():
    while True:
        try:
            real_number = float(input("Real: "))
        except (ValueError, TypeError):
            print("Invalid input type")
        else:
            return real_number
        

def input_user():
    int = None
    real = None
    try:
        int = get_int()
        real = get_real() 
    except KeyboardInterrupt as e:
        print("Operation interrupted by user")
    except Exception as exception:
        print("An error occurred")
    else:
        print("Real and int number are ok")
    finally:
        print(f"Real number: {real} <---> Int number: {int}")

input_user()