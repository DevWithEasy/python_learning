"""
#write file

f = open('a.text','w')
f.write('Python is really awesome')
f.close()

# appending

f = open('a.text','a')
f.write('. I love Javascript.')
f.close()

#read file
f = open('a.text', 'r')
info = f.read()
# info = f.read(20)
print(info)
f.close()

#read and write

f = open('a.text', 'w+')
f.write('All lost !')
f.close()

"""