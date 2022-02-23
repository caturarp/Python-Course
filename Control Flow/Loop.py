# For

# Print 'Dicoding' characters
for huruf in 'Dicoding':  
    print('Huruf: {}'.format(huruf))

# Print what's inside flowers[]
flowers = ['mawar', 'melati', 'anggrek']
for flower in flowers:  
    print('Flower: {}'.format(flower))

# Print what's inside flowers[] based on the length of the flowers[]
flowers = ['mawar', 'melati', 'anggrek']
for index in range(len(flowers)): 
    print('Flowers: {}'.format(flowers[index]))

# While

count = 0
while (count < 7):
    print('Hitungannya adalah: {}'.format(count))
    count = count + 1

# var = 1
# while var == 1:  # This constructs an infinite loop
#     num = input('Masukkan angka: ')
#     print('Anda memasukkan angka: {}'.format(num))
 
 
# while True:  # This constructs an infinite loop
#     num = input('Masukkan angka: ')
#     print('Anda memasukkan angka: {}'.format(num))

# Nested loop

for i in range(0, 6):
    for j in range(0, 6 - i):
        print('*', end='')
    print()
# ******
# *****
# ****
# ***
# **
# *