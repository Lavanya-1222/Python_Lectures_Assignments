# write in a File 

# f=open('abc.txt','a')
# f.write("Lavanya")
# f.close()

# f=open('abc.txt','r')
# print(f.read())


print('----------readline()--------------')
with open('abc.txt','r') as f:
   p=f.readline()
print(p)


print('----------readlines()-------------------')
f=open('abc.txt','r')
p=f.readlines()
print(p)
print()


print('----------with index----------------------')
# line=f.readlines()
print(p[2])