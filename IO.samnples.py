#I/O notes+ 
#? Write to text file- output 
file = open("example.txt", "a") 
file.write("Hello ninja") 
file.write("\n")
file.close()
#? Read from open text file 
with open("example.txt", "r")as file:
    content = file.read()
    print(content) 
    file.close
