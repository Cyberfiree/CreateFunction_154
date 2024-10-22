#materi baru
#anonymous function yg berfungsi sebagai fungsi kecil/fungsi pengganti , praktikum hari ini ngikut program

import math #Library untuk operasi matematika

luas_lingkaran = lambda r: math.pi * r*r # Mendefinisikan fungsi lambda untuk menghitung luas lingkaran
#lambda r - mendefinisikan fungsi kecil/anonim yang menerima parameter r (jari-jari)
#math.pi - Konstanta yang mewakili nilai π (pi), sekitar 3.14159, digunakan dalam perhitungan lingkaran.
#r * r - Menghitung kuadrat dari r (jari-jari), yaitu r kuadrat 2

#contoh penggunaannya
jari_jari = 7 # Jari-jari lingkaran
area = luas_lingkaran(jari_jari) # Menghitung luas lingkaran menggunakan fungsi lambda
#area - Variabel untuk menyimpan hasil perhitungan luas lingkaran.

print(f"Luas Lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}")  # Mencetak hasil luas lingkaran
#f - Merujuk pada f-string, memungkinkan penyisipan nilai variabel ke dalam string dengan {} / untuk spasi.