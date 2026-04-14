# reverse a string
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
