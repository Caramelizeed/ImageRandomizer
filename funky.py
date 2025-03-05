import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO
import threading
BG_COLOR = "#2C2F33"
FG_COLOR = "#FFFFFF"
BUTTON_COLOR = "#7289DA"

def generate_funny_image():
    def fetch_image():
        try:
            response = requests.get("https://meme-api.com/gimme")
            data = response.json()

            if "url" not in data:
                messagebox.showerror("Error", "Failed to fetch meme. Try again!")
                return

            meme_url = data["url"]
            image_response = requests.get(meme_url, stream=True)

            image_data = BytesIO(image_response.content)
            img = Image.open(image_data)

            img_tk = ImageTk.PhotoImage(img)
            label_image.config(image=img_tk)
            label_image.image = img_tk
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch meme: {e}")

    threading.Thread(target=fetch_image, daemon=True).start()

root = tk.Tk()
root.title("Funny Meme Generator")
root.geometry("450x500")
root.configure(bg=BG_COLOR)

tk.Label(root, text="Click to generate a funny meme!", bg=BG_COLOR, fg=FG_COLOR, font=("Arial", 12)).pack(pady=5)

generate_btn = tk.Button(root, text="Generate Meme", command=generate_funny_image, bg=BUTTON_COLOR, fg=FG_COLOR, font=("Arial", 12), relief="flat", padx=10, pady=5)
generate_btn.pack(pady=10)

label_image = tk.Label(root, bg=BG_COLOR)
label_image.pack(pady=10)

def animate_button():
    current_color = generate_btn.cget("bg")
    new_color = "#5865F2" if current_color == BUTTON_COLOR else BUTTON_COLOR
    generate_btn.config(bg=new_color)
    root.after(500, animate_button)

animate_button()

root.mainloop()
