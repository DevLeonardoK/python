# This Python script demonstrates the correct way to manipulate files using manual open and using 'with open'.
# It also shows the difference in memory usage and processing compared to manually opening and closing files.

#--IMPORTS--
from memory_profiler import profile, memory_usage


#--LOGIC--
file_path = "files/text_open_write_add.txt"

#open,read - manual
@profile
def open_file_manual():
    
    file_read = open(file_path, 'r')
    content = file_read.read()
    file_read.close()
    
    file_add = open(file_path, 'a')
    content = content + "Hello 1"
    file_add.write(content)
    file_add.close()
    return f"File content: {content}"

#open, read - with
@profile
def open_file_with():
    
    with open(file_path, 'r') as file_read:
        content = file_read.read()
    
    with open(file_path, 'a') as file_add:
        content = "\n" + content + " - Hello 2"
        file_add.write(content)    
        return f"File content: {content}"


#Execution
if __name__ == "__main__":
    print("------------MANUAL------------")
    open_file_manual()
    print("\n------------WITH------------")
    open_file_with()
    