from geometri.bangun_ruang import BangunRuang


class Segitiga(BangunRuang):
    def __init__(self, a, t):
        self.a = a
        self.t = t

    def info(self):
        return f'Ini adalah object dari Segitiga dengan alas = {self.a} dan tinggi = {self.t}'

    def hitung_luas(self):
        return self.a * self.t / 2
