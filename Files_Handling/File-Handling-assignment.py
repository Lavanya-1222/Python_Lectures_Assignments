#  Task: Library System Data Handling

#     Imagine you're building a Library Management System. You need to create a file to store book information (such as book title, author, and publication year). After creating and writing the data into the file, you'll read the data, process it by performing various tasks (like sorting, filtering, and performing calculations), and then store the processed data in a new file. After that, you'll delete the original file.

#  Steps:

# 1. Create a file with book data:
#    - Store book information (book title, author, publication year) in a file.
#    - Example data for the file:

#      "The Catcher in the Rye, J.D. Salinger, 1951"
#      "To Kill a Mockingbird, Harper Lee, 1960"
#      "1984, George Orwell, 1949"
#      "Moby-Dick, Herman Melville, 1851"
#      "Pride and Prejudice, Jane Austen, 1813"
'''
with open('Book-data.txt','w') as f:
    f.writelines(["The Catcher in the Rye, J.D. Salinger, 1951\n",'To Kill a Mockingbird, Harper Lee, 1960\n','1984, George Orwell, 1949\n','Moby-Dick, Herman Melville, 1851\n','Pride and Prejudice, Jane Austen, 1813\n'])
    
'''

# 2. Read the data from the file and store it in a variable.
f=open('Book-data.txt','r')
book_list=f.readlines()
print(book_list)
f.close()

#appending result in another list
f2=open("Result.txt",'a')
# f2.writelines(book_list)

# 3. Perform the following tasks on the data:
new_list=[]
for i in book_list:
   new_list.append(i.split(","))
#    1. Count the total number of books.
# f2.write(f'{'\n'}Total_number_of_Books {len(book_list)}')


#    2. Filter books that were published after 1950.
'''
f2.write("\n\nBooks published after 1950.\n")
for i in new_list:
    if int(i[-1].strip())>1950:
        f2.write(f'{i[0]} {i[-1]}')
 '''       


#    3. Sort the books alphabetically by title.
'''
f2.write('\nSort the books alphabetically by title.\n')
s=sorted(book_list)
for i in s:
    f2.write(i,)
'''


#    4. Sort the books by publication year in descending order.
'''
f2.write('\n-------------sorted books by publication year---------------\n')
p=sorted(new_list,key=lambda x:x[-1])
for i in p:
   f2.write(" ".join(i))
'''

print('-------------Oldest Book-----------------------------------')
#    5. Find the oldest book in the list.
'''
min=int(new_list[0][-1])
f2.write('------------------------Oldest Book-----------------------------------')
b=''
for i in new_list:
   if int(i[-1].strip())<min:
      min=int(i[-1].strip())
      b=" ".join(i)
f2.write(f'Oldest Book: {b}')
'''


#    6. Find the most recent book in the list.
'''
f2.write('\n-------------Most recent book----------------')
max=0
b=''
for i in new_list:
   if int(i[-1].strip())>max:
      max=int(i[-1].strip())
      b=" ".join(i)
f2.write(f'{'\n'} Most recent book :{b}')  
'''


#    7. Find books written by a specific author (e.g., 'Harper Lee').
'''
f2.write("\n-----------------Book written by specifc author----------------\n")
for i in new_list:
   if i[1].strip()=='Harper Lee':
      f2.write(f'Harper Lee Books: {i[0]}')
'''


#    8. Count how many books are written by the same author.
'''
f2.write('\n-----------------numbers  books writeen by same author-------------')
boks_count=[]
for i in new_list:
   boks_count.append(i[1].strip())
d={i:boks_count.count(i) for i in boks_count}
print(d)
for k,v in d.items():
   f2.write(f'{'\n'}{k}: {v}')
'''
   

#    9. Generate a list of book titles only.
'''
f2.write("\n---------------Books Titles-------------------")
for i in new_list:
   f2.write(f"{'\n'} {i[0].strip()}")
'''
#    10. Count how many books have more than one word in their title.
'''
f2.write("\n--------------Books Having length more than 1 word--------------")
c=0
for i in new_list:
   n=i[0].strip().split(" ")
   if len(n)>1 or '-' in i[0]:
      c+=1
f2.write(f'{'\n'}Count: {c}')
'''

# 4. Store the final data in a new file (e.g., 'processed_books.txt').
'''
f3=open('processed_books.txt','w')
with open('Result.txt','r')as f2:
 while(True):
   data=f2.readline()
   if data=='':
      break
   else:
      f3.write(f'{'\n'} {data}')

'''

f2.close()#closing result file
# 5. Delete the original file after processing.
'''
import os
os.remove('Result.txt')
'''