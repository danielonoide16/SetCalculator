import tkinter as tk
import sortedset as ss
import utils
import relation

class EncrypterWindow:

    def _popup(self, title, text):
        """crea una ventana emergente modal con un mensaje"""
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.geometry("700x300")

        tk.Label(popup, text=text).pack(pady=20)
        tk.Button(popup, text="Cerrar", command=popup.destroy).pack(pady=10)

        popup.transient(self.root)
        popup.grab_set() # hace que la ventana sea modal, modal es que no se puede interactuar con la ventana padre hasta cerrar la hija
        self.root.wait_window(popup) #espera a que se cierre la ventana hija para continuar con la ejecución del código

    

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mini Game")
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}")
        self.root.resizable(True, True)
        self.root.configure(bg="#2C3E50")
        self.root.configure(bg="#2C3E50")

        #go back button
        import main
        self.back_button = tk.Button(self.root, text="Volver", font=("Arial", 12), command= lambda: main.open_new_window_and_close_old(self.root, 'main'))
        self.back_button.place(x=10, y=10)



        #INPUT

        transmitters_label = tk.Label(self.root, text="Emisores", font=("Arial", 18), fg="white", bg="#2C3E50")
        self.transmitters_input = tk.Entry(self.root, width=30)

        keys_label = tk.Label(self.root, text="Llaves", font=("Arial", 18), fg="white", bg="#2C3E50")
        self.keys_input = tk.Entry(self.root, width=30)

        receivers_label = tk.Label(self.root, text="Receptores", font=("Arial", 18), fg="white", bg="#2C3E50")
        self.receivers_input = tk.Entry(self.root, width=30)

        connections_label = tk.Label(self.root, text="Conexiones", font=("Arial", 18), fg="white", bg="#2C3E50")
        self.connections_input = tk.Entry(self.root, width=100)

        transmitters_label.pack(pady=10)
        self.transmitters_input.pack(pady=10)

        keys_label.pack(pady=10)
        self.keys_input.pack(pady=10)        

        receivers_label.pack(pady=10)
        self.receivers_input.pack(pady=10)

        connections_label.pack(pady=10)
        self.connections_input.pack(pady=10)


        # OUTPUT
        results_button = tk.Button(self.root, text="Ver resultados", command=lambda: self.generate_results())
        results_button.pack(pady=50)

        results_frame = tk.LabelFrame(self.root, text="Resultados", padx=10, pady=10)
        results_frame.pack(fill="both", expand=True, padx=10, pady=10)

        function_label = tk.Label(results_frame, text="Propiedades de funciones", font=("Arial", 18), fg="white", bg="#6C6C6C")
        function_label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.function_results = tk.Text(results_frame, height=7, state="disabled")
        self.function_results.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        relation_label = tk.Label(results_frame, text="Propiedades de relación", font=("Arial", 18), fg="white", bg="#6C6C6C")
        relation_label.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        self.relation_results = tk.Text(results_frame, height=7, state="disabled")
        self.relation_results.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

        operations_label = tk.Label(results_frame, text="Operaciones de conjuntos", font=("Arial", 18), fg="white", bg="#6C6C6C")
        operations_label.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        self.operations_results = tk.Text(results_frame, height=7, state="disabled", fg="black")
        self.operations_results.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

        #expansion equitativa
        results_frame.columnconfigure(0, weight=1)
        results_frame.columnconfigure(1, weight=1)
        results_frame.columnconfigure(2, weight=1)
        results_frame.rowconfigure(0, weight=1)
        results_frame.rowconfigure(1, weight=1)


   


    def generate_results(self):
        #verify input

        transmitters_text = self.transmitters_input.get()
        keys_text = self.keys_input.get()
        receivers_text = self.receivers_input.get()
        connections_text = self.connections_input.get()

        popup_text = ""
        if not utils.is_valid_format(transmitters_text):
            popup_text += "El formato de los emisores es inválido\n"
        if not utils.is_valid_format(keys_text):
            popup_text += "El formato de las llaves es inválido\n"
        if not utils.is_valid_format(receivers_text):
            popup_text += "El formato de los receptores es inválido\n"
        if not utils.is_valid_format_tuple(connections_text):
            popup_text += "El formato de las conexiones es inválido\n"
        
        if popup_text != "":
            popup_text += "Asegurate de que los conjuntos sigan el formato: Str,Str,Str...\nY las relaciones (Str,Int,Str),(Str,Int,Str)..."
            self._popup("Entrada inválida", popup_text)
            return
        
        keys_list = utils.text_to_list(keys_text)

        if not all(x.strip().lstrip('-').isdigit() for x in keys_list): #verificar que la lista de llaves sean solo enteros
            self._popup("Entrada inválida", "Las llaves solo pueden ser enteros")
            return

        transmitters_set = ss.SortedSet(utils.text_to_list(transmitters_text))
        keys_set = ss.SortedSet(keys_list)
        receivers_set = ss.SortedSet(utils.text_to_list(receivers_text))

        print(transmitters_set)
        print(keys_set)
        print(receivers_set)

        #Verificar que las conexiones sean válidas
        connections_list = utils.text_to_tuples(connections_text)

        popup_text = ""

        tuples = []

        for t, k, r in connections_list:
            if not transmitters_set.contains(t):
                popup_text += f"El elemento {t} no está en el conjunto de emisores\n"
            if not keys_set.contains(k):
                popup_text += f"El elemento {k} no está en el conjunto de llaves\n"
            if not receivers_set.contains(r):
                popup_text += f"El elemento {r} no está en el conjunto de receptores\n"

            tuples.append((t,r))


        if popup_text != "":
            self._popup("Conexiones inválidas", popup_text)
            return



        tuples_set = ss.SortedSet(tuples)
        print(tuples_set)
        
        rel = relation.Relation(tuples_set, transmitters_set, receivers_set)

        #GENERAR RESULTADOS

        self.function_results.configure(state="normal")
        self.relation_results.configure(state="normal")
        self.operations_results.configure(state="normal")

        self.function_results.delete("1.0", tk.END)
        self.relation_results.delete("1.0", tk.END)
        self.operations_results.delete("1.0", tk.END)

        #FUNCIONES
        self.function_results.insert("end", "- Es función: " + ("SÍ" if rel.isfunction() else "No") + "\n")
        self.function_results.insert("end", "- Inyectiva: " + ("SÍ" if rel.isinjective() else "No") + "\n")
        self.function_results.insert("end", "- Sobreyectiva: " + ("SÍ" if rel.issurjective() else "No") + "\n")
        self.function_results.insert("end", "- Biyectiva: " + ("SÍ" if rel.isbijective() else "No") + "\n")


        #RELACIONES
        self.relation_results.insert("end", "- Reflexiva: " + ("SÍ" if rel.isreflexive() else "No") + "\n")
        self.relation_results.insert("end", "- Simétrica: " + ("SÍ" if rel.issymmetric() else "No") + "\n")
        self.relation_results.insert("end", "- Transitiva: " + ("SÍ" if rel.istransitive() else "No") + "\n")

        # CONJUNTOS
        union = transmitters_set.union(receivers_set)
        intersection = transmitters_set.intersection(receivers_set)
        difference = transmitters_set.difference(receivers_set)
        reverse_difference = receivers_set.difference(transmitters_set)
        sym_difference = transmitters_set.sym_difference(receivers_set)
        t_complement = transmitters_set.complement(union)
        r_complement = receivers_set.complement(union)

        t_is_sub = transmitters_set.is_sub_set(receivers_set)
        r_is_sub = receivers_set.is_sub_set(transmitters_set)

        t_is_sub = "Si" if t_is_sub else "No"
        r_is_sub = "Si" if r_is_sub else "No"

        t_is_proper_sub = transmitters_set.is_proper_sub_set(receivers_set)
        r_is_proper_sub = receivers_set.is_proper_sub_set(transmitters_set)

        t_is_proper_sub = "Si" if t_is_proper_sub else "No"
        r_is_proper_sub = "Si" if r_is_proper_sub else "No"        


        self.operations_results.insert("end", "Unión: " + str(union) + "\n")
        self.operations_results.insert("end", "Intersección: " + str(intersection) + "\n")
        self.operations_results.insert("end", "Emisores - Receptores: " + str(difference) + "\n")
        self.operations_results.insert("end", "Receptores - Emisores: " + str(reverse_difference) + "\n")
        self.operations_results.insert("end", "Diferencia simétrica: " + str(sym_difference) + "\n")
        self.operations_results.insert("end", "Complemento de los emisores: " + str(t_complement) + "\n")
        self.operations_results.insert("end", "Complemento de los receptores: " + str(r_complement) + "\n")
        self.operations_results.insert("end", "¿Los emisores son subconjunto de los receptores? " + t_is_sub + "\n")
        self.operations_results.insert("end", "¿Los receptores son subconjunto de los emisores? " + r_is_sub + "\n")
        self.operations_results.insert("end", "¿Los emisores son subconjunto propio de los receptores? " + t_is_proper_sub + "\n")
        self.operations_results.insert("end", "¿Los receptores son subconjunto propio de los emisores? " + r_is_proper_sub + "\n")


        self.function_results.configure(state="disabled")
        self.relation_results.configure(state="disabled")
        self.operations_results.configure(state="disabled")        

    


def main():
    game = EncrypterWindow()
    game.root.mainloop()