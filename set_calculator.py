import tkinter as tk
from tkinter import messagebox, scrolledtext
import random
from sorted_set import SortedSet  # usamos el SortedSet que nos dieron

conjuntos = {}  # aqui guardamos todos los conjuntos creados


# crear conjunto escribiendo elementos separados por comas
def crear_conjunto_manual(texto):
    if texto.strip() == '':
        return SortedSet()

    elementos = texto.split(',')
    conjunto = SortedSet()

    for elem in elementos:
        elem = elem.strip()
        if elem != '':
            conjunto.add(elem)  # add ya evita duplicados automaticamente

    return conjunto


# genera numeros random del 1 al 100
def generar_numeros(cantidad):
    if cantidad > 30:
        cantidad = 30

    conjunto = SortedSet()
    while len(conjunto.elements) < cantidad:
        num = random.randint(1, 100)
        conjunto.add(str(num))  # add ya evita duplicados

    return conjunto


#devuelve un caracter alfanumerico o simbolo aleatorio
def get_random_char() -> str:
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%&*+-=?'
    return random.choice(chars)


# devuelve un conjunto con letras y simbolos random
def generar_caracteres(cantidad):
    cantidad = min(cantidad, 15)

    conjunto = SortedSet()

    while len(conjunto.elements) < cantidad:
        char = get_random_char()
        conjunto.add(char)  # add ya evita duplicados

    return conjunto


# devuelve un conjunto con cadenas random
def generate_strings(amount):
    amount = min(amount, 15)
    
    MAX_LENGTH = 10
    
    result = SortedSet()
    for _ in range(amount):
        length = random.randint(1, MAX_LENGTH)
        string = str().join(get_random_char() for _ in range(length))
        result.add(string)
    
    return result


# muestra los conjuntos en el area de texto
def actualizar_vista():
    area_texto.configure(state="normal")
    area_texto.delete(1.0, tk.END)

    if len(conjuntos) == 0:
        area_texto.insert(tk.END, "No hay conjuntos creados.\n")
    else:
        for nombre, conjunto in conjuntos.items():
            texto = f"{nombre} = {conjunto} (Cardinalidad: {len(conjunto.elements)})\n"
            area_texto.insert(tk.END, texto)

    area_texto.configure(state="disabled")


# boton para crear conjunto escribiendo elementos
def btn_crear_manual():
    nombre = entrada_nombre.get().strip()

    if nombre == '':
        messagebox.showerror("Error", "Escribe un nombre")
        return

    conjunto = crear_conjunto_manual(entrada_elementos.get())

    if len(conjunto.elements) == 0:
        messagebox.showwarning("Advertencia", "No hay elementos")
        return

    conjuntos[nombre] = conjunto
    messagebox.showinfo("Éxito", f"Conjunto {nombre} creado")
    actualizar_vista()

    entrada_nombre.delete(0, tk.END)
    entrada_elementos.delete(0, tk.END)



def validar_entrada(nombre_entry, cantidad_entry, max_cantidad):
    nombre = nombre_entry.get().strip()
    if not nombre:
        messagebox.showerror("Error", "Escribe un nombre")
        return None, None

    try:
        cantidad = int(cantidad_entry.get())
        if not (1 <= cantidad <= max_cantidad):
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", f"Cantidad entre 1 y {max_cantidad}")
        return None, None

    return nombre, cantidad


def generar_conjunto(nombre_entry, cantidad_entry, max_cantidad, generador_func):
    nombre, cantidad = validar_entrada(nombre_entry, cantidad_entry, max_cantidad)
    if nombre is None:
        return  # hubo error en validación

    conjuntos[nombre] = generador_func(cantidad)
    messagebox.showinfo("Éxito", f"Conjunto {nombre} creado")
    actualizar_vista()
    nombre_entry.delete(0, tk.END)
    #cantidad_entry.delete(0, tk.END)


# eventos de botones 
def btn_generar_numeros():
    generar_conjunto(entrada_nombre, entrada_cantidad, 30, generar_numeros)


def btn_generar_caracteres():
    generar_conjunto(entrada_nombre, entrada_cantidad, 15, generar_caracteres)


def btn_generar_strings():
    generar_conjunto(entrada_nombre, entrada_cantidad, 15, generate_strings)


# boton union A U B
def btn_union():
    nombre_a = entrada_conj_a.get().strip()
    nombre_b = entrada_conj_b.get().strip()

    if nombre_a not in conjuntos or nombre_b not in conjuntos:
        messagebox.showerror("Error", "Conjuntos no existen")
        return

    resultado = conjuntos[nombre_a].union(conjuntos[nombre_b])  # usa el metodo de SortedSet
    messagebox.showinfo("Resultado", f"{nombre_a} ∪ {nombre_b} = {resultado}")


