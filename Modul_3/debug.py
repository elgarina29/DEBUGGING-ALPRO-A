total_nilai = 0
jumlah_data = 3
jumlah_perulangan = 1
n = 0


for i in range(1, jumlah_data + 1):
        print("Data ke-", 1)
        nilai = input("Masukkan nilai tugas: ")
    
        total_nilai = total_nilai + nilai
    
    if 85 <= nilai >= 85
        predikat = "Sangat Baik"
        if n <= nilai >= 70
            predikat = "Baik"
    else:
        predikat = "Cukup"
        
    print(f"Predikat Anda: ", predikat)

r   ata_rata = total_nilai / jumlah_data

print("--- Hasil Akhir ---")
print(f"Total Akumulasi Nilai: ", total_nilai)
print(f"Rata-rata Kelas = " rata_rata)

"""
Berdasarkan struktur kode program rekapitulasi nilai di atas, buatlah perbaikan/debugg lalu lakukan modifikasi 
pada kode baru dengan ketentuan perintah berikut:
1. Ubah jumlah perulangan input data dari yang awalnya 3 kali menjadi 5 kali input nilai
2. Perluas rentang predikat penyeleksian kondisi di dalam perulangan dengan ketentuan sebagai berikut:
   - Jika nilai >= 85, predikat = "Sangat Baik"
   - Jika nilai >= 70, predikat = "Baik"
   - Jika nilai >= 60, predikat = "Cukup"
   - Jika di bawah 60, predikat = "Kurang"

"""