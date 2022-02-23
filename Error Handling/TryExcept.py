# Error handling works so that there's no  crash in running process
# below program will print something if there's zerodivisionerror
z = 0
try:
  x = 1 / z
  print(x)
except ZeroDivisionError:
  print('tidak bisa membagi angka dengan nilai nol')

# below program will print something if there's filenotfounderror
try:
    with open('contoh_tidak_ada.py') as file:                   
         print(file.read())                          
except (FileNotFoundError, ):
    print('file tidak ditemukan') # file tidak ditemukan