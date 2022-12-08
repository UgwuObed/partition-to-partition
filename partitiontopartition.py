
#import os module
import os

#importing shutil module
import shutil

# path
path = "/home/User/Desktop/harddrive"

#List files and directories in "/home/User/Desktop/harddrive"
print("Before moving file:")
print(os.listdir(path))

# Indicate the path of the running app
source = "/home/User/Desktop/harddrive/partition1"

# Permission of the path of the running app
perm = os.stat(source).st_mode
print("File Permission mode:", perm, "\n")

# Indicate the destination path 
destination = "/home/User/Desktop/harddrive/partition2"

# Move the running app from the partition1 to the partition 2
try:
  shutil.move(source, destination)
  print("Application moved successfully.")
except Exception as e:
  print("An error occurred while moving the application:", e)

# List the files and directories in the hard drive again to show that the application has been moved
print("\nAfter moving file:")
print(os.listdir(path))



