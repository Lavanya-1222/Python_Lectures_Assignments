# 1. Find the second most frequent character in a given string using loops and conditionals.  
# s=input("enter string ")
# d={}
# for i in s:
#    if i in d:
#       d[i]+=1
#    else:
#       d[i]=1
# print(d)
# mx=max(d.values())
# second_high=0
# key=''
# for k,v in d.items():
#    if v<mx and second_high<v:
#       second_high=v
#       key=k
# print(key,second_high)
      
   

# # 2. Check if two strings are rotations of each other using loops.  
# s1=input("Enter string 1 ")
# s2=input("enter string 2 ")
# # abcd -> dabc-> cdab
# #  s2=> cdab
# #python -> npytho ->onpyth->honpy
# # s2=>honpy
# f=0
# rotates1=s1[1:]+s1[0]

# if len(s1)==len(s2):
#    for i in range(len(s1)-1):
#       if rotates1==s2:
#          f=1
#          break
#       else:
#          rotates1=rotates1[1:]+rotates1[0]
# if f==1:
#    print("Rotation is yes ",rotates1)
# else:
#    print('rotation is not')
      
      
      

   
# # 3. Remove all consecutive duplicate characters from a string using loops.  
# s=input("enter string ")
# # abbccddddde  ->ab
# r=''
# for i in range(len(s)-1):
#     if s[i]!=s[i+1]:
#         r+=s[i]
# if s[-1]!=r[-1]:
#     r+=s[-1]
# print(r)
        
# 4. Find all substrings of a given string using nested loops
# s=input("enter string ")
# # s=lavanya-> l,la,lav,lava,lavan,lavany
# l=[]
# for i in range(len(s)):
#     sub=''
#     for j in range(i+1):
#         sub=sub+s[j]
#     l.append(sub)

# print(l)
        
# 5. Find the longest palindrome substring in a given string using loops.
# s=input("enter string ")
# abcwoowbocmadam 


# 6. Replace all spaces with '%20' (like URL encoding) using loops.  
# s=input("Enter string ").strip()
# r=''
# for i in s:
#     if i==' ':
#         r+='%20'
#     else:
#         r+=i
# print(r)

# 7. Extract all numeric substrings from a given string using loops. 
# s=input("enter string ")
# r=''
# for i in s:
#     if i.isdigit():
#         r+=i
# print(r) 

# 8. Convert a given sentence to camelCase using loops and conditionals.  
# l=input("Enter String ").split(" ")

# r=''
# for i in l:
#     r+=i.capitalize()
# print(r)


# 9. Find all words that start with a vowel in a given sentence using loops. 
# l=input("Enter string ").split(" ")
# result=[] 
# for i in l:
#     if i[0] in 'AIOUEaioue':
#         result.append(i)
# print(result)

# 10. Sort the words in a given sentence in ascending order using loops.  
# l=input('Enter string ').split()
# r=''
# s='lavanya'
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         if ord(s[i])>ord(s[j]):
#             t=s[i]
#             s[i]=s[j]
#             s[j]=t
# pint(s)

# 11. Find all unique words from two given sentences using loops. 
# s=input("Enter string ").split() 
# l=[]
# for i in s:
#     if i not in l:
#         l.append(i)
# print(l)

# 
# 12. Check if a given string follows a specific pattern (e.g., "abba" → "dog cat cat dog") using loops and dictionaries. 
# s=input("Enter string ").split(" ")

# f=0
# if len(s)//2<=0:
#     j=len(s[0])-1
#     for i in range(len(s[0])//2):
#         if s[0][i]!=s[0][j]:
#             f=1
#         j-=1
# else:
#  j=len(s)-1
#  for i in range(len(s)//2):
#     if s[i]!=s[j]:
#         f=1
#     j-=1
# if f==0:
#     print("pattern follows")
# else:
#     print("not followed ")



# 13. Find the first non-repeating character in a given string using loops. 
# s=input("enter string ")
# l=[]
# for i in s:
#     if i not in l :
#         l.append(i)
#     else:
#         l.remove(i)
# print(l[0])

