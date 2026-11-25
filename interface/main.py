import tkinter as tk

janela = tk.Tk()

janela.title("SGA - Sistema de Gerenciamento de Animais")
janela.geometry("1000x600")

janela.mainloop()

frame_topo = tk.Frame(janela, bg="grey", width=100, height=250)
frame_topo.pack(padx=10, pady=10)