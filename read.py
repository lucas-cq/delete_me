filename = input('Enter a file name: ')
try: 
    fileopen = open(filename)
except:
    print('File name ' + str(filename) + ' could not be found')
    quit()

count = 0
for line in fileopen :
    if line.startswith('  .then') :
        count = count + 1
print('There were', count, 'strings that started with .then')