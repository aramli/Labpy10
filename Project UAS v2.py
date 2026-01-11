# ===== Class Data =====
class Employee:
    def __init__(self, nik, name, salary, thr, bonus, ptkp):
        self.nik = nik
        self.name = name
        self.salary = salary
        self.thr = thr
        self.bonus = bonus
        self.ptkp = ptkp

# ===== Class Process =====
class TaxCalculator:
    def __init__(self, emp):
        self.emp = emp

    def annual_income(self):
        return (self.emp.salary * 12) + self.emp.thr + self.emp.bonus

    def taxable_income(self):
        return max(0, self.annual_income() - self.emp.ptkp)

    def annual_tax(self):
        pkp = self.taxable_income()
        if pkp <= 60000000:
            return pkp * 0.05
        elif pkp <= 250000000:
            return (60000000 * 0.05) + ((pkp - 60000000) * 0.15)
        else:
            return (60000000 * 0.05) + (190000000 * 0.15) + ((pkp - 250000000) * 0.25)

    def tax_percentage(self):
        income = self.annual_income()
        tax = self.annual_tax()
        if income == 0:
            return 0
        return (tax / income) * 100

# ===== Class View =====
class TaxView:
    @staticmethod
    def show(emp):
        calc = TaxCalculator(emp)
        print("\n==================== Rekap Pajak =====================")
        print(f"  NIK                   : {emp.nik}           ")
        print(f"  Nama                  : {emp.name}          ")
        print(f"  Gaji Tahunan          : Rp. {calc.annual_income():,}")
        print(f"  PTKP                  : RP. {emp.ptkp:,}")   
        print(f"  PKP                   : Rp. {calc.taxable_income():,}")
        print(f"  Pajak                 : Rp. {calc.annual_tax():,}")
        print(f"  Persentase Pajak      : {calc.tax_percentage():.2f}%")
        print(f"=======================================================")

# ===== Main =====
def main():
    while True:  # perulangan agar bisa menghitung lagi
        try:
            # Input data karyawan
            nik = input("Nomor Karyawan: ")
            name = input("Nama Lengkap: ")

            # Validasi input angka untuk gaji, THR, dan bonus
            try:
                salary = int(input("Gaji bulanan: "))
            except ValueError:
                print("Error: Gaji bulanan harus berupa angka!")
                continue

            try:
                thr = int(input("THR: "))
            except ValueError:
                print("Error: THR harus berupa angka!")
                continue

            try:
                bonus = int(input("Bonus: "))
            except ValueError:
                print("Error: Bonus harus berupa angka!")
                continue

            # Pilihan PTKP
            print("\n Silahkan Pilih Type PTKP (Penghasilan Tidak Kena Pajak):")
            print("______________________________________________________________")
            print("|Opsi|              Keterangan               |   Jumlah PTKP  |")
            print("|____|_______________________________________|________________|")
            print("| A. | TK/0 (Tidak Kawin, tanpa tanggungan)  | Rp. 54,000,000 |")
            print("| B. | TK/1 (Tidak Kawin, 1 Tanggungan)      | Rp. 58,500,000 |")
            print("| C. | TK/2 (Tidak Kawin, 2 Tanggungan)      | Rp. 63,000,000 |")
            print("| D. | TK/3 (Tidak Kawin, 3 Tanggungan)      | Rp. 67,500,000 |")
            print("| E. | K/0  (Kawin, tanpa tanggungan)        | Rp. 58,500,000 |")
            print("| F. | K/1  (Kawin, 1 tanggungan)            | Rp. 63,000,000 |")
            print("| G. | K/2  (Kawin, 2 tanggungan)            | Rp. 67,500,000 |")
            print("| H. | K/3  (Kawin, 3 tanggungan)            | Rp. 72,000,000 |")
            print("|____|_______________________________________|________________|")
            print("")

            pilihan = input("Masukkan Type PTKP (A/B/C/D/E/F/G/H): ").upper()

            ptkp_dict = {
                "A": 54000000,
                "B": 58500000,
                "C": 63000000,
                "D": 67500000,
                "E": 58500000,
                "F": 63000000,
                "G": 67500000,
                "H": 72000000
            }

            if pilihan not in ptkp_dict:
                print("Error: Pilihan PTKP tidak valid!")
                continue

            ptkp = ptkp_dict[pilihan]

            # Buat objek Employee
            emp = Employee(nik, name, salary, thr, bonus, ptkp)
            TaxView.show(emp)

            # Tanya apakah mau hitung lagi
            ulang = input("\nApakah mau menghitung lagi? (y/n): ").lower()
            if ulang != "y":
                print("Terimakasih telah menggunakan program ini.")
                break

        except Exception as e:
            print("Terjadi kesalahan:", e)


if __name__ == "__main__":
    main()
