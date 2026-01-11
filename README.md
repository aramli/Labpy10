# Praktikum 10
Tugas Project Ujian Akhir Semester Pemrograman Dasar Pertemuan Ke 16 <br>

NAMA    : Andi Ramli Hidayat <br>
NIM     : 312510385 <br>
KELAS   : TI.25 C.5

# Program Penghitungan Pajak PPh21
<ul>
  <li>Program</li>
  <img src="https://github.com/aramli/labpy10/raw/main/img/1.png" width="750"/>
  <img src="https://github.com/aramli/labpy10/raw/main/img/2.png" width="750"/>
  <img src="https://github.com/aramli/labpy10/raw/main/img/3.png" width="750"/>
  <li>Hasil Program</li>
  <img src="https://github.com/aramli/labpy10/raw/main/img/4.png" width="750"/><br>
  <img src="https://github.com/aramli/labpy10/raw/main/img/5.png" width="750"/><br>
  <img src="https://github.com/aramli/labpy10/raw/main/img/6.png" width="750"/><br>
  
  <li>Penjelasan Kode</li>
  <img src="https://github.com/aramli/labpy10/raw/main/img/7.png" width="850"/><br>
  1. Pertama-tama, Kode berfungsi mendefinisikan class Employee yang berfungsi sebagai wadah data karyawan. Fungsi __init__ digunakan sebagai constructor, yaitu fungsi yang otomatis dijalankan ketika objek baru dibuat. Parameter yang diterima adalah NIK, nama, gaji bulanan, THR, bonus, dan PTKP. Semua data tersebut disimpan ke dalam atribut objek menggunakan kata kunci self. Dengan cara ini, setiap objek karyawan akan memiliki data lengkap yang bisa diproses lebih lanjut.

<br><br>

 <img src="https://github.com/aramli/labpy10/raw/main/img/8.png" width="850"/><br>
  2. Selanjutnya, Class TaxCalculator berfungsi untuk melakukan perhitungan pajak. Objek karyawan yang dibuat dari class Employee akan diterima sebagai parameter emp, lalu disimpan ke dalam atribut self.emp. Dengan begitu, semua data karyawan bisa digunakan dalam perhitungan.
<br><br>

<img src="https://github.com/aramli/labpy10/raw/main/img/9.png" width="850"/><br>
  3. Kemudian, Fungsi ini menghitung penghasilan tahunan karyawan. Rumusnya adalah gaji bulanan dikali 12, kemudian ditambah THR dan bonus. Hasilnya berupa total penghasilan setahun.
<br><br>

<img src="https://github.com/aramli/labpy10/raw/main/img/10.png" width="850"/><br>
  4. Lalu, Fungsi ini menghitung PKP (Penghasilan Kena Pajak). Caranya adalah mengurangi penghasilan tahunan dengan PTKP. Fungsi max(0, …) digunakan agar hasil tidak negatif. Jika penghasilan lebih kecil dari PTKP, maka PKP dianggap nol.

<br><br>

<img src="https://github.com/aramli/labpy10/raw/main/img/11.png" width="850"/><br>
  5. Lalu, Fungsi ini menghitung pajak tahunan berdasarkan tarif progresif. Jika PKP kurang dari atau sama dengan 60 juta, dikenakan tarif 5%. Jika PKP antara 60 juta hingga 250 juta, maka 60 juta pertama dikenakan 5% dan sisanya 15%. Jika PKP lebih dari 250 juta, maka ada tambahan tarif 25% untuk sisanya.
<br><br>

<img src="https://github.com/aramli/labpy10/raw/main/img/12.png" width="850"/><br>
  6. Kemudian, Fungsi ini menghitung persentase pajak dari total penghasilan tahunan. Rumusnya adalah pajak dibagi penghasilan lalu dikali seratus persen. Dengan cara ini, kita bisa mengetahui berapa persen penghasilan yang dipotong untuk pajak.
<br><br>

