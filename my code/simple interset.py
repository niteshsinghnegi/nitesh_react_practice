# # Input from the user
# principal = float(input("Enter the principal amount (P): "))
# rate = float(input("Enter the rate of interest (R): "))
# time = float(input("Enter the time period in years (T): "))

# # Calculate Simple Interest
# simple_interest = (principal * rate * time) / 100

# # Display the result
# print(f"The simple interest is: {simple_interest}")


# def add (a,b,sum):
#     try :
#         a=int(input("enter the value of a "))
#         b=int(input("enter the value of b"))
#         sum=a+b
#         print(sum)
#         return 1
#     except:
#         print  ("some error occurd")  
#         return 0
#     finally :
#         print("very good nitesh ")
# name= "Nitesh"
# print("hello"+name)

# x=add(5,6,sum)
# print(x)
        

# r=open('myfile.txt' ,'r')
# contents=r.read()
# print(contents)
# r.close()
# f=open('myfile.txt','w')
# f.write("nitesh is a good boy ")
# f.close()
 
# 

# animal="tiger"
# len=len(animal)
# print(len)









# numbers = [1, 2, 3, 4, 5]
# print(numbers[2])





# fruits = ("apple", "banana", "cherry", "apple")
# print(fruits.count("apple"))




class answer:
    def __init__(self,firstnumber,secondnumber):
        self.firstnumber=firstnumber
        self.secondnumber=secondnumber
    def add(self) :
        return self.firstnumber+self.secondnumber
num1=answer(4,5)  
print(num1.add())      


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len

# Example usage:
solution = Solution()
result = solution.lengthOfLongestSubstring("niteshsingh")
print(result)






