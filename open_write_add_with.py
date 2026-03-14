# This Python script demonstrates the correct way to manipulate files using 'with'.
# It also shows the difference in memory usage and processing compared to manually opening and closing files.

#--IMPORTS--
from memory_profiler import profile, memory_usage


#--LOGIC--
file_path = "files/text_open_write_add_with.txt"

#open,read - manual
@profile
def open_file_manual():
    file = open(file_path, 'r')
    content = file.read()
    file.close()
    return content

#open, read - with
@profile
def open_file_with():
    with open(file_path, 'r') as file:
        content = file.read()
        return content


#Execution
if __name__ == "__main__":
    print("------------MANUAL------------")
    open_file_manual()
    print("\n------------WITH------------")
    open_file_with()
    