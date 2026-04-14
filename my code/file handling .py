# # file handling in reading mode


# # f=open('myfile.txt','r')
# # contents=f.read()
# # print(contents)


# # #  file handling in writing mode
# # f=open("myfile.txt","w")
# # contents=f.write("my father name is mr.khushal negi")
# # print(contents)
# # f.close()

# # # file hNDLING IN WRITING MODE IN USING WITH

# # with open("myfile.txt", "w") as f:
# #     f.write("my father name is mr.khushal negi")


# #     #USING WITH FUNCUTION OPEN FILW IN READIMG MOOD

# # with open("myfile.txt", "r") as f:
# #     print(f.read())
# # f=open("myfile.txt",'a')
# # f.write ("hello world")
# # f.close()

# # #USING WITHB FUNCTION WRITE THE CONTENT IN WRTING MOOD
# # with open("myfile.txt",'a') as f :
# #    f.write("my name is nitesh")

# # #    TOPIC : READ ()READ LINES()AND OTHER

# # # f=open("myfile.txt",'r')
# # # while True:
# # #     line=f.readline()
# # #     if not line:
# # #         break
# # #     print(line)

# f=open("myfile.txt","r")
# i=0
# while True:
#     i=i+1
#     line=f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
   

#     print(f"marks of student {i} in maths is {m1}")
    
#     print(f"marks of student {i} in english is{m2}")

#     print(f"marks of student {i} in history is {m3}")
    
#     print(line)

# #  
# # f = open('myfile.txt', 'r')
# # i = 0
# # while True:
# #   i = i + 1
# #   line = f.readline()
# #   if not line:
# #     break
# #   m1 = int(line.split(",")[0])
# #   m2 = int(line.split(",")[1])
# #   m3 = int(line.split(",")[2])
# #   print(f"Marks of student {i} in Maths is: {m1}")
# #   print(f"Marks of student {i} in English is: {m2}")
# #   print(f"Marks of student {i} in SST is: {m3}")

# #   print(line)

# #wite line method
# f=open('myfile.txt','w')
# lines=['line1/n','line2/n','line3/n']
# f.writelines(lines)
# f.close()

f=open("in_transit_buses.csv","r")
contents=f.read()
print(contents)