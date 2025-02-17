# 1. Implement a program to find the number of prime numbers in a given range using while loop.
# start=int(input("enter start range "))
# end=int(input("enter end range "))
# while(start<=end):
#  p=1
#  if start>1:
#     for i in range(2,start):
      
#         if start%i==0:
#             p=0
#             break
#     if p==1:
#        print(start,end=" ")
#  start+=1


# # 2. Find the number of unique characters in a string.
# c=0
# s=input("enter string ")
# l=[]
# for i in s:
#     if i not in l:
#         l.append(i)
#         c+=1
# print(c)


# 3.  Calculate the sum of all even Fibonacci numbers less than N and print the sequence.
# n=int(input("enter no "))
# n1=0
# n2=1
# c=0
# sum=0
# print(0,1,end=" ")
# while(True):
#     c=n1+n2
    
#     if c>n:
#         break
#     print(c,end=' ')
#     if c%2==0:
#         sum+=c
#     n1=n2
#     n2=c
# print("sum",sum)


# 4. Python function to check if a number is magical number or not
# n=int(input("enter no "))
# sum=0
# while(n!=0):
#     sum+=n%10
#     n//=10
# r=0
# while(sum!=0):
#     r+=sum%10
#     sum//=10
# if r==1:
#     print("Magical number")
# else:
#     print("not Magical number")


# 5. WAP print all the sum of Armstrong items from the list.
# l=[153,123,1,370]
# sum_of_arm=0
# for i in l:
#     le=len(str(i))
#     t=i
#     sum=0
#     while(t!=0):
#         sum+=(t%10)**le
#         t//=10
#     if sum==i:
#         sum_of_arm+=i
# print(sum_of_arm)


# # 6.Find the second largest element in a list.(without using inbuilt function)
# l=[10,20,30,40,50,60,60,70,70]
# max=0
# l1=[]
# for i in l:
#     if i not  in l1:
#         l1.append(i)
# second_largest=0
# max=0
# for i in l1:
#     if i>max:
#         second_largest=max
#         max=i
# print(second_largest,max)   


# 7. Write a program to flatten a nested list.
l=[1,2,3,[4,6,7,8],9,15,[3,4,5],(1,2,3,4,5),4,5]
# lst=[]
# for i in l:
#     if type(i)!=int:
#         for j in i:
#             lst.append(j)
#     else:
#         lst.append(i)
# print(lst)

n=[]
def lst(i):
    if type(i)==int:
        return i
    else:
        for j in i:
            return lst(j)
for i in l:
    p=lst(i)
    n.append(p)
# print(n)
print(n)


# 8. Remove all 3 from list.
# l=[1,2,3,4,8,9,3,6,5,3,1,3,54,3,12,9,3]
# for i in l:
#     if i==3:
#         l.remove(3)
# print(l)





# 9.Reverse words in a given string
#   input: s = “python quiz practice code” 
#   Output: s = “code practice quiz python”
# s = 'python quiz practice code'
# lst=s.split(" ")
# print(" ".join(lst[::-1]))

# without split
# lst=[]
# start=0
# for i in range(len(s)):
#     if s[i]==' ' or i==len(s)-1:
#         if i==len(s)-1:
#             word=s[start:i+1]
#             lst.append(word)
#         else:
#             word=s[start:i]
#             lst.append(word)
#             start=i+1
#         word=''

        
# print(lst)      
# print(" ".join(lst[::-1]))


# 10.Reverse the words, order should be maintained
#    str="Hello world "
#    output: "olleh dlrow"

# st="Hello world".split(" ")
# for i in range(len(lst)):
#     lst[i]=lst[i][::-1]
# print(" ".join(lst))l


# 11. Write a Python program to check if two strings are anagrams.
# s1=input("enter string1 ")
# s2=input("enter string2 ")
# f=1
# if len(s1)!=len(s2):
#     print("Not Anagrams")
# else:
#     for i in s1:
#         if i not in s2:
#             f=0
#             break
#     if f==1:
#         print("Anagrams Strings")
#     else:
#         print("not anagram strings")

    

# 12. Check a number is Automorphic or not.
# n=int(input("enter no "))#76
# sqr=n**n#5276
# l=[]
# p=1
# while(n!=0):
#     if sqr%10!=n%10:
#         p=0
#         break
#     sqr//=10
#     n//=10
# if p==1:
#     print("Automorphic")
# else:
#     print("not")
        
        

# 13. Write a Python program to count the number of vowels in a given string.
# s=input("enter string ")
# vc=0
# c=0
# for i in s:
#     if i in 'aioueAIOUE':
#         c+=1
# print(c)


# 14. Write a Python program to find the first non-repeating character in a string.
# s=input("enter string ")
# d={}
# chr=''
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# for i in d:
#     if d[i]==1:
#         print(i)
#         break


# 15. Given a string, write a Python program to find the frequency of each character using a dictionary.
# print({i:s.count(i) for i in s})