import pyodbc
import customtkinter as ctk
from tkinter import ttk

# Veritabanı bağlantısını kur
def connect_to_db():
    try:
        conn = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=YOUR SERVER'  # Server adınız
            'DATABASE=İlacTakipSistemFinal;'  # Veritabanı adı
            'Trusted_Connection=yes;'  # Windows Authentication
        )
        return conn
    except pyodbc.Error as e:
        error_message = f"Bağlantı hatası: {e}"
        print(error_message)
        error_label.configure(text=error_message)  # Hata mesajını GUI'de göster
        return None

# Tablo verilerini al
def fetch_table_data(table_name):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            conn.close()
            return columns, rows
        except pyodbc.Error as e:
            error_message = f"Veri alma hatası: {e}"
            print(error_message)
            error_label.configure(text=error_message)  # Hata mesajını GUI'de göster
            conn.close()
    return [], []

# Tablo verilerini arayüzde göster
def show_data():
    selected_table = table_selector.get()
    if not selected_table:
        error_label.configure(text="Lütfen bir tablo seçin!")  # Hata mesajı
        return

    # Tablodaki verileri çek
    columns, rows = fetch_table_data(selected_table)

    if not columns:
        error_label.configure(text="Tablo verileri alınamadı!")  # Hata mesajı
        return

    # Eski verileri temizle
    treeview.delete(*treeview.get_children())

    # Sütunları ayarla
    treeview["columns"] = columns
    treeview["show"] = "headings"

    for col in columns:
        treeview.heading(col, text=col)
        treeview.column(col, width=150)

    # Satırları ekle
    for row in rows:
        treeview.insert("", "end", values=row)

    error_label.configure(text="")  # Hata mesajını temizle

# Ana pencere oluştur
app = ctk.CTk()
app.title("İlaç Takip Sistemi")
app.geometry("900x600")
app.configure(bg="white")  # Arka planı beyaz yap

# Başlık
title_label = ctk.CTkLabel(app, text="İlaç Takip Sistemi", font=("Arial", 24))  # Font büyütüldü
title_label.pack(pady=10)

# Tablo seçici
table_selector = ctk.CTkComboBox(app, values=[
    "dbo.Adres", "dbo.Eczane", "dbo.Email", "dbo.Ilac_Bilgi",
    "dbo.Ilac_Detay", "dbo.Musteri", "dbo.Recete",
    "dbo.Recete_Detay", "dbo.Telefon"
])
table_selector.pack(pady=10)

# Veri gösterme butonu
fetch_button = ctk.CTkButton(app, text="Verileri Göster", command=show_data)
fetch_button.pack(pady=10)

# Hata mesajı etiketi
error_label = ctk.CTkLabel(app, text="", text_color="red", font=("Arial", 14))  # Font büyütüldü
error_label.pack(pady=5)

# Treeview ile veri gösterimi
treeview_frame = ctk.CTkFrame(app)
treeview_frame.pack(expand=True, fill="both", padx=10, pady=10)

# Style for Treeview to increase font size
style = ttk.Style()
style.configure("Treeview", font=("Arial", 12))  # Set font for Treeview

# Style for Treeview headings to make them bigger
style.configure("Treeview.Heading", font=("Arial", 16, "bold"))  # Increase header font size and make it bold

treeview = ttk.Treeview(treeview_frame, style="Treeview")
treeview.pack(expand=True, fill="both")

# Uygulamayı çalıştır
app.mainloop()
