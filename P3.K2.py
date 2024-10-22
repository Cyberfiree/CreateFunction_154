def konversisuhu(temperature, value): # Fungsi untuk mengonversi suhu dari Celsius ke Fahrenheit atau sebaliknya
    if value == 'C': # Jika nilai 'value' adalah 'C', artinya kita ingin mengonversi dari Fahrenheit ke Celsius
        temperaturesuhu = (temperature - 32) * 5/9 # Rumus konversi dari Fahrenheit ke Celsius
        return temperaturesuhu, 'C'  # Mengembalikan suhu yang telah dikonversi dan satuan 'C'
    else:
        temperaturesuhu = (temperature * 9/5) + 32 # Rumus konversi dari Celsius ke Fahrenheit
        return temperaturesuhu, 'F'  # Mengembalikan suhu yang telah dikonversi dan satuan 'F'

# Contoh konversi dari Celsius ke Fahrenheit
celsius_temperature = 30
temperaturesuhu, target_value = konversisuhu(celsius_temperature, 'F')
print(f"{celsius_temperature}°C dikonversikan ke Fahrenheit adalah {temperaturesuhu}°{target_value}") # Mencetak hasil konversi


# Contoh konversi dari Fahrenheit ke Celsius
fahrenheit_temperature = 86
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'C')
print(f"{fahrenheit_temperature}°F dikonversikan ke Celcius adalah {temperaturesuhu}°{target_value}") # Mencetak hasil konversi