# ============================================================
# TUGAS STUDI KASUS OOP PYTHON
# ============================================================
# Kasus 01 : Class & Object - Sistem Pendataan Dosen
# ============================================================
# KASUS 01 - CLASS & OBJECT
# SISTEM PENDATAAN DOSEN
# ============================================================

class Dosen:
    def __init__(self, nidn, nama, prodi, fakultas):
        self.nidn = nidn
        self.nama = nama
        self.prodi = prodi
        self.fakultas = fakultas

    def cek_profil(self):
        print("\n--- PROFIL DOSEN ---")
        print("NIDN     :", self.nidn)
        print("Nama     :", self.nama)
        print("Prodi    :", self.prodi)
        print("Fakultas :", self.fakultas)

    def cek_prodi(self):
        daftar_prodi = [
            "Teknik Informatika",
            "Sistem Informasi",
            "Teknik Elektro",
            "Manajemen",
            "Akuntansi"
        ]

        if self.prodi in daftar_prodi:
            return f"Prodi '{self.prodi}' terdaftar."
        return f"Prodi '{self.prodi}' tidak terdaftar."


dosen1 = Dosen(
    "123456",
    "Budi Santoso",
    "Teknik Informatika",
    "Fakultas Teknologi Informasi"
)

dosen2 = Dosen(
    "1234567",
    "Siti Aminah",
    "Sistem Informasi",
    "Fakultas Teknologi Informasi"
)

dosen3 = Dosen(
    "12345678",
    "Andi Wijaya",
    "Manajemen",
    "Fakultas Ekonomi"
)

daftar_dosen = [dosen1, dosen2, dosen3]


def cari_dosen(nidn):
    """Mencari object Dosen berdasarkan NIDN."""
    for dosen in daftar_dosen:
        if dosen.nidn == nidn:
            return dosen
    return None


print("=" * 55)
print("KASUS 01 - SISTEM PENDATAAN DOSEN")
print("=" * 55)

print("\nDATA SELURUH DOSEN")
for dosen in daftar_dosen:
    dosen.cek_profil()
    print("Status prodi:", dosen.cek_prodi())
[]
print("\nCEK PROFIL BERDASARKAN NIDN")
nidn_input = input("Masukkan NIDN yang ingin dicek: ")

dosen_ditemukan = cari_dosen(nidn_input)

if dosen_ditemukan is not None:
    dosen_ditemukan.cek_profil()
    print("Status prodi:", dosen_ditemukan.cek_prodi())
else:
    print("NIDN tidak ditemukan.")


