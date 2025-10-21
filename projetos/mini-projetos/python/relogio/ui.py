# Módulo de Interface Gráfica

# Importações
import customtkinter as ctk
import time
import sys



class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry = "650x400"

        # Frame Central
        mainFrame = ctk.CTkFrame(self, 
                                 fg_color= "transparent")

        # Criação do Frame do Relógio
        clockFrame = ctk.CTkFrame(
            mainFrame,
            fg_color= "transparent"
        )

        clockFrame.pack(mainFrame)

if __name__ == "__main__":
    app = App()
    app.mainloop()