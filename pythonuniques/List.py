x = [5, 10, 15, 20, 25, 30, 35, 40]
print(x[3])
print(x[-1])
print(x[2:6])
print(x[:6])
print(x[-3:])
print(x[1:6:2])

# Change list value is possible in py
x[3] = 4
print(x[3])

# Easiness of unit delete
del(x[3])
print(x[3])

# Mutable and Unmuteable
s = "Hello World!"
print(s[4])  # ambil karakter kelima dari string s
print(s[6:11])  # ambil karakter ketujuh hingga sebelas dari string s
# s[5] = "d"  # ubah karakter keenam dari string
# s menjadi "d", seharusnya gagal karena immutable
# ubah isi string s menjadi "Halo Dunia!", seharusnya berhasil karena mutable
s = "Halo Dunia!"
print(s)

# Tuple(imuteable form of list)
t = (5, 'program', 1+3j)
print(t)
print(t[1])
print(t[0:3])  # Bisa slicing
# print(t[0]=10) # error because of imuteable
