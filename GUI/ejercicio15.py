import tkinter as tk

window = tk.Tk()
window.config(padx=50, pady=15)


carbohidratos1 = tk.IntVar()
carbohidratos2 = tk.IntVar()
carbohidratos3 = tk.IntVar()

proteinas1 = tk.IntVar()
proteinas2 = tk.IntVar()
proteinas3 = tk.IntVar()
proteinas4 = tk.IntVar()

ensalada1 = tk.IntVar()
ensalada2 = tk.IntVar()
ensalada3 = tk.IntVar()

bebida = tk.IntVar()


question_label = tk.Label(window, text="Elige los ingredientes de tu menú:", pady=15).pack() 

carbs_label = tk.Label(window, text="Carbohidratos", pady=10, font=(15)).pack()
tk.Checkbutton(window, text="Arroz", variable="carbohidratos1", onvalue="Arroz").pack()
tk.Checkbutton(window, text="Spaguetti", variable="carbohidratos2", onvalue="Spaguetti").pack()
tk.Checkbutton(window, text="Papas a la francesa", variable="carbohidratos3", onvalue="Papas").pack()

protein_label = tk.Label(window, text="Proteinas", pady=10, font=(15)).pack()

tk.Checkbutton(window, text="Carne de res", variable="proteinas1", onvalue="Res").pack()
tk.Checkbutton(window, text="Cerdo", variable="proteinas2", onvalue="Cerdo").pack()
tk.Checkbutton(window, text="Pescado", variable="proteinas3", onvalue="Pescado").pack()
tk.Checkbutton(window, text="Proteina vegetal", variable="proteinas4", onvalue="Vegetal").pack()

salad_label = tk.Label(window, text="Ensaladas", pady=10, font=(15)).pack()

tk.Checkbutton(window, text="Ensalada rusa", variable="ensalada1").pack()
tk.Checkbutton(window, text="Ensalada Caesar", variable="ensalada2").pack()
tk.Checkbutton(window, text="Kartoffelsalat", variable="ensalada3").pack()

beverage_label = tk.Label(window, text="Bebidas", pady=10, font=(15)).pack()

tk.Radiobutton(window, text="Agua", variable="bebida", value=1).pack()
tk.Radiobutton(window, text="Limonada", variable="bebida", value=2).pack()
tk.Radiobutton(window, text="Zumo de frutos rojos", variable="bebida", value=3).pack()


window.mainloop()