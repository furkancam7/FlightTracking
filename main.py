import tkinter as tk
from tkinter import messagebox


from PIL import Image, ImageTk
import requests


API_KEY = '180d2cdcb9376c51bfd7c393a0585879'



def get_flight_info():
    flight_number = entry_flight_number.get()

    if flight_number == "":
        messagebox.showerror("Hata", "Lütfen geçerli bir uçuş numarası girin.")
        return


    url = f'http://api.aviationstack.com/v1/flights?access_key={API_KEY}&flight_number={flight_number}'

    try:
        response = requests.get(url)
        flight_data = response.json()

        if 'data' in flight_data and len(flight_data['data']) > 0:
            flight = flight_data['data'][0]
            display_flight_info(flight)
        else:
            messagebox.showinfo("Bilgi", "Uçuş bilgisi bulunamadı!")
    except Exception as e:
        messagebox.showerror("Hata", f"Veri alınırken hata oluştu: {e}")



def display_flight_info(flight):
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, f"Uçuş Tarihi: {flight['flight_date']}\n")
    result_text.insert(tk.END, f"Uçuş Durumu: {flight['flight_status']}\n")
    result_text.insert(tk.END, f"Kalkış Havaalanı: {flight['departure']['airport']}\n")
    result_text.insert(tk.END, f"Kalkış Zamanı: {flight['departure']['scheduled']}\n")
    result_text.insert(tk.END, f"Varış Havaalanı: {flight['arrival']['airport']}\n")
    result_text.insert(tk.END, f"Varış Zamanı: {flight['arrival']['scheduled']}\n")
    result_text.insert(tk.END, f"Havayolu: {flight['airline']['name']}\n")
    result_text.insert(tk.END, f"Uçuş Numarası: {flight['flight']['number']}\n")
    result_text.insert(tk.END, f"Uçak Modeli: {flight['aircraft']['model']}\n")



root = tk.Tk()
root.title("Uçuş Bilgisi Sorgulama")
root.geometry("400x400")

canvas = tk.Canvas(root, height=100, width=100)
canvas.pack()


img = Image.open("flight.jpg")  # JPEG veya PNG dosya yolunu yaz
img = img.resize((200, 100))  # Resmi uygun boyutlara göre yeniden boyutlandır
logo = ImageTk.PhotoImage(img)


canvas.create_image(100,100, image=logo)


label_flight_number = tk.Label(root, text="Uçuş Numarası:")
label_flight_number.pack(pady=10)


entry_flight_number = tk.Entry(root)
entry_flight_number.pack(pady=10)


btn_search = tk.Button(root, text="Sorgula", command=get_flight_info)
btn_search.pack(pady=10)


result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=10)


root.mainloop()
