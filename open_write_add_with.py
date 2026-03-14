# This Python script demonstrates the correct way to manipulate files using 'with'.
# It also shows the difference in memory usage and processing compared to manually opening and closing files.

#--IMPORTS--
from memory_profiler import profile


#--LOGIC--
@profile
def open_file():
    file_path = "files/text_open_write_add_with.txt"
    file = open(file_path, 'r')
    content = file.read()
    file.close()
    return content

if __name__ == "__main__":
    open_file()