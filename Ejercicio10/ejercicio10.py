with open('archivo.txt', 'w') as f:
    texto = 'Info escrita al archivo por primera vez'
    f.write(texto)


with open('archivo.txt', 'a') as f:
    nuevo_texto = "\nInfo que puse después"
    f.write(nuevo_texto)
