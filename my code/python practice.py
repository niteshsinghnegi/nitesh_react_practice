# # reverse a string
s=input("enter a string:")
print("reverse string is :",s[::-1])

# count vowels,and consostance
s=input("enter the string :")
vowels="aeiouAEIOU"
c=0
v=0
# V=C=0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v+=1
        else:
            c+=1
print("vowels",v)            
print("constans",c)  


# cheack given string paledron or not 
s=input("enter a string:")
if s==s[::-1]:
    print("the given string is pailedron")
else:
    print("the given string is not a pailedron ")

# count  the number of words in string 
s=input ("enter the string :")
print(len(s))

# covert a string to uper case and lower case 
s=input("enter a string ")
print(s.upper())
print(s.lower())

# Count Frequency of Each Character
s=input("enter a string ")

freq={}
for ch in s:
 freq[ch]=freq.get(ch,0)+1
 print("charactor frequnece ",freq)

# Find Longest Word in a Sentence
s = input("Enter a sentence: ")
words = s.split()
print(words)
longest = max(words, key=len)
print("Longest word:", longest)

# Check if Two Strings are Anagram
s1 = input("Enter a sentence: ")
s2=input("Enter a sentence: ")
if sorted(s1)==sorted(s2):
 print("anagram")
else:
 print(" not anagram")

# Remove All Digits from String
s1 = input("Enter a sentence: ")
result=''.join([ch for ch in s1 if not ch.isdigit()])
print("remove all digit to string ",result)

# Find First Non-Repeated Character
s = input("Enter a string ")
for ch in s:
    if s.count(ch)==1:
        print("frist non repted charcheter ",ch)
        break

# Replace a Word in Sentence
s = input("Enter a string ")
a=input("word to replace ")
b=input("new word")
print(s.replace(a,b))

# Check if String Contains Only Digits
s = input("Enter a string ")
if s.isdigit():
    print("the string contain only digit ")
else:
    print ("string not contain a digit ")

# Count Uppercase and Lowercase Letters
s = input("Enter a string ")
u=0
l=0
for ch in s:
    if ch.isupper():
        u+=1
    elif  ch.islower():
      l+=1
      
print("upper case",u)
print("lower case",l)

# Print All Substrings of a String

s = input("Enter a string: ")
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        print(s[i:j])
   
   
#    Check if String is Alphanumeric
s = input("Enter a string: ")
if s.isalnum():
   print("string is alphanumric")
else:
    print("string is not  alphanumric")

    # Remove Punctuation
import string
s= input("enter the string")
for p in string.punctuation:
   s=s.replace(p,"")
print("with out punction ",s)

# Find Common Characters in Two Strings
s1= input("enter the string")
s2= input("enter the string")
comman=set(s1)&set(s2)
print("comman charater ",comman)

# Check String Starts or Ends With Specific Word
s1= input("enter the string")
word=input("check the specific word ")
if s.startswith(word): 
 print("sentence start with ",word )
elif s.endswith(word):
   print("sentence ends with ",word)
else:
   print("no match ")

#     Mini Project Idea – String Analyzer
def string_analyzer(s):
    print("Length:", len(s))
    print("Vowels:", sum(ch in 'aeiouAEIOU' for ch in s))
    print("Digits:", sum(ch.isdigit() for ch in s))
    print("Uppercase:", sum(ch.isupper() for ch in s))
    print("Lowercase:", sum(ch.islower() for ch in s))
    print("Spaces:", s.count(" "))
    print("Reversed:", s[::-1])

s = input("Enter your string: ")
string_analyzer(s)


# cheack number positvie and negtie 
num=12
if(num>0):
    print("num is positive")
else:
    print ("num is neg")

# even odd in python 
num =13
if(num%2==0):
    print("num is even ")
else:
    print ("num is odd")

# : Check grade based on marks.
# num=90
if(num>=85):
    print("grade a")
elif(num>=75):
    print("grade is b")
elif(num>=60):
    print("grade is c")
elif(num>=45):
    print("grade is d")
else:
    print("student fail")

# find largest number in three number 
a=45
b=23
c=90
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
else:
    print("c is greater")

# Check if a year is a leap year
year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

# Check if a number is divisible by 2 and 3.
num=12
if num % 2==0:
    if num %3==0:
     print( "num devided by 2 and 3")
    else:
       print("num deivied by only 2")

balanced=5000
withdraw=200
if withdraw  <= balanced:
    balanced -=withdraw
    print((f"Withdrawal successful! Remaining balance: {balanced}"))     
else:
    print("does not exit amount ")
 

temp=34
if(temp>40):
    print("temp is very hot ")
elif(temp>35):
    print("temp is  hot ")
elif(temp>28):
    print ("today is cool")
else:
    print("today is very cool")

num = int(input("Number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
else:
    print("Not prime")


color="red"
if color=="red":
    print("stop ")
elif color=="yellow":
    print("start your vichels ")
elif color == "green":
    print("chlo chle ")