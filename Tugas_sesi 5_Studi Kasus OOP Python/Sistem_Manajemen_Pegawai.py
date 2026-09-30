# ============================================================
# TUGAS STUDI KASUS OOP PYTHON
# ============================================================
# Kasus 03 : Multiple Inheritance - Sistem Manajemen Pegawai
# ============================================================
# KASUS 03 - MULTIPLE INHERITANCE
# SISTEM MANAJEMEN PEGAWAI
# ============================================================


class Pegawai:
    def __init__(self, id_pegawai, nama):
        self.id_pegawai = id_pegawai
        self.nama = nama



class Gaji:
    def __init__(self, gaji):
        self.gaji = gaji


class PegawaiProyek:
    def __init__(self, nama_proyek):
        self.nama_proyek = nama_proyek


class ProjectManager(Pegawai, Gaji, PegawaiProyek):
    def __init__(self, id_pegawai, nama, gaji, nama_proyek):
        Pegawai.__init__(self, id_pegawai, nama)
        Gaji.__init__(self, gaji)
        PegawaiProyek.__init__(self, nama_proyek)

        self.peran = "Project Manager"

   
    def tampilkan_data(self):
        print("ID Pegawai :", self.id_pegawai)
        print("Nama       :", self.nama)
        print("Gaji       : Rp{:,.0f}".format(self.gaji))
        print("Proyek     :", self.nama_proyek)
        print("Peran      :", self.peran)


manager1 = ProjectManager(
    "PM001",
    "Rina Putri",
    8500000,
    "Sistem Informasi Akademik"
)

print("\n" + "=" * 55)
print("KASUS 03 - SISTEM MANAJEMEN PEGAWAI")
print("=" * 55)

manager1.tampilkan_data()

print("\nProgram selesai.")
