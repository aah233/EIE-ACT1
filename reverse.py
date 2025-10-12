if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print("Se debe indicar el fichero como primer argumento")
    sys.exit(1)

print(f"Se leerán las palabras del fichero {filename}")

# Nombre del fichero de entrada definido como parametro
filename = "texto.txt"

# Abrir y leer el contenido
with open(filename, "r", encoding="utf-8") as f:
    contenido = f.read()

# Separar el texto en palabras
palabras = contenido.split()

# Dar la vuelta a la lista de palabras
palabras_invertidas = palabras[::-1]

# Mostrar por pantalla o guardar en otro fichero
print("Palabras invertidas:")
print(" ".join(palabras_invertidas))
