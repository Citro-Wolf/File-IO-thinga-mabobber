# Hello! #

#Modes 
#w - write
#a - append
#r - read 
#r+ / w+ Read & Write
#rb / wb - Read & Write Binary (in bytes! (b))
# Hope that helps! :3

#Configuration
#File names
file_name = "data.txt"
file_name2 = "numbers.txt"
#Text 
text_inserted = "file created." 



#Code
import random 
file = open(file_name, "w") # This code opens and allows you to write to whatever file you chose.
file.write(text_inserted + "\n")
file.close()

file = open("data.txt", "r")
data = []
for line in file:
    data.append(line)
print(data) 

with open(file_name2, "w") as file:
    for i in range(500):
        file.write(str(random.randint(-500,500)) + "\n") # Assigns 500 numbers ranging from -500 to 500.


data = []
with open(file_name2, "r") as file:
    for line in file:
        data.append(int(line)) # Converts the numbers on your "file_name2" from strings to integers. 