import tkinter as tk
from tkinter import messagebox

# Fungsi untuk login
def login_attempt(username, password, users_db):
    if username in users_db and users_db[username] == password:
        return True
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah")
        return False

# Fungsi untuk mengatur soal
class Soal:
    def __init__(self, pertanyaan, opsi, jawaban):
        self.pertanyaan = pertanyaan
        self.opsi = opsi
        self.jawaban = jawaban

# Kuis utama
class KuisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Kuis")
        self.root.geometry("600x400")
        self.root.configure(bg="lightblue")

        self.admin_soal = []  # Menyimpan soal-soal
        self.murid_jawaban = []  # Menyimpan jawaban murid
        self.users_db = {}  # Menyimpan username dan password

        self.main_menu()

    def main_menu(self):
        self.clear_window()
        self.create_header("Menu Utama")
        tk.Button(self.root, text="Registrasi Admin", font=("Arial", 14), command=self.registrasi_admin).pack(pady=10)
        tk.Button(self.root, text="Registrasi Murid", font=("Arial", 14), command=self.registrasi_murid).pack(pady=10)
        tk.Button(self.root, text="Login Sebagai Admin", font=("Arial", 14), command=self.admin_login).pack(pady=10)
        tk.Button(self.root, text="Login Sebagai Murid", font=("Arial", 14), command=self.murid_login).pack(pady=10)

    def admin_login(self):
        self.clear_window()
        self.create_header("Login Admin")
        self.create_login_form("admin")

    def murid_login(self):
        self.clear_window()
        self.create_header("Login Murid")
        self.create_login_form("murid")

    def create_login_form(self, role):
        tk.Label(self.root, text="Username:", font=("Arial", 12)).pack(pady=5)
        username_entry = tk.Entry(self.root, font=("Arial", 12))
        username_entry.pack(pady=5)
        tk.Label(self.root, text="Password:", font=("Arial", 12)).pack(pady=5)
        password_entry = tk.Entry(self.root, show="*", font=("Arial", 12))
        password_entry.pack(pady=5)

        def submit():
            username = username_entry.get()
            password = password_entry.get()
            if login_attempt(username, password, self.users_db):
                if role == "admin":
                    self.admin_panel()
                else:
                    self.murid_panel()

        tk.Button(self.root, text="Login", font=("Arial", 14), command=submit).pack(pady=10)

        # Tombol Kembali ke Menu Utama
        tk.Button(self.root, text="Kembali", font=("Arial", 14), command=self.main_menu).pack(pady=10)

    def registrasi_admin(self):
        self.clear_window()
        self.create_header("Registrasi Admin")
        self.create_registration_form("admin")

    def registrasi_murid(self):
        self.clear_window()
        self.create_header("Registrasi Murid")
        self.create_registration_form("murid")

    def create_registration_form(self, role):
        tk.Label(self.root, text="Username:", font=("Arial", 12)).pack(pady=5)
        username_entry = tk.Entry(self.root, font=("Arial", 12))
        username_entry.pack(pady=5)
        tk.Label(self.root, text="Password:", font=("Arial", 12)).pack(pady=5)
        password_entry = tk.Entry(self.root, show="*", font=("Arial", 12))
        password_entry.pack(pady=5)
        tk.Label(self.root, text="Konfirmasi Password:", font=("Arial", 12)).pack(pady=5)
        confirm_password_entry = tk.Entry(self.root, show="*", font=("Arial", 12))
        confirm_password_entry.pack(pady=5)

        def register():
            username = username_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()

            if password != confirm_password:
                messagebox.showerror("Error", "Password dan konfirmasi password tidak sama!")
                return

            if username in self.users_db:
                messagebox.showerror("Error", "Username sudah terdaftar!")
                return

            self.users_db[username] = password
            messagebox.showinfo("Registrasi Berhasil", f"Registrasi {role} berhasil!")
            self.main_menu()

        tk.Button(self.root, text="Daftar", font=("Arial", 14), command=register).pack(pady=10)

        # Tombol Kembali ke Menu Utama
        tk.Button(self.root, text="Kembali", font=("Arial", 14), command=self.main_menu).pack(pady=10)

    def admin_panel(self):
        self.clear_window()
        self.create_header("Admin Panel")
        tk.Button(self.root, text="Buat Soal", font=("Arial", 14), command=self.buat_soal).pack(pady=10)
        tk.Button(self.root, text="Edit Soal", font=("Arial", 14), command=self.edit_soal).pack(pady=10)
        tk.Button(self.root, text="Hapus Soal", font=("Arial", 14), command=self.hapus_soal).pack(pady=10)
        tk.Button(self.root, text="Logout", font=("Arial", 14), command=self.main_menu).pack(pady=10)

        # Tombol Kembali ke Menu Utama
        tk.Button(self.root, text="Kembali", font=("Arial", 14), command=self.main_menu).pack(pady=10)

    def murid_panel(self):
        self.clear_window()
        self.create_header("Murid Panel")
        tk.Button(self.root, text="Mengerjakan Soal", font=("Arial", 14), command=self.mengerjakan_soal).pack(pady=10)
        tk.Button(self.root, text="Lihat Nilai", font=("Arial", 14), command=self.lihat_nilai).pack(pady=10)
        tk.Button(self.root, text="Logout", font=("Arial", 14), command=self.main_menu).pack(pady=10)

        # Tombol Kembali ke Menu Utama
        tk.Button(self.root, text="Kembali", font=("Arial", 14), command=self.main_menu).pack(pady=10)

    def buat_soal(self):
        self.clear_window()
        self.create_header("Buat Soal Baru")
        tk.Label(self.root, text="Pertanyaan:", font=("Arial", 12)).pack(pady=5)
        pertanyaan_entry = tk.Entry(self.root, font=("Arial", 12))
        pertanyaan_entry.pack(pady=5)

        tk.Label(self.root, text="Opsi A:", font=("Arial", 12)).pack(pady=5)
        opsi_a_entry = tk.Entry(self.root, font=("Arial", 12))
        opsi_a_entry.pack(pady=5)
        tk.Label(self.root, text="Opsi B:", font=("Arial", 12)).pack(pady=5)
        opsi_b_entry = tk.Entry(self.root, font=("Arial", 12))
        opsi_b_entry.pack(pady=5)
        tk.Label(self.root, text="Opsi C:", font=("Arial", 12)).pack(pady=5)
        opsi_c_entry = tk.Entry(self.root, font=("Arial", 12))
        opsi_c_entry.pack(pady=5)
        tk.Label(self.root, text="Opsi D:", font=("Arial", 12)).pack(pady=5)
        opsi_d_entry = tk.Entry(self.root, font=("Arial", 12))
        opsi_d_entry.pack(pady=5)

        tk.Label(self.root, text="Jawaban (A/B/C/D):", font=("Arial", 12)).pack(pady=5)
        jawaban_entry = tk.Entry(self.root, font=("Arial", 12))
        jawaban_entry.pack(pady=5)

        def simpan_soal():
            pertanyaan = pertanyaan_entry.get()
            opsi = [opsi_a_entry.get(), opsi_b_entry.get(), opsi_c_entry.get(), opsi_d_entry.get()]
            jawaban = jawaban_entry.get().upper()

            if jawaban not in ["A", "B", "C", "D"]:
                messagebox.showerror("Error", "Jawaban harus A, B, C, atau D")
                return

            soal_baru = Soal(pertanyaan, opsi, jawaban)
            self.admin_soal.append(soal_baru)
            messagebox.showinfo("Berhasil", "Soal berhasil disimpan!")
            self.admin_panel()

        tk.Button(self.root, text="Simpan Soal", font=("Arial", 14), command=simpan_soal).pack(pady=10)

        # Tombol Kembali ke Panel Admin
        tk.Button(self.root, text="Kembali", font=("Arial", 14), command=self.admin_panel).pack(pady=10)

    def edit_soal(self):
        self.clear_window()
        self.create_header("Edit Soal")

        if not self.admin_soal:
            messagebox.showerror("Error", "Tidak ada soal yang tersedia untuk diedit.")
            self.admin_panel()
            return

        self.selected_soal_index = tk.IntVar()
        self.selected_soal_index.set(-1)

        for index, soal in enumerate(self.admin_soal):
            tk.Radiobutton(self.root, text=f"{index + 1}. {soal.pertanyaan}", variable=self.selected_soal_index, value=index,
                           font=("Arial", 12)).pack(anchor="w", pady=5)

        def edit_selected_soal():
            soal_index = self.selected_soal_index.get()
            if soal_index == -1:
                messagebox.showerror("Error", "Pilih soal yang akan diedit.")
                return

            soal = self.admin_soal[soal_index]
            self.edit_soal_form(soal, soal_index)

        tk.Button(self.root, text="Edit Soal", font=("Arial", 14), command=edit_selected_soal).pack(pady=10)

        # Tombol Kembali ke Panel Admin
        tk.Button(self.root, text="Kembali", font=("Arial", 14), command=self.admin_panel).pack(pady=10)

    def edit_soal_form(self, soal, soal_index):
        self.clear_window()
        self.create_header("Edit Soal")

        tk.Label(self.root, text="Pertanyaan:", font=("Arial", 12)).pack(pady=5)
        pertanyaan_entry = tk.Entry(self.root, font=("Arial", 12))
        pertanyaan_entry.insert(0, soal.pertanyaan)
        pertanyaan_entry.pack(pady=5)

        tk.Label(self.root, text="Opsi A:", font=("Arial", 12)).pack(pady=5)
        opsi_a_entry = tk.Entry(self.root, font=("Arial", 12))
        opsi_a_entry.insert(0, soal.opsi[0])
        opsi_a_entry.pack(pady=5)
        tk.Label(self.root, text="Opsi B:", font=("Arial", 12)).pack(pady=5)
        opsi_b_entry = tk.Entry(self.root, font=("Arial", 12))
        opsi_b_entry.insert(0, soal.opsi[1])
        opsi_b_entry.pack(pady=5)
        tk.Label(self.root, text="Opsi C:", font=("Arial", 12)).pack(pady=5)
        opsi_c_entry = tk.Entry(self.root, font=("Arial", 12))
        opsi_c_entry.insert(0, soal.opsi[2])
        opsi_c_entry.pack(pady=5)
        tk.Label(self.root, text="Opsi D:", font=("Arial", 12)).pack(pady=5)
        opsi_d_entry = tk.Entry(self.root, font=("Arial", 12))
        opsi_d_entry.insert(0, soal.opsi[3])
        opsi_d_entry.pack(pady=5)

        tk.Label(self.root, text="Jawaban (A/B/C/D):", font=("Arial", 12)).pack(pady=5)
        jawaban_entry = tk.Entry(self.root, font=("Arial", 12))
        jawaban_entry.insert(0, soal.jawaban)
        jawaban_entry.pack(pady=5)

        def update_soal():
            soal.pertanyaan = pertanyaan_entry.get()
            soal.opsi = [opsi_a_entry.get(), opsi_b_entry.get(), opsi_c_entry.get(), opsi_d_entry.get()]
            soal.jawaban = jawaban_entry.get().upper()

            if soal.jawaban not in ["A", "B", "C", "D"]:
                messagebox.showerror("Error", "Jawaban harus A, B, C, atau D")
                return

            self.admin_soal[soal_index] = soal
            messagebox.showinfo("Berhasil", "Soal berhasil diperbarui!")
            self.admin_panel()

        tk.Button(self.root, text="Simpan Perubahan", font=("Arial", 14), command=update_soal).pack(pady=10)

        # Tombol Kembali ke Panel Admin
        tk.Button(self.root, text="Kembali", font=("Arial", 14), command=self.admin_panel).pack(pady=10)

    def hapus_soal(self):
        self.clear_window()
        self.create_header("Hapus Soal")

        if not self.admin_soal:
            messagebox.showerror("Error", "Tidak ada soal yang tersedia untuk dihapus.")
            self.admin_panel()
            return

        self.selected_soal_index = tk.IntVar()
        self.selected_soal_index.set(-1)

        for index, soal in enumerate(self.admin_soal):
            tk.Radiobutton(self.root, text=f"{index + 1}. {soal.pertanyaan}", variable=self.selected_soal_index, value=index,
                           font=("Arial", 12)).pack(anchor="w", pady=5)

        def hapus_selected_soal():
            soal_index = self.selected_soal_index.get()
            if soal_index == -1:
                messagebox.showerror("Error", "Pilih soal yang akan dihapus.")
                return

            del self.admin_soal[soal_index]
            messagebox.showinfo("Berhasil", "Soal berhasil dihapus!")
            self.admin_panel()

        tk.Button(self.root, text="Hapus Soal", font=("Arial", 14), command=hapus_selected_soal).pack(pady=10)

        # Tombol Kembali ke Panel Admin
        tk.Button(self.root, text="Kembali", font=("Arial", 14), command=self.admin_panel).pack(pady=10)

    def mengerjakan_soal(self):
        self.clear_window()
        self.create_header("Mengerjakan Soal")
        self.murid_jawaban = []
        for index, soal in enumerate(self.admin_soal):
            tk.Label(self.root, text=f"{index + 1}. {soal.pertanyaan}", font=("Arial", 12)).pack(pady=5)
            jawaban_var = tk.StringVar()
            self.murid_jawaban.append(jawaban_var)  # Menyimpan variabel jawaban untuk setiap soal
            for idx, opsi in enumerate(soal.opsi):
                tk.Radiobutton(self.root, text=f"{chr(65 + idx)}. {opsi}", font=("Arial", 12), value=chr(65 + idx),
                               variable=jawaban_var).pack(anchor="w", pady=5)

        def submit_jawaban():
            correct_count = 0
            for idx, soal in enumerate(self.admin_soal):
                if self.murid_jawaban[idx].get() == soal.jawaban:
                    correct_count += 1
            score = (correct_count / len(self.admin_soal)) * 100
            messagebox.showinfo("Nilai", f"Nilai Anda: {score}%")

            # Rekursi: Menanyakan apakah murid ingin mencoba lagi setelah melihat hasil
            self.tanya_ulang_kuis()

        tk.Button(self.root, text="Kirim Jawaban", font=("Arial", 14), command=submit_jawaban).pack(pady=10)

        # Tombol Kembali ke Panel Murid
        tk.Button(self.root, text="Kembali", font=("Arial", 14), command=self.murid_panel).pack(pady=10)

    def tanya_ulang_kuis(self):
        # Fungsi rekursif untuk menanyakan apakah murid ingin mengulang kuis
        result = messagebox.askyesno("Coba Lagi?", "Apakah Anda ingin mencoba kuis lagi?")
        if result:
            self.mengerjakan_soal()  # Panggil lagi fungsi ini untuk memulai kuis dari awal
        else:
            self.murid_panel()  # Kembali ke panel murid jika tidak ingin mengulang

    def clear_window(self):
        # Menghapus semua widget dari window
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_header(self, title):
        # Menampilkan header pada jendela
        header = tk.Label(self.root, text=title, font=("Arial", 20), bg="lightblue")
        header.pack(pady=20)

# Menjalankan aplikasi GUI
root = tk.Tk()
app = KuisApp(root)
root.mainloop()

