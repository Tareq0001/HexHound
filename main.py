import tkinter as tk
from tkinter import ttk

class HexHoundApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HexHound - Digital Forensics & File Carver")
        self.geometry("900x600")
        self.configure(bg="#121212")
        
        # Toolbar
        toolbar = tk.Frame(self, bg="#1E1E1E", height=50)
        toolbar.pack(fill=tk.X, side=tk.TOP)
        tk.Button(toolbar, text="Load Disk Image", bg="#BB86FC", fg="#000", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(toolbar, text="Run YARA Scan", bg="#03DAC6", fg="#000", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=10, pady=10)
        
        # Hex Viewer
        hex_frame = tk.Frame(self, bg="#000")
        hex_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        hex_text = tk.Text(hex_frame, bg="#000", fg="#4ADE80", font=("Courier", 12))
        hex_text.pack(fill=tk.BOTH, expand=True)
        
        sample_hex = "00000000  4D 5A 90 00 03 00 00 00  04 00 00 00 FF FF 00 00  |MZ..............|\n"
        sample_hex += "00000010  B8 00 00 00 00 00 00 00  40 00 00 00 00 00 00 00  |........@.......|\n"
        sample_hex += "00000020  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|\n"
        sample_hex += "[!] ANOMALY DETECTED AT OFFSET 0x000002F0: SUSPICIOUS PE HEADER"
        hex_text.insert(tk.END, sample_hex)
        hex_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = HexHoundApp()
    app.mainloop()