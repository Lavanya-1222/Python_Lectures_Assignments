# f=open('abc.txt','r')
# print(f.read())
# # output:
# lavanya
# samarth

# f1=open('abc.txt','w')# if file exixts then it will overitten
# # # print(f.read())# gives you error not readable
# f1.write('lavanya')
# f1.write('\nsamarth')
# f1.close()

f2=open('abc.txt','a')
f2.write("\nthis is new append line")

f3=open('image.jpeg','rb')
f3.read()

# f4=open('abc.txt','r+')
# print(f4.readlines())
# f4.write("\nthis is read write mode")
# print(f4.readlines())

f4=open('abc.txt','w+')
print(f4.read())
f4.write("This is write read code")
f4.read()


