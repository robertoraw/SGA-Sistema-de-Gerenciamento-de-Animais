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

def cadastrar_animais():
        limpar_tela()
        cadastrar = tk.Label(
        frame_principal,
        text="Cadastrar animais!",
        font=("Arial", 12),
        bg="white",
        fg="black"
    )
        cadastrar.pack(pady=20)
    
def listar_animais():
        limpar_tela()
        listar_animais = tk.Label(
        frame_principal,
        text="Lista de Animais!",
        font=("Arial", 12),
        bg="white",
        fg="black"
    )
        listar_animais.pack(pady=20)

def consultar_animais():
    limpar_tela()
    consultar_animais = tk.Label(
        frame_principal,
        text="Consultar animais!",
        font=("Arial", 12),
        bg="white",
        fg="black"
    )
    consultar_animais.pack(pady=20)
def limpar_tela():
    for widget in frame_principal.winfo_children():
        widget.destroy()

btn_cadastrar = tk.Button(
    frame_menu,
    text="Cadastrar Animal",
    font=("Arial", 12),
    width=20,
    height=2,
    bg="#88E788",
    fg="black",
    command= cadastrar_animais
)

btn_cadastrar.pack(pady=10)

btn_lista_animais = tk.Button(
    frame_menu,
    text="Ver lista de animais",
    font=("Arial", 12),
    width=20,
    height=2,
    bg="#88E788",
    fg="black",
    command=listar_animais
)
btn_lista_animais.pack(pady=10)

btn_consulta = tk.Button(
    frame_menu,
    text="Consultar animal",
    font=("Arial", 12),
    width=20,
    height=2,
    bg="#88E788",
    fg="black",
    command=consultar_animais
)
btn_consulta.pack(pady=10)

frame_principal = tk.Frame(janela, bg="white", width=800, height=520)
frame_principal.pack(side="right", fill="both", expand=True)



janela.mainloop()
