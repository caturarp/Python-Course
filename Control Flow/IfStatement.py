# if, elif, and else
kelerengku = 9
if kelerengku > 12:
    print("Jumlah kelereng banyak")
    print(kelerengku)
elif kelerengku > 8:
    print("cukup")
else:
    print("sedikit " + str(kelerengku))

# Normal If Else
lulus = True
if (lulus):
    kata = "selamat"
else:
    kata = "“perbaiki”"
print(kata)

# Ternary form

    # condition_if_true if the_condition else condition_if_false
    # Tuple Ternary
    # (condition_if_false, condition_if_true)[the_condition]

lulus2 = False
kata2 = "selamat" if lulus2 else "ga hoki"
print(kata2)
