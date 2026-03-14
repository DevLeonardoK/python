# This Python script demonstrates the correct way to manipulate files using manual open and using 'with open' and Path lib.
# It also shows the difference in memory usage and processing compared to manually opening and closing files.

#--IMPORTS--
from memory_profiler import profile, memory_usage
from pathlib import Path


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


#Path
@profile
def open_file_path():
    path = Path(file_path)
    with path.open('r') as file_open:
        content = file_open.read()
    
    with path.open('a') as file_add:
        content = "\n" + content + " - Hello 3"
        file_add.write(content)
        return f"File content: {content}"
    
    
# Code example: writelines with lists and tuples
scores = [10.0, 5.0, 2.0, 7.0, 6.5] #List
subjects = ("math","history","biology","physics", "chemistry") #Tuples
student = ["David", "Matew", "Nikolas", "Sarah", "Jacob"]

@profile
def example_grades_report():
    path = Path(file_path)
    list_content = []
    content = []
    length = len(subjects)
    
    for r in range(length):
        list_content.append(f"\n\n\n\n\n\n ------Example------ \nStudent {student[r]} received a grade of {scores[r]} in {subjects[r]}")

    with path.open('a') as file:
        file.writelines(list_content)
    
    return 'Ok'    
    
#Execution
if __name__ == "__main__":
    print("------------MANUAL------------")
    open_file_manual()
    print("\n------------WITH------------")
    open_file_with()
    print("\n------------PATH + WITH------------")
    open_file_path()
    print("\n------------Example------------")
    example_grades_report()