# boton interseccion A ∩ B
def btn_interseccion():
    nombre_a = entrada_conj_a.get().strip()
    nombre_b = entrada_conj_b.get().strip()

    if nombre_a not in conjuntos or nombre_b not in conjuntos:
        messagebox.showerror("Error", "Conjuntos no existen")
        return

    resultado = conjuntos[nombre_a].intersection(conjuntos[nombre_b])  # usa el metodo de SortedSet
    messagebox.showinfo("Resultado", f"{nombre_a} ∩ {nombre_b} = {resultado}")


# boton diferencia A - B
def btn_diferencia():
    nombre_a = entrada_conj_a.get().strip()
    nombre_b = entrada_conj_b.get().strip()

    if nombre_a not in conjuntos or nombre_b not in conjuntos:
        messagebox.showerror("Error", "Conjuntos no existen")
        return

    resultado = conjuntos[nombre_a].difference(conjuntos[nombre_b])  # usa el metodo de SortedSet
    messagebox.showinfo("Resultado", f"{nombre_a} - {nombre_b} = {resultado}")


# boton diferencia simetrica A Δ B
def btn_diferencia_simetrica():
    nombre_a = entrada_conj_a.get().strip()
    nombre_b = entrada_conj_b.get().strip()

    if nombre_a not in conjuntos or nombre_b not in conjuntos:
        messagebox.showerror("Error", "Conjuntos no existen")
        return

    resultado = conjuntos[nombre_a].sym_difference(conjuntos[nombre_b])  # usa el metodo de SortedSet
    messagebox.showinfo("Resultado", f"{nombre_a} Δ {nombre_b} = {resultado}")


# boton complemento A'
def btn_complemento():
    nombre_a = entrada_conj_a.get().strip()

    if nombre_a not in conjuntos:
        messagebox.showerror("Error", "Conjunto no existe")
        return

    # el universo son todos los elementos de todos los conjuntos
    if len(conjuntos) == 0:
        return

    lista_conjuntos = list(conjuntos.values())
    universo = lista_conjuntos[0]
    for i in range(1, len(lista_conjuntos)):
        universo = universo.union(lista_conjuntos[i])

    resultado = conjuntos[nombre_a].complement(universo)  # usa el metodo de SortedSet
    messagebox.showinfo("Resultado", f"{nombre_a}' = {resultado}")


# boton verificar si A esta contenido en B
def btn_subconjunto():
    nombre_a = entrada_conj_a.get().strip()
    nombre_b = entrada_conj_b.get().strip()

    if nombre_a not in conjuntos or nombre_b not in conjuntos:
        messagebox.showerror("Error", "Conjuntos no existen")
        return

    resultado = conjuntos[nombre_a].is_sub_set(conjuntos[nombre_b])  # usa el metodo de SortedSet
    respuesta = "SÍ" if resultado else "NO"
    messagebox.showinfo("Verificación", f"¿{nombre_a} ⊆ {nombre_b}?\n{respuesta}")


# boton verificar si A esta contenido propio en B
def btn_subconjunto_propio():
    nombre_a = entrada_conj_a.get().strip()
    nombre_b = entrada_conj_b.get().strip()

    if nombre_a not in conjuntos or nombre_b not in conjuntos:
        messagebox.showerror("Error", "Conjuntos no existen")
        return

    resultado = conjuntos[nombre_a].is_proper_sub_set(conjuntos[nombre_b])  # usa el metodo de SortedSet
    respuesta = "SÍ" if resultado else "NO"
    messagebox.showinfo("Verificación", f"¿{nombre_a} ⊂ {nombre_b}?\n{respuesta}")


# boton verificar si son disjuntos (no tienen nada en comun)
def btn_disjuntos():
    nombre_a = entrada_conj_a.get().strip()
    nombre_b = entrada_conj_b.get().strip()

    if nombre_a not in conjuntos or nombre_b not in conjuntos:
        messagebox.showerror("Error", "Conjuntos no existen")
        return

    # disjuntos = la interseccion esta vacia
    interseccion = conjuntos[nombre_a].intersection(conjuntos[nombre_b])
    resultado = len(interseccion.elements) == 0
    respuesta = "SÍ" if resultado else "NO"
    messagebox.showinfo("Verificación", f"¿Son disjuntos?\n{respuesta}")


