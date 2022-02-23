# Break
# Stopping loop
for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))  # Dico

# Continue
# Stopping current iteration and continue on to the next iteration
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))  # Dicoding

# # Else after for
# Used for exit if not found

# items = [1, 2, 3]
# for item in items:
#     if cari(item):
#         #ditemukan!
#         proses_item()
#         break
# else:
#     #Item tidak ditemukan
#     not_found_in_container()

# # Else after while
# else will be triggered every the while end.
n = 10
while n > 0:
    n = n - 1
    print(n)
else:
    print("Loop selesai")
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
# Loop selesai

# Pass
# Used for filling null function, because null function declared error by default
import sys
data=''
while(data!='exit'):
    try:
        data=input('Please enter an integer (type exit to exit): ')
        print('got integer: {}'.format(int(data)))
    except:
        if data == 'exit':
            pass  # exit gracefully without prompt any error
            # without pass will be error, because data is empty
        else:
            print('error: {}'.format(sys.exc_info()[0]))

# List Comprehension
# recycle the list for other purpose

#new_list = [expression for_loop_one_or_more conditions]

#Cara 1
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)

#Cara 2 List Comprehension
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)
