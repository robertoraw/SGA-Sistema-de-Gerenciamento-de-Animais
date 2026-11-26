import tkinter as tk

janela = tk.Tk()

janela.title("SGA - Sistema de Gerenciamento de Animais")
janela.geometry("1000x600")

frame_topo = tk.Frame(janela, bg="gray", height=80 )
frame_topo.pack(fill="x")

titulo = tk.Label(
frame_topo,
text="SGA - Sistema de Gestão de Animais",
font=("Arial", 18, "bold"),
bg="gray",
fg="white",
)
titulo.pack(pady=20)

frame_menu = tk.Frame(janela, bg="blue", width=200, height=520)
frame_menu.pack(side="left", fill="y")

btn_cadastrar = tk.Button(
    frame_menu,
    text="Cadastrar Animal",
    font=("Arial", 12),
    width=20,
    height=2
)

btn_cadastrar.pack(pady=10)

frame_principal = tk.Frame(janela, bg="orange", width=800, height=520)
frame_principal.pack(side="right", fill="both", expand=True)

janela.mainloop()
