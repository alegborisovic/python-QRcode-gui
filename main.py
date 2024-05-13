# Created by Emre Aydemir.
# 14.05.2024
# www.emreaydemir.com.tr

import customtkinter as ctk
from tkinter import filedialog, messagebox
import qrcode
from PIL import ImageTk


def create_qr():
    data = url_entry.get()  # URL veya istediğiniz metni kullanıcıdan alıyoruz.
    if not data:
        messagebox.showinfo("Bilgi", "Lütfen bir URL veya metin giriniz.")
        return

    path = filedialog.asksaveasfilename(defaultextension='.png',
                                        filetypes=[("PNG files", "*.png")],
                                        initialdir="/Users/olegborisov/Desktop/qr_codes")  # Kaydetme yolu seçtiriyoruz.
    if not path:
        messagebox.showinfo("Bilgi", "Kaydetme yolu seçilmedi.")
        return

    # QR kodu oluşturma
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(path)

    # Kaydedilen QR kodunu göstermek için
    image = ImageTk.PhotoImage(img)
    image_label.config(image=image)
    image_label.image = image  # Referansı tutuyoruz, yoksa gözükmeyebilir.

    messagebox.showinfo("Başarılı", "QR Kod başarıyla kaydedildi!")


root = ctk.CTk()
root.geometry("750x450")
root.title("QR Kod Oluşturucu")

title_label = ctk.CTkLabel(root, text="QR Kod Oluşturucu", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20))

url_entry = ctk.CTkEntry(root, placeholder_text="Buraya bir URL veya metin girin")
url_entry.pack(fill="x", padx=20, pady=10)

create_button = ctk.CTkButton(root, text="QR Kod Oluştur", command=create_qr)
create_button.pack(pady=20)

image_label = ctk.CTkLabel(root)  # QR Kodunun gösterileceği yer
image_label.pack(pady=(10, 0))

root.mainloop()