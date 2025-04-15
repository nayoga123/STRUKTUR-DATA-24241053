# Input jumlah deret
jumlah = int(input("Masukkan jumlah deret bilangan genap: "))

# Membuat dan menampilkan deret bilangan genap
print("Output:")
for i in range(1, jumlah + 1):
    print(i * 2, end=", ")