# 14. Remove all adjacent pairs of matching characters from a string using loops (e.g., "aabbcc" → "").  
# aabbabc
# s=input("enter string ")
# r=''
# for i in range(1,len(s)-1):
#     if  s[i-1]!=s[i] and s[i+1]!=s[i]:
#         r+=s[i]
# if s[-2]!=s[-1]:
#     r+=s[-1]
# print(r)

# 15. Implement a basic string compression algorithm (e.g., "aaabbc" → "a3b2c1") using loops.  
# aaabbc-> ]
# s=input("enter string ")
# c=1
# r=''
# for i in range(len(s)-1):
#     if s[i]!=s[i+1]:
#         r+=s[i]+str(c)
#         c=1
#     else:
#         c+=1
# print(r)

# 16. Convert a given integer to its equivalent string representation manually (without using str()).  
# n=int(input('Enter num '))
# digits=[]
# while(n!=0):
#     d=n%10
#     digits.append(chr(ord('0')+d))
#     n//=10
# s="".join(reversed(digits))
# print(s)

# 17. Find all anagram substrings in a given string using loops. 
# abc def cba gba c 
# s='abcdefcbagbac'
# p='abc'
# l=[]
# i=0
# while(i<len(s)):
#     sub=s[i:i+3]
    
#     f=0
#     if len(sub)==3:
#      for j in sub:
#         if j not in p:
#             f=1
#             break
#      if f==0:
#         l.append(i)
#         f=0
#     i+=1        
# print(l)

# 18. Reverse only the words in a sentence while keeping spaces intact using loops.  
# l=input("Enter string ").split(" ")
# r=[]
# for i in range(len(l)-1,-1,-1):
#     r.append(l[i])
# print(" ".join(r))


# 19. Write a function to format a string to title case, capitalizing only non-preposition words.  
# s=input("Enter string ").split(" ")
# r=[]
# for i in s:
#     if len(i)==1:
#         r.append(i[0].upper())
#     else:
#         r.append(i[0].upper()+i[1:])
# print(" ".join(r))

# 20. Find the longest common prefix among multiple given strings using loops.

# 1. Implement a custom strip() function to remove leading and trailing spaces from a string without using strip

def mystrip(s):
    r=''
    for i in range(len(s)-1):
        if s[i]!=" ":
            r+=s[i]
        else:
            if s[i+1]!=" " and i!=0:
                r+=s[i]

            
    return r

s=input("Enter string ")

print(len(mystrip(s)))
print(mystrip(s))

# 2. Find the longest repeating non-overlapping substring in a given string.  
# 3. Implement a function to check if a string is a valid IPv4 address.  
# 4. Convert a given sentence into "snake_case" and "kebab-case" using loops and conditionals.  
# 5. Given two strings, find the shortest string that contains both as subsequences (Shortest Common Supersequence).  
# 6. Find all possible permutations of a given string using recursion.  
# 7. Convert a Roman numeral string to an integer.  
# 8. Find the lexicographically next permutation of a given string.  
# 9. Implement a basic text justification algorithm to format a paragraph to a given line width.  
# 10. Check if a string follows a given regular expression pattern without using re module.  
# 11. Implement a function to check if a string is a valid scrambled version of another.  
# 12. Find the minimum number of edits (insertions, deletions, replacements) to convert one string into another (Levenshtein Distance).  
# 13. Given a dictionary and a jumbled string, find all valid words that can be formed.  
# 14. Find the longest common substring between two given strings.  
# 15. Determine if a string can be broken into a sequence of valid dictionary words (Word Break Problem).  
# 16. Find the smallest window in a string that contains all characters of another string.  
# 17. Implement a function to convert a string into a ZigZag pattern and read row-wise.  
# 18. Compress a string using Run-Length Encoding (RLE) and decompress it back.  
# 19. Check if a given string can be rearranged to form a palindrome (Palindrome Permutation).  
# 20. Implement a function to decode a string encoded with a shifting cipher (e.g., Caesar cipher)