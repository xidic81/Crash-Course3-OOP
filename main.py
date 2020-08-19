from geometri.bangun_ruang import BangunRuang
from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga

print('Menggunakan OOP')
p1 = PersegiPanjang(10, 2)
print(p1.info())
print(p1.hitung_luas())

s1 = Segitiga(5, 3)
print(s1.info())
print(s1.hitung_luas())

print('\nMencoba membuat object dari kelas BangunRuang')
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())

# Polymorphism = kemampuan object untuk merespon berbeda, terhadap pemanggilan method yang sama
daftar_bangun_ruang = [p1, s1]

print('\nPolymorphism')
for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())
