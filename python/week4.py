filename = input("Enter filename to read content:(include file extension) ")

try:
  with open(filename, "r") as file:
    data = file.read()
  with open("new.txt", "w") as newfile:
    newfile.write(data)
  print("Done!")
except FileNotFoundError:
  print("File not found. Please check filename.")