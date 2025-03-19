# Level 1:
# 1. How do you create an empty dictionary in Python?
d={}
d2=dict()
print(type(d))
print(type(d2))
# 2. How do you add a key-value pair to a dictionary in Python?
d.update({'nitish':'Mech'})
d['lavanya']='comp'
print(d)
# 3. How do you remove a key-value pair from a dictionary in Python?
d.pop('nitish')
print(d)
# 4. How do you check if a key exists in a dictionary in Python?
print('lavanya' in d)
# 5. How do you access the value associated with a key in a dictionary in Python?
print(d['lavanya'])
print(d.get('lavanya'))
# 6. How do you find the length of a dictionary in Python?
print(len(d))
# 7. How do you update the value of an existing key in a dictionary in Python?
d['lavanya']='Computer'
print(d)
# 8. How do you iterate over the keys of a dictionary in Python?
for i in d.keys():
    print(i)
# 9. How do you iterate over the values of a dictionary in Python?
for v in d.values():
   print(v)
# 10. How do you iterate over the key-value pairs of a dictionary in Python?
for k,v in d.items():
    print(k,v)
# 11. How do you get a list of all the keys in a dictionary in Python?
lst_key=list(d.keys())
print(lst_key)
# 12. How do you get a list of all the values in a dictionary in Python?
lst_values=list(d.values())
print(lst_values)
# 13. How do you get a list of all the key-value pairs in a dictionary in Python?
lst_key_value=list(d.items())
print(lst_key_value)
# 14. How do you clear all elements from a dictionary in Python?
d.clear()
print(d)
# 15. How do you copy a dictionary in Python?
d2={1:10,2:30}
d=d2.copy()
print(d)
# 16. How do you merge two dictionaries in Python?
d1={10:100,20:300}
d2={1:10,2:30}
d3={}
for i in d1:
    d3.update({i:d1[i]})
for j in d2:
    d3.update({j:d2[j]})
print(d3)
# 17. How do you create a dictionary from two lists, one for keys and one for values, in Python?
l1=['A','B','C','D','E']
l2=[100,200,300,400,500]
dct={}
for k,v in zip(l1,l2):
    dct.update({k:v})
print(dct)
    
# 18. How do you get the value of a key in a dictionary with a default value if the key does not exist in Python?
d4={1:10,2:20}
d4.setdefault(200)
# print(d4[3])

# 19. How do you remove a key from a dictionary and get its value in Python?
# print(dct.pop('A'))

# Level 2:
    
# 21. How do you find the maximum value in a dictionary in Python?
# d={1:10,2:30,3:40,5:80,6:10}
# max=0
# for i in d.values():
#     if i>max:
#         max=i
# print("Maximum",max)

# 22. How do you find the minimum value in a dictionary in Python?
# d={1:10,2:30,3:40,5:80,6:10}
# min=d[1]
# for i in d.values():
#     if i<min:
#         min=i
# print("Minimum",min)

# 23. How do you find the key associated with the maximum value in a dictionary in Python?
# d={1:10,2:30,3:40,5:80,6:10}
# mx=0
# key=''
# for i in d:
#     if d[i]>mx:
#         mx=d[i]
#         key=i
# print(key,mx)

# 24. How do you find the key associated with the minimum value in a dictionary in Python?
d={1:10,2:30,3:40,5:80,6:10}
min=d[1]
key=1
for i in d:
    if d[i]<min:
        min=d[i]
        key=i
print(key,min)
# 25. How do you sort a dictionary by keys in Python?
d={1:10,2:30,3:40,5:80,6:10}
print(sorted(d.items(),key=lambda x :x[0]))

# 26. How do you sort a dictionary by values in Python?
print(sorted(d.items(),key=lambda x: x[1]))

# 27. How do you filter a dictionary by keeping only the key-value pairs that satisfy a condition in Python?
#   (eg.fetch those values are greater than 15)
d={1:1,2:10,3:40,5:80,6:20,7:6}
result={}
for i in d:
    if d[i]>15:
        result.update({i:d[i]})
print(result)



# 28. How do you reverse the keys and values in a dictionary in Python?
d = {'a': 60, 'b': 25, 'c': 60}
d2={}
for k,v in d.items():
    if v in d2:
        d2[v]=[d2[v],k]
    else:
        d2.update({v:k})
print(d2)

# 29. How do you count the occurrences of each character in a string using a dictionary in Python?
s='lavanya'
d={i:s.count(i) for i in s}
print(d)
# 30. How do you group elements by length of a list based on a function using a dictionary in Python?
#     words = ["apple", "bat", "cat", "banana", "ant"]


