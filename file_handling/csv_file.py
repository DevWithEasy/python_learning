import csv

"""
#Read csv file

file = open('example.csv')

file_reader = csv.reader(file)

for row in file_reader :
    print(str(file_reader.line_num), ' : ', str(row))

"""
#write csv file

file = open('example.csv', 'w', newline='')
file_writer = csv.writer(file)
#file_writer = csv.writer(file,delimiter = '.')
file_writer.writerow(['Bangladesh','BD'])
file_writer.writerow(['India','IND'])
file.close()