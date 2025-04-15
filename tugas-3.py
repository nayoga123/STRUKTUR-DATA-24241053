def fibonacci(jumlah):
    a, b = 1, 2
    hasil = []
    for _ in range(jumlah):
        hasil.append(a)
        a, b = b, a + b
    return hasil

# Input jumlah deret
jumlah = int(input("Masukkan jumlah deret: "))

# Cetak hasil deret Fibonacci
deret = fibonacci(jumlah)
print("Deret Fibonacci:")
print(" ".join(map(str, deret)))