# # f=open('xyz.txt','w')

# f=open('xyz.txt','a')
# f.write("\nHello world")
# f.write("\nHello world 2")
# f.write("\nHello world 3")
# f.write("\nHello world 4")

# with open('xyz.txt','r') as f:
#  p=f.readlines()
#  print(p)
#  p.insert(2,'I am in Pune')
#  print(p)


f1=open('lect.txt','w')
f2=open('lect2.txt','w')

# f2.write("Hello World\n")
# f2.write("Hello World2\n")
# f2.write("Hello World3\n")
# f2.write("Hello World4\n")
# f2.write("Hello World5\n")

with open('lect2.txt','r') as f2:
 print(f2.readline())
 p=f2.readlines()
 p.insert(2,'I am inserting line')

with open('lect2.txt','r') as f2:
 print(f2.readlines())