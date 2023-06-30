
with open("readwrite/test.txt","r+") as read_file:
    content = read_file.readlines()

line = 1
for i in content:
   print("Line {}: {}".format(line, i.strip()))
   line +=1



#a = open("readwrite/test.txt","a")
#a.write("\nToi 15 tuoi")
#a.close()



