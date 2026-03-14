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
except: #exception
    print("An error occurred")
else: #success
    print(f"Result: {result}")
finally: #success/exception - always happens
    print("come back soon")