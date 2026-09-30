# ============================================================
# TUGAS STUDI KASUS OOP PYTHON
# ============================================================
# Kasus 02 : Inheritance - Sistem Rental Kendaraan
# ============================================================
# KASUS 02 - INHERITANCE
# SISTEM RENTAL KENDARAAN
# ============================================================

class Kendaraan:
    def __init__(self, nama, merk, tahun, kecepatan):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

    def tampilkan_info(self):
        print("Nama       :", self.nama)
        print("Merk       :", self.merk)
        print("Tahun      :", self.tahun)
        print("Kecepatan  :", self.kecepatan, "km/jam")



class Mobil(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, jumlah_kursi):
        super().__init__(nama, merk, tahun, kecepatan)
        self.jumlah_kursi = jumlah_kursi

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Jumlah kursi:", self.jumlah_kursi)



class Motor(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, tipe_motor):
        super().__init__(nama, merk, tahun, kecepatan)
        self.tipe_motor = tipe_motor

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Tipe motor :", self.tipe_motor)


mobil1 = Mobil("Avanza", "Toyota", 2023, 180, 7)
mobil2 = Mobil("Civic", "Honda", 2024, 200, 5)

motor1 = Motor("NMAX", "Yamaha", 2023, 130, "Matic")
motor2 = Motor("CBR", "Honda", 2024, 150, "Sport")

armada = [mobil1, mobil2, motor1, motor2]

print("\n" + "=" * 55)
print("KASUS 02 - SISTEM RENTAL KENDARAAN")
print("=" * 55)

for kendaraan in armada:
    kendaraan.tampilkan_info()
    print("-" * 55)


