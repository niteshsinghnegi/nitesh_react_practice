# name=input("enter your name")
# try:
#      if(name=="manyata"):
#        print("nitesh loves you ")

# except:
#         print("i am not intersted")
    
# finally:
#  print("jai bhole ki ")



# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = {}

#     def add_grade(self, course, marks):
# #         self.grades[course] = marks

#     def average(self):
#         if not self.grades:
#             return 0.0
#         return sum(self.grades.values()) / len(self.grades)

#     def top_course(self):
#         if not self.grades:
#             return ''
        
#         return max(self.grades, key=lambda c: self.grades[c])


# class Song:
#     def __init__(self, title, duration_sec):
#         self.title = title
#         self.duration_sec = duration_sec

# class Playlist:
#     def __init__(self, name):
#         self.name = name
#         self.songs = []

#     def add_song(self, song):
#         self.songs.append(song)

#     def total_duration(self):
#         return sum(song.duration_sec for song in self.songs)

#     def __len__(self):
#         return len(self.songs)






# name1 ={"nitesh"  ,"amit","abhishek"}
# name2= {"nitesh","sumit","daksh"}
# name3=name1.union(name2)
# print(name3)
                                        






num1={1,2,3,4,5}
num2={1,7,8,3,9}
print(num1.isdisjoint(num2))
                                   