# boton verificar si son iguales
def btn_iguales():
    nombre_a = entrada_conj_a.get().strip()
    nombre_b = entrada_conj_b.get().strip()

    if nombre_a not in conjuntos or nombre_b not in conjuntos:
        messagebox.showerror("Error", "Conjuntos no existen")
        return

    resultado = conjuntos[nombre_a].equals(conjuntos[nombre_b])  # usa el metodo de SortedSet
    respuesta = "SÍ" if resultado else "NO"
    messagebox.showinfo("Verificación", f"¿{nombre_a} = {nombre_b}?\n{respuesta}")


# boton union de varios conjuntos
def btn_union_multiple():
    nombres = entrada_multiples.get().strip()

    if nombres == '':
        messagebox.showerror("Error", "Ingresa nombres separados por comas")
        return

    lista_nombres = [n.strip() for n in nombres.split(',')]

    for nombre in lista_nombres:
        if nombre not in conjuntos:
            messagebox.showerror("Error", f"Conjunto {nombre} no existe")
            return

    # union de varios conjuntos
    resultado = conjuntos[lista_nombres[0]]
    for i in range(1, len(lista_nombres)):
        resultado = resultado.union(conjuntos[lista_nombres[i]])

    messagebox.showinfo("Resultado", f"{' ∪ '.join(lista_nombres)} = {resultado}")


# boton interseccion de varios conjuntos
def btn_interseccion_multiple():
    nombres = entrada_multiples.get().strip()

    if nombres == '':
        messagebox.showerror("Error", "Ingresa nombres separados por comas")
        return

    lista_nombres = [n.strip() for n in nombres.split(',')]

    for nombre in lista_nombres:
        if nombre not in conjuntos:
            messagebox.showerror("Error", f"Conjunto {nombre} no existe")
            return

    # interseccion de varios conjuntos
    resultado = conjuntos[lista_nombres[0]]
    for i in range(1, len(lista_nombres)):
        resultado = resultado.intersection(conjuntos[lista_nombres[i]])

    messagebox.showinfo("Resultado", f"{' ∩ '.join(lista_nombres)} = {resultado}")


# boton limpiar todo
def btn_limpiar():
    respuesta = messagebox.askyesno("Confirmar", "¿Eliminar todos los conjuntos?")
    if respuesta:
        conjuntos.clear()
        actualizar_vista()


def btn_borrar_conjunto():
    nombre = entrada_nombre.get().strip()

    if nombre not in conjuntos:
        messagebox.showerror("Error", "Conjunto no encontrado")
        return
    
    del conjuntos[nombre]
    messagebox.showinfo("Éxito", "Conjunto eliminado correctamente")
    actualizar_vista()




