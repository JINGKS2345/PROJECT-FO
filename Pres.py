import os

print("FOLDER TO ORGANIZE")
folder_path = str(input("Enter the path of your foler: "))

print("CHECKING IF THE FOLDER EXISTS")
if os.path.exists('Pres.py'):
    print("The file exists!")
else:
    print("The file does not exist.")

# GETTING THE LISTS OF FILES IN THE FOLDER
print("All folders & files:", os.listdir())


