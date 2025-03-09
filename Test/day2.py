#Integer
#Jika menuliskan 10000000, maka akan susah dibaca
#Sehingga bisa ditulis dengan seperti ini "1_000_000"
#Akan menghasilkan output yang sama

#Cara mengetahui tipe data
num_char = len(input("What is your name? "))
print(type(num_char))
# Hasilnya adalah <class 'int'> karena nilai dari num char adalah jumlah karakter dari inputan

#Cara mengubah tipe data
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
print(type(new_num_char))

#contoh lagi
print(70 + float("100.5"))


# Cara membulatkan angka (float)
print(round(8 / 3))
# Hasilnya adalah 3
print(round(8 / 3, 2))
# Hasilnya adalah 2.67, 2 berarti adalah 2 angka di belakang koma
print(8 // 3)
# Pembagian di atas merupakan pembagian floor, sehingga dibulatkan ke bawah yang akan mengeluarkan output berupa 2


#F string
score = 0
height = 1.8
isWinning = True

#cara biasa
print("Your score is " + str(score) + ", your height is " + str(height) + ", you are winning is " + str(isWinning))

#Jika menggunakan F-string
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
#F-string akan langsung mengubah semua tipe data menjadi string
