# upper() and lower() used for Uppercase-ing value(string) and vice-versa

# upper()
kata = 'dicoding'
kata = kata.upper()
print(kata) # DICODING

#lower()
kata = kata.lower()
print(kata) # dicoding

# strip(), rstrip() and lstrip() used for removing whitespace in string
# rstrip itself stands for right-strip and left-strip for lstrip

print('Dicoding    '.rstrip()) # Dicoding
print('    Dicoding'.lstrip()) # Dicoding
print('    Dicoding    '.strip()) # Dicoding

# Another usage of strip() is to remove certain character / word
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip('Code')) # Dicoding

# startswith() returned true if some string starts with declared value
# endswith() is the exact opposite

print('Dicoding Indonesia'.startswith('Dicoding')) # True

print('Dicoding Indonesia'.endswith('Indonesia')) # True

# join() join 2+ strings
print(' '.join(['Dicoding', 'Indonesia', '!'])) # Dicoding Indonesia !

# split() for spliting 
print('Dicoding Indonesia !'.split()) # ['Dicoding', 'Indonesia', '!']

# replace() for replace certain value with another value
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman")) # Ayo belajar pemrograman di Dicoding

# use the next parameters in replace as a counter how much you want to replace
string = "Ayo belajar Coding di Dicoding karena Coding adalah bahasa masa depan"
print(string.replace("Coding", "Pemrograman", 1)) # Ayo belajar Pemrograman di Dicoding karena Coding adalah bahasa masa depan

# isupper() for checking is string an uppercase, while lowercase() is the opposite
kata = 'DICODING'
kata.isupper() # True
kata = 'Dicoding'
kata.isupper() # False

# Alphabet checker

# while True:
#     print('Masukkan nama Anda:')
#     name = input()
#     if name.isalpha():
#         print("Halo", name)
#         break
#     print('Masukkan nama Anda dengan benar.')

# zfill() used for adding something inside a value

# Contoh 1: Penggunaan zfill 5 pada angka satuan
angka = 5
print (str(angka).zfill(5)) #00005
# Contoh 2: Penggunaan zfill 5 pada angka ratusan
angka = 300
print (str(angka).zfill(5)); #00300
# Contoh 3: Penggunaan zfill 5 pada angka desimal negatif (memiliki koma)
angka = -0.45
print (str(angka).zfill(5)); # -0.45
# Contoh 4: Penggunaan zfill 7 pada angka desimal negatif (memiliki koma)
angka = -0.45
print (str(angka).zfill(7)); # -000.45




