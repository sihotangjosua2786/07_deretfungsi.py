
def hitung_suku_ke_n(awal, beda, n):
    return awal + ((n - 1) * beda)


def tampilkan_deret(awal, beda, jumlah):

    for i in range(jumlah):
        suku = awal + (i * beda)
        print(suku, end=" ")


print("PROGRAM DERET ARITMETIKA DENGAN FUNGSI")

awal = int(input("Suku pertama : "))
beda = int(input("Beda         : "))
jumlah = int(input("Jumlah suku  : "))

print("\nDeret Aritmetika:")
tampilkan_deret(awal, beda, jumlah)

suku_terakhir = hitung_suku_ke_n(awal, beda, jumlah)

print("\nSuku ke-", jumlah, "=", suku_terakhir)