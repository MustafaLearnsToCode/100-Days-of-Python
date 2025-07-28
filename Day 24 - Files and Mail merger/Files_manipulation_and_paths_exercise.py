# with open("my_file.txt") as file2: #you can open files this way, don't have to close them then.
#     contents = file2.read()
#     print(contents)
#
# file = open("my_file.txt") #Don't forget type extension ie. .txt
# file.close() #don't forget to close the file

with open("../../../mustafabadshah/Downloads/new_file.txt", mode="w") as file: #default is read-only mode, "w" = write (deletes contents before) and "a" is for append
    file.write("\nNew text.")

#use mode "w" and use a new file name to create new files

#root - main drive starting represented by /
#direction explained using / ex. /Work/Projects/Presentation.ppt
#absolute file path - starting with root
#relative file path - ./(look in current folder), ../(go to parent folder)