# range() as declared with its name

for i in range(5):
    print(i) # 0\n1\n2\n3\n4\n5

# range(n, p)
# starts from n, end before 1 value p

for i in range(1, 11):
    print(i) # 0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10

# range(n, p, q)
# q stands for difference in value

print([_ for _ in range(0,20,5)]) # [0, 5, 10, 15]


# in and not in 

kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat) # True
print('tidak' in kalimat) # false
print('Dicoding' not in kalimat) # false
print('tidak' not in kalimat) # true

# set up value from list or set 
# js form => data = [req.data.body]

data = ['shirt', 'white', 'L'] # From List
apparel, color, size = data
data = ('shirt', 'white', 'L')  # From Tuple
apparel, color, size = data

# sort

angka = [100, 1000, 500, 200, 5]
angka.sort()
print(angka) # [5, 100, 200, 500, 1000]

# sort string based on alphabet
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()
print(kendaraan) #  ['helikopter', 'mobil', 'motor', 'pesawat']

#reverse
kendaraan.sort(reverse=True)
print(kendaraan) # ['pesawat', 'motor', 'mobil', 'helikopter']



