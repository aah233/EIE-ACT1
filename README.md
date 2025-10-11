# Repo para EIEC - DevOps - UNIR

Este repositorio nos servirá para demostrar el uso de Git en la asignatura de EIEC y muchas cosas mas.

---

Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, necesitarás adaptarlos o ejecutarlos en una máquina virtual Linux.

## Ejecución

python3 main.py <filename> <dup>
  filename: **ruta** al fichero que contiene la lista de palabras, una por línea
  dup: **yes|no**, yes para eliminar palabras duplicadas, no para mantener la lista


---

### Ejemplo de ejecución 

Archivo: `palabras.txt`

Unir
Universidad
Canarias
Master
Gofio
Totufo
Totufa
Canarias
Cachopo
gato

Ejecución del script:
```bash
python3 main.py palabras.txt yes