<img src="https://github.com/aramli/labpy10/raw/main/img/13.png" width="850"/><br>
  7. Selanjutnya, Class TaxView bertugas menampilkan hasil perhitungan pajak. Fungsi show menerima objek karyawan, lalu membuat objek TaxCalculator untuk melakukan perhitungan. Hasil yang ditampilkan berupa NIK, nama, gaji tahunan, PTKP, PKP, pajak, dan persentase pajak. Format angka menggunakan tanda pemisah ribuan agar lebih rapi. Tampilan dibuat menyerupai tabel sederhana sehingga mudah dibaca.
<br><br>

<img src="https://github.com/aramli/labpy10/raw/main/img/14.png" width="850"/><br>
  8. Lalu, Bagian main adalah inti program. Program menggunakan perulangan while True agar bisa menghitung pajak berkali-kali. Pertama, program meminta input NIK dan nama lengkap karyawan.
<br><br>

<img src="https://github.com/aramli/labpy10/raw/main/img/15.png" width="850"/><br>
  9. Berikutnya, Program meminta input gaji bulanan, THR, dan bonus. Semua input ini divalidasi agar harus berupa angka. Jika pengguna salah mengetik, misalnya huruf, maka program akan menampilkan pesan error dan kembali meminta input.
<br><br>

<img src="https://github.com/aramli/labpy10/raw/main/img/15.png" width="850"/><br>
  10. Selanjutnya, Program menampilkan tabel pilihan PTKP. Pengguna cukup memilih huruf A sampai H sesuai status perkawinan dan jumlah tanggungan. Input huruf otomatis diubah menjadi huruf besar agar konsisten.
<br><br>

<img src="https://github.com/aramli/labpy10/raw/main/img/16.png" width="850"/><br>
  11. Lalu, Dictionary ini menyimpan nilai PTKP sesuai pilihan. Misalnya, jika pengguna memilih A, maka PTKP otomatis bernilai 54 juta. Jika memilih H, maka PTKP bernilai 72 juta.
<br><br>

<img src="https://github.com/aramli/labpy10/raw/main/img/17.png" width="850"/><br>
  12. Kemudian, Jika pengguna salah memasukkan huruf, program akan menampilkan pesan error. Ini bagian dari validasi input.
<br><br>

<img src="https://github.com/aramli/labpy10/raw/main/img/18.png" width="850"/><br>
  13. Selanjutnya, Program menampilkan tabel pilihan PTKP. Pengguna cukup memilih huruf A sampai H sesuai status perkawinan dan jumlah tanggungan. Input huruf otomatis diubah menjadi huruf besar agar konsisten.
<br><br>

<img src="https://github.com/aramli/labpy10/raw/main/img/19.png" width="850"/><br>
  14. Lalu, Dictionary ini menyimpan nilai PTKP sesuai pilihan. Misalnya, jika pengguna memilih A, maka PTKP otomatis bernilai 54 juta. Jika memilih H, maka PTKP bernilai 72 juta.
<br><br>

<img src="https://github.com/aramli/labpy10/raw/main/img/20.png" width="850"/><br>
  15. Kemudian, Jika pengguna salah memasukkan huruf, program akan menampilkan pesan error. Ini bagian dari validasi input.
<br><br>

<img src="https://github.com/aramli/labpy10/raw/main/img/21.png" width="850"/><br>
  16. Lalu, Setelah PTKP dipilih, program membuat objek karyawan dengan semua data yang sudah dimasukkan. Lalu memanggil TaxView.show() untuk menampilkan hasil rekap pajak.

<br><br>

<img src="https://github.com/aramli/labpy10/raw/main/img/22.png" width="850"/><br>
  17. Kemudian, Setelah hasil ditampilkan, program akan bertanya apakah mau menghitung lagi. Jika jawab “y”, program akan mengulang dari awal. Jika jawab “n”, program berhenti dan menampilkan pesan “Terimakasih telah menggunakan program ini.”
<br><br>

<img src="https://github.com/aramli/labpy10/raw/main/img/23.png" width="850"/><br>
  18. Terakhir, Bagian terakhir memastikan program berjalan dari fungsi main(). Ini adalah standar Python untuk menjalankan program utama.

<br><br>


