import os

cwd=os.getcwd()
print(f"Currect Working Directory {cwd}")

os.chdir("../") # going back one step

print(os.getcwd())

os.chdir("C:/Users/Astha/Documents/Git") # changing to particular location
print(os.getcwd())
# create single directory inside that location-C:/Users/Astha/Documents/Git
# os.mkdir("directory")  

# [Note: If directory already exist in that location it will throw error]
print(os.listdir()) # list out all files and directory in that location

# Removing directory from that loocation
# os.rmdir("directory") # 
print(os.listdir())

print(os.name) # give you the name of operating system

# Rename the existing file
# os.rename("js-2025", "js-2023")
print(os.listdir())

# check the directory path exist or not
print(os.path.exists("C:/Users/Astha/Documentss"))

# Size of the file
print(os.path.getsize("C:/Users/Astha/Documents"))