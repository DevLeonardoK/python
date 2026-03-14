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