def main():
    global area_texto, entrada_nombre, entrada_elementos, entrada_cantidad
    global entrada_conj_a, entrada_conj_b, entrada_multiples

    root = tk.Tk()
    root.title("Calculadora de Conjuntos")
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    root.resizable(True, True)
    root.configure(bg="#2C3E50")

    # boton para volver al menu principal
    import main
    back_button = tk.Button(root, text="Volver", font=("Arial", 12),
                           command=lambda: main.open_new_window_and_close_old(root, 'main'))
    back_button.place(x=10, y=10)

    # titulo
    tk.Label(root, text="CALCULADORA DE CONJUNTOS", font=("Arial", 28, "bold"),
             bg="#2C3E50", fg="white").pack(pady=20)

    # seccion crear conjuntos
    frame_crear = tk.Frame(root, bg="#2C3E50")
    frame_crear.pack(pady=10)

    tk.Label(frame_crear, text="Nombre:", bg="#2C3E50", fg="white", font=("Arial", 14)).pack(side=tk.LEFT, padx=5)
    entrada_nombre = tk.Entry(frame_crear, width=15, font=("Arial", 14))
    entrada_nombre.pack(side=tk.LEFT, padx=5)

    tk.Label(frame_crear, text="Elementos:", bg="#2C3E50", fg="white", font=("Arial", 14)).pack(side=tk.LEFT, padx=5)
    entrada_elementos = tk.Entry(frame_crear, width=30, font=("Arial", 14))
    entrada_elementos.pack(side=tk.LEFT, padx=5)

    tk.Button(frame_crear, text="Crear Manual", command=btn_crear_manual,
             font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=5)
    
    tk.Button(frame_crear, text="Eliminar conjunto", command=btn_borrar_conjunto,
              font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=5)

    # seccion aleatorios
    frame_aleatorio = tk.Frame(root, bg="#2C3E50")
    frame_aleatorio.pack(pady=10)

    tk.Label(frame_aleatorio, text="Cantidad:", bg="#2C3E50", fg="white", font=("Arial", 14)).pack(side=tk.LEFT, padx=5)
    entrada_cantidad = tk.Entry(frame_aleatorio, width=10, font=("Arial", 14))
    entrada_cantidad.insert(0, "10")
    entrada_cantidad.pack(side=tk.LEFT, padx=5)

    tk.Button(frame_aleatorio, text="Generar Números", command=btn_generar_numeros,
             font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_aleatorio, text="Generar Caracteres", command=btn_generar_caracteres,
             font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=5)
    

    tk.Button(frame_aleatorio, text="Generar Cadenas", command=btn_generar_strings,
            font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=5)

    # seccion seleccionar A y B
    frame_ab = tk.Frame(root, bg="#2C3E50")
    frame_ab.pack(pady=15)

    tk.Label(frame_ab, text="Conjunto A:", bg="#2C3E50", fg="white", font=("Arial", 14)).pack(side=tk.LEFT, padx=5)
    entrada_conj_a = tk.Entry(frame_ab, width=12, font=("Arial", 14))
    entrada_conj_a.pack(side=tk.LEFT, padx=5)

    tk.Label(frame_ab, text="Conjunto B:", bg="#2C3E50", fg="white", font=("Arial", 14)).pack(side=tk.LEFT, padx=5)
    entrada_conj_b = tk.Entry(frame_ab, width=12, font=("Arial", 14))
    entrada_conj_b.pack(side=tk.LEFT, padx=5)

    # botones de operaciones
    frame_ops = tk.Frame(root, bg="#2C3E50")
    frame_ops.pack(pady=10)

    tk.Button(frame_ops, text="A ∪ B", command=btn_union, font=("Arial", 12, "bold"), width=8).pack(side=tk.LEFT, padx=3)
    tk.Button(frame_ops, text="A ∩ B", command=btn_interseccion, font=("Arial", 12, "bold"), width=8).pack(side=tk.LEFT, padx=3)
    tk.Button(frame_ops, text="A - B", command=btn_diferencia, font=("Arial", 12, "bold"), width=8).pack(side=tk.LEFT, padx=3)
    tk.Button(frame_ops, text="A Δ B", command=btn_diferencia_simetrica, font=("Arial", 12, "bold"), width=8).pack(side=tk.LEFT, padx=3)
    tk.Button(frame_ops, text="A'", command=btn_complemento, font=("Arial", 12, "bold"), width=8).pack(side=tk.LEFT, padx=3)

    # botones de verificaciones
    frame_verif = tk.Frame(root, bg="#2C3E50")
    frame_verif.pack(pady=10)

    tk.Button(frame_verif, text="A ⊆ B", command=btn_subconjunto, font=("Arial", 12, "bold"), width=10).pack(side=tk.LEFT, padx=3)
    tk.Button(frame_verif, text="A ⊂ B", command=btn_subconjunto_propio, font=("Arial", 12, "bold"), width=10).pack(side=tk.LEFT, padx=3)
    tk.Button(frame_verif, text="Disjuntos", command=btn_disjuntos, font=("Arial", 12, "bold"), width=10).pack(side=tk.LEFT, padx=3)
    tk.Button(frame_verif, text="A = B", command=btn_iguales, font=("Arial", 12, "bold"), width=10).pack(side=tk.LEFT, padx=3)

    # operaciones multiples
    frame_mult = tk.Frame(root, bg="#2C3E50")
    frame_mult.pack(pady=15)

    tk.Label(frame_mult, text="Múltiples (A,B,C):", bg="#2C3E50", fg="white", font=("Arial", 14)).pack(side=tk.LEFT, padx=5)
    entrada_multiples = tk.Entry(frame_mult, width=25, font=("Arial", 14))
    entrada_multiples.pack(side=tk.LEFT, padx=5)

    tk.Button(frame_mult, text="∪", command=btn_union_multiple, font=("Arial", 12, "bold"), width=5).pack(side=tk.LEFT, padx=3)
    tk.Button(frame_mult, text="∩", command=btn_interseccion_multiple, font=("Arial", 12, "bold"), width=5).pack(side=tk.LEFT, padx=3)

    # area de texto
    tk.Label(root, text="CONJUNTOS CREADOS:", font=("Arial", 14, "bold"),
             bg="#2C3E50", fg="white").pack(pady=10)

    area_texto = scrolledtext.ScrolledText(root, height=8, width=100, bg="white",
                                           fg="#2C3E50", font=("Arial", 12), state="disabled")
    area_texto.pack(pady=10)

    # boton limpiar
    tk.Button(root, text="Limpiar Todo", command=btn_limpiar,
             font=("Arial", 12, "bold"), width=15).pack(pady=10)

    actualizar_vista()

    root.mainloop()


if __name__ == "__main__":
    main()
