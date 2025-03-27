print('-'*60)
file_one = open('file handling.txt','r')
for every_line in file_one:
    print(every_line)

print('-'*60)

file_two = open('file handling.txt','r')
print(file_two.read())

print('-'*60)

with open('file handling.txt') as file_three:
    print_file = file_three.read() 
    print(print_file)

print('-'*60)

file_four = open('file handling.txt','r')
print(file_four.read(8))

print('-'*60)

with open('file handling.txt','r') as file_five:
    print_data = file_five.read() 
    for each_line in print_data:
        print_data_2 = each_line.split()
        print(print_data_2)

print('*-'*60)

#write in files

file_six = open('file handling2.txt','w')
file_six.write('Soham Admires Walter White ')
file_six.write('From Here This Is Edited In w mode')
file_six.close()


with open('file handling2.txt','w') as file_seven:
    file_seven.write(' This is line is from file seven')
    file_seven.close()

with open ('file handling2.txt','a') as file_eight:
    file_eight.write(' This Line Appended To File Eight')
    file_eight.close()


print_write_file = open('file handling2.txt','r')
print(print_write_file.read())

