import tkinter as tk

def open_new_window_and_close_old(old_window, new_window):
    old_window.destroy() 
    new_window = __import__(new_window)  
    new_window.main()  



def main():
    #MAIN WINDOW
    root = tk.Tk()
    root.title("Proyecto Lógic Vol. 2")
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    root.resizable(True, True)
    root.configure(bg="#2C3E50")
    root.configure(bg="#2C3E50")
    
    main_frame = tk.Frame(root, bg="#2C3E50")
    main_frame.pack(expand=True, fill="both", padx=50, pady=50)
    
    title_frame = tk.Frame(main_frame, bg="#2C3E50")
    title_frame.pack(pady=(0, 40))
    
    mainLabel = tk.Label(title_frame, 
                         text="Proyecto Lógica Vol. 2", 
                         font=("Arial", 32, "bold"), 
                         bg="#2C3E50", 
                         fg="#ECF0F1")
    mainLabel.pack(pady=(0, 10))

    #BOTONES

    button_frame = tk.Frame(main_frame, bg="#2C3E50")
    button_frame.pack(expand=True)
    
    button_style = {
        "font": ("Arial", 14, "bold"),
        "width": 25,
        "height": 2,
        "bd": 0,
        "relief": "flat",
        "cursor": "hand2"
    }
    
    btn1 = tk.Button(button_frame, 
                              text="Calculadora de Conjuntos", 
                              bg="#27AE60", 
                              fg="black",
                              activebackground="#2ECC71",
                              activeforeground="white",
                              command=lambda: open_new_window_and_close_old(root, 'set_calculator'),
                              **button_style)
    
    btn1.pack(pady=15)
    
    btn2 = tk.Button(button_frame, 
                                       text="Llaves de Cifrado", 
                                       bg="#E67E22", 
                                       fg="black",
                                       activebackground="#F39C12",
                                       activeforeground="white",
                                       command=lambda: open_new_window_and_close_old(root, 'encryption'),
                                       **button_style)
    btn2.pack(pady=15)
    

    #FOOTER
    footer_frame = tk.Frame(main_frame, bg="#2C3E50")
    footer_frame.pack(side="bottom", fill="x", pady=20)
    
    footer_label = tk.Label(footer_frame, 
                           text="Desarrollado por Daniel, David y Rahul", 
                           font=("Arial", 10), 
                           bg="#2C3E50", 
                           fg="#7F8C8D")
    footer_label.pack()
    
    root.mainloop()


if __name__ == "__main__":
    main()