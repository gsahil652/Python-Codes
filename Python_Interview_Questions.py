#!/usr/bin/env python
# coding: utf-8

# ### Que1:- Write a python code in which we will take Integer as input from user and print the square root of integers smaller than that.
# 
# Example :- Input = 5
#            Output :- 0, 1, 4, 9, 16
# 

# In[1]:


import math
n = int(input())
for i in range(n):
    print(i**2)


# ### Que2:- Write a code in which we need to check SET A is subset of SET B or not
# 
# Example :- 
# 
# Input:- 
# 
# 1) Take T as input from user to enter total test case.
# 
# 2) Now first it will check the length of Set A.
# 
# 3) It will print the each element in set A separated by comma.
# 
# 4) Now it will check the length of Set B.
# 
# 5) It will print the each element in set B separated by comma.
# 
# 6) If A is subset of B it will print 'True' else 'False'.  
# 
# Output:-
# 
# True or False

# In[5]:


T = int(input()) # No of test cases
for i in range(T):
    len_a = int(input())
    a = set(map(int, input().split()))
    print(a)
    len_b = int(input())
    b = set(map(int, input().split()))
    print(b)
    print(a.issubset(b))


# In[9]:


A = set(map(int, input().split()))
print("Elements of set A :- ",A)
n = int(input())
B = set(map(int, input().split()))
print("Elements of set B :- ",B)
C = set(map(int, input().split()))
print("Elements of set C :- ",C)
print(A.issuperset(B))
print(A.issuperset(C))


# ### Que3:- The MINION GAME
#     
# Rules:- 
#     
# 1) Both players are given the same string 'S'.
# 
# 2) Both players have to make substrings using the letters of the string .
# 
# 3) Stuart has to make words starting with consonants.
# 
# 4) Kevin has to make words starting with vowels.
# 
# 5) The game ends when both players have made all possible substrings.
# 
# For Example :- 
# 
# String 'S' = 'BANANA'
# 
# Kevin's vowel beginning word = ANA
# 
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points

# In[38]:


S = str(input())
print('The String is:-', S)
kevsc = 0
stusc = 0
s = string
    
def is_vowel(i):
    return i in 'AEIOU'

# Loop through each character in the string
for i in range(len(string)):
    # Calculate the score for Kevin
    if is_vowel(string[i]):
        kevsc += len(string) - i
        #print(kevsc)
    # Calculate the score for Stuart
    else:
        stusc += len(string) - i
        #print(stusc)
        
if (kevsc>stusc):
    print('Kevin', kevsc)
elif (stusc>kevsc):
    print('Stuart', stusc)
else:
    print('Draw')


# In[42]:


n = int(input())
for i in range(1,n):
    print(str(i)*i)


# In[48]:


i = 4
num = i
row_value = num * (10 ** (i - 1))
print(row_value)


# In[50]:


n = 6  # height of the triangle

for i in range(1, n):
    print(i * (10 ** i - 1) // 9)


# In[ ]:





# In[52]:


S  = str(input())
S = S .lower()
print(S)


# In[59]:


from collections import Counter
S  = str(input())
S = S .lower()
# Counter is used to count the occurence of each character in string
count = Counter(S)
print(count)
#
most_common = sorted(count.items(), key=lambda x: (-x[1], x[0]))

# Print the result
for i, j in most_common[:3]:
    print(i,j)


# In[61]:


import re

def validate_credit_card(number):
    # Check if the number starts with 4, 5, or 6
    if not re.match(r'^[456]', number):
        return False

    # Check if the number contains exactly 16 digits
    if not re.match(r'^\d{16}$', number):
        return False

    # Check if the number consists only of digits and hyphens
    if not re.match(r'^[\d-]+$', number):
        return False

    # Check if the number has groups of digits separated by a single hyphen
    if not re.match(r'^(\d{4}-?){4}$', number):
        return False

    # Check if the number does not have 4 or more consecutive repeated digits
    if re.search(r'(\d)\1\1\1', number):
        return False

    return True

# Take input from the user
number = input("Enter credit card number: ")

# Validate the input
if validate_credit_card(number):
    print("Valid credit card number")
else:
    print("Invalid credit card number")


# In[ ]:




