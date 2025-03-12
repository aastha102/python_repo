
# To store data temporarily and permanently, we use files. 
# A file is the collection of data stored on a disk in one unit identified by filename. 

#   Open a file  in write mode
file=open("python_data.txt", "w")

# file= file pointer - which points to location of content in file.
# python_data.txt - file name
# "w"- mode of the file

file.write("This text file is open in write mode for writing data to the file.")
file.write("If python_data.txt exists, it will be overwritten. If not, a new file will be created.")
file.writelines("writelines()-Writes a list of strings to a file.\n Used to write multiple lines at once.\n \
Takes a list of strings and writes them to the file \n \
Used to write a single string to a file. \n \
Overwrites existing content if the file is opened in write mode ('w') \n \
Appends content if opened in append mode ('a').")
print(file.writable()) # It return true if file object for writing else false.
print(file.write_through) # In file handling, write-through means that data is immediately written to the file without buffering. 
# By default, Python uses buffered writing, meaning data is first stored in memory before being written to disk.

# How to Achieve Write-Through in Python?
# You can achieve write-through behavior using:

# Opening a file with buffering=0 (unbuffered mode)
# Using flush() to force writing data immediately
# Using os.fsync() to ensure data is saved to disk

file.close() # closing a file

# Open a file in read mode
with open("python_data.txt", "r") as file_read:
    sinlge_line=file_read.readline() # read single line from file
    print(file_read.tell())
    print(sinlge_line)
    # read a file in list format
    all_lines=file_read.readlines()  # it will output as list format
    file_read.seek(0) # move the file pointer to start
    content=file_read.read()
    print(file_read.readable()) # true if file is readable else false
   
    print(f"Content of file-\n {content}")
    print(f"all_lines {all_lines}")

''' [Note: When you call read(), it reads the entire file and moves the file pointer to the end of the file.
After that, if you try readlines(), it won’t return any data because there is nothing left to read.] '''
