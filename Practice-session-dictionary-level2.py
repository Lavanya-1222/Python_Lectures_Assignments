# 1. Given a dictionary, group keys that have the same values.
# data = {"a": 1, "b": 2, "c": 1, "d": 3}
# #     o/p= {1: ['a', 'c'], 2: ['b'], 3: ['d']}
# result={}
# for k,v in data.items():
#     if v in result:
#         result[v].append(k)
#     else:
#         result.update({v:list(k)})
# print(result)

# 2. Identify which value appears the most in a dictionary.
# data = {"a": 1, "b": 2, "c": 1, "d": 3}
# result={}
# for i in data:
#     if data[i] in result:
#         result[data[i]]+=1
#     else:
#         result[data[i]]=1
# print(result)


# 3. Convert Two Lists into a Dictionary without using zip function.
# l1=[1,2,3,4]
# l2=[10,20,30,40]
# r={}
# for i in range(len(l1)):
#     r.update({l1[i]:l2[i]})
# print(r)

# 4. Given a string, count how many times each word appears.
# s=input("Enter string ").split(" ")
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
#    text = "apple banana apple apple orange banana"
#     Output: {'apple': 3, 'banana': 2, 'orange': 1}


# 5. Write a Python function to count the frequency of each chara in a string and return a dictionary with char frequencies.
# s=input("enter string ")
# d={i:s.count(i) for i in s}
# print(d)


# 6. Fetch best_buy_date and best_Sell_date from following dictionary:
# d = {
#     '1/1/2024': 1200,
#     '2/1/2024': 100, # 400
#     '3/1/2024': 50,  # 450
#     '4/1/2024': 120,
#     '5/1/2024': 370,
#     '6/1/2024': 500,
#     '7/1/2024': 300
# }
# best_sell_date=''
# best_buy_date=''
# mx=0
# for k,v in d.items():
#         for k1,v1 in d.items():
#                 if int(k1[0])>int(k[0]):
#                         # print(k1,v1)    
#                         if (v1-v)>mx:
#                             mx=v1-v
#                             best_buy_date=k
#                             best_sell_date=k1

# print(best_buy_date,best_sell_date,mx)
    

# 7. Find the longest key name in a dictionary.
# from functools import reduce
# d={'abc':1,'a':23,'defc':8}
# print(reduce(lambda x,y: x if len(x)>len(y) else y,d.keys()))
# mx=0
# l_key=''
# for k in d:
#     if len(k)>mx:
#         mx=len(k)
#         l_key=k
# print(l_key)


# 8. Write a function that merges two dictionaries,adding values for keys that appear in both dictionaries.
# data = {"a": 1, "b": 2,"d": 3}
# d2={"c": 1,'a':1}
# d3={}
# for k in data:
#     if k in d2:
#         d3.update({k:data[k]+d2[k]})
#     else:
#         d3[k]=data[k]
# for k in d2:
#     if k not in data:
#         d3[k]=d2[k]
# print(d3)
    

# 9. Given two dictionaries, write a function to find and return a new dictionary containing only the common keys and their corresponding values.
data = {"a": 1, "b": 2,"d": 3}
d2={"c": 1,'a':1}
d3={}
for k in data:
    if k in d2:
        d3[k]=list(data[k],d2[k])
print(d3)
# 10.Develop a function that finds the element with the maximum frequency in a list ,and returns the element along with its frequency.