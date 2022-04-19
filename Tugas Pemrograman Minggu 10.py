# Nomor 1 

kalimat = input("Masukkan Kalimat > ")
pemisah = kalimat.split()
panjang = len(pemisah)

for i in range (panjang):
    if (i == 0 or i % 2 == 0):
        pemisah[i]=pemisah[i].lower()
    elif (i % 2 != 0):
        pemisah[i]=pemisah[i].upper()

print("Output : ",end="")
for j in (pemisah):
    print(j,end=" ")
print("""
""")
    
# Nomor 2

print("Daftar Perintah \n1. Tambah\n2. Sisip\n3. Buang")
masukan = input("Masukkan Perintah > ")

pisah = masukan.split()
angka = [1, 3, 5]
perintah = pisah[0].upper()
batas = len(angka)-1
Error = "Perintah tidak dapat dieksekusi !"

if (len(pisah) == 2):
    if perintah == "TAMBAH":
        nilai = pisah[1]
        if nilai.isnumeric():
            nilai = int(nilai)
            angka.append(nilai)
        elif nilai.isalpha():
            nilai = nilai.capitalize()
            angka.append(nilai)
        else :
            angka = Error
    elif perintah == "BUANG":
        letak = pisah[1]
        if letak.isnumeric():
            letak = int(letak)
        else :
            angka = Error
        if (letak > batas):
            angka = Error
        else :
            angka.pop(letak)
    else :
        angka = Error
elif (len(pisah) == 3):
    if perintah == "SISIP":
        letak = pisah[1]
        if letak.isnumeric():
            letak = int(letak)
        else :
            angka = Error

        nilai = pisah [2]
        if nilai.isnumeric():
            nilai = int(nilai)
        elif nilai.isalpha():
            nilai = nilai.capitalize()
        else:
            angka = Error
        
        if (letak > batas):
            angka = Error
        else :
            angka.insert(letak,nilai)
    else :
        angka = Error
else :
     angka = Error

print("Output : ",angka)
input()