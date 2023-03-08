import tkinter as tk

def reiniciar():
    opciones.set(None)

window = tk.Tk()

window.configure(padx=15, pady=20)

q_label = tk.Label(window,text="¿Cuál es tu deporte favorito?").pack()
opciones = tk.IntVar()

tk.Radiobutton(window, text="Fútbol", variable=opciones, value=1).pack()
tk.Radiobutton(window, text="Basketball", variable=opciones, value=2).pack()
tk.Radiobutton(window, text="Tenis", variable=opciones, value=3).pack()
tk.Radiobutton(window, text="Atletismo", variable=opciones, value=4).pack()

tk.Button(window,text="Reiniciar", command=reiniciar).pack()

window.mainloop()