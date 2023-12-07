import customtkinter as ctk
from PIL import Image, ImageTk
import pygame

#pantalla de inicio y menú principal funciones
def show_welcome_message():
    reproducir_sonido()
    name = name_entry.get()
    welcome_label = ctk.CTkLabel(root, text=f"¡Bienvenido/a a enSeñaMe, {name}!")
    welcome_label.place(relx=0.5, rely=0.6, anchor="center")
    welcome_label.configure(bg_color='#0c8f8f')
    welcome_label.configure(font=("Goudy Stout", 20))
    

def show_menu():
    reproducir_sonido()
    hide_current_screen()

    menú_frame.place(relx=0.5, rely=0.5, anchor="center")
    menú_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    abecedario_button.grid(row=0, column=4, padx=20, pady=20)
    familia_button.grid(row=1, column=4, padx=20, pady=20)
    saludos_button.grid(row=2, column=4, padx=20, pady=20)

#Sonidos
def reproducir_sonido():
    pygame.mixer.init()
    pygame.mixer.music.load("sonido.mp3")  
    pygame.mixer.music.play()

def reproducir_sonidoClick():
    pygame.mixer.init()
    pygame.mixer.music.load("sonidoClick.mp3")  # Ruta del archivo de sonido
    pygame.mixer.music.play()


#abecedario funciones

def show_abecedario():
    reproducir_sonidoClick()
    
    abecedario_frame.place(relx=0.5, rely=0.5, anchor="center")
    abecedario_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    letra_a_button.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letra_b_button.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    letra_c_button.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    letra_d_button.grid(row=0, column=3, padx=(20, 40), pady=(20, 40))
    letra_e_button.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    letra_f_button.grid(row=1, column=1, padx=(20, 40), pady=(20, 40))
    letra_g_button.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    letra_h_button.grid(row=1, column=3, padx=(20, 40), pady=(20, 40))
    letra_i_button.grid(row=2, column=0, padx=(20, 40), pady=(20, 40))
    letra_j_button.grid(row=2, column=1, padx=(20, 40), pady=(20, 40))
    letra_k_button.grid(row=2, column=2, padx=(20, 40), pady=(20, 40))
    letra_l_button.grid(row=2, column=3, padx=(20, 40), pady=(20, 40))
    letra_m_button.grid(row=3, column=0, padx=(20, 40), pady=(20, 40))
    letra_n_button.grid(row=3, column=1, padx=(20, 40), pady=(20, 40))
    letra_ñ_button.grid(row=3, column=2, padx=(20, 40), pady=(20, 40))
    letra_o_button.grid(row=3, column=3, padx=(20, 40), pady=(20, 40))
    letra_p_button.grid(row=4, column=0, padx=(20, 40), pady=(20, 40))
    letra_q_button.grid(row=4, column=1, padx=(20, 40), pady=(20, 40))
    letra_r_button.grid(row=4, column=2, padx=(20, 40), pady=(20, 40))
    letra_s_button.grid(row=4, column=3, padx=(20, 40), pady=(20, 40))
    letra_t_button.grid(row=5, column=0, padx=(20, 40), pady=(20, 40))
    letra_u_button.grid(row=5, column=1, padx=(20, 40), pady=(20, 40))
    letra_v_button.grid(row=5, column=2, padx=(20, 40), pady=(20, 40))
    letra_w_button.grid(row=5, column=3, padx=(20, 40), pady=(20, 40))
    letra_x_button.grid(row=6, column=0, padx=(20, 40), pady=(20, 40))
    letra_y_button.grid(row=6, column=1, padx=(20, 40), pady=(20, 40))
    letra_z_button.grid(row=6, column=2, padx=(20, 40), pady=(20, 40))
    volver_menu_abecedario_button.grid(row=7, column=0, pady=20, columnspan=4)

def volver_al_menu_abecedario():
    reproducir_sonidoClick()
    show_menu()
    abecedario_frame.place_forget()

#Función A
def letra_a():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_a_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_a_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_a_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_a_button.place(relx=0.95, rely=0.05, anchor="ne")

    letraA = ctk.CTkImage(dark_image=Image.open("letraA.png"), size=(250, 250))
    imagen1A = ctk.CTkImage(dark_image=Image.open("A.png"), size=(300, 400))
    imagen2A = ctk.CTkImage(dark_image=Image.open("árbol.png"), size=(400, 400))
    
    letraA_label = ctk.CTkLabel(letra_a_frame, image=letraA, text="LETRA A/a:", compound="bottom")
    imagen1A_label = ctk.CTkLabel(letra_a_frame, image=imagen1A, text="Seña:", compound="bottom")
    imagen2A_label = ctk.CTkLabel(letra_a_frame, image=imagen2A, text="Otra palabra con esta letra: Árbol", compound="bottom")
   
   
    letraA_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraA_label.configure(bg_color='#101652')
    letraA_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1A_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1A_label.configure(bg_color='#0c8f8f')
    imagen1A_label.configure(font=("Cooper Black", 40))
    
    imagen2A_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2A_label.configure(bg_color='#0c8f8f')
    imagen2A_label.configure(font=("Cooper Black", 40))
    
    A_label = ctk.CTkLabel(letra_a_frame, text="A de abeja.")
    A_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    A_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    A_label.configure(font=("Cooper Black", 70))
    
    
def volver_al_menu_letra_a():
    show_abecedario()
    letra_a_frame.place_forget()
    pág_siguiente_a_button.place_forget()
    
    
def pág_siguiente_a():
    letra_b()
    letra_a_frame.place_forget()
    
#Función B
def letra_b():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_b_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_b_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_b_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_b_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_b_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraB = ctk.CTkImage(dark_image=Image.open("letraB.png"), size=(250, 250))
    imagen1B = ctk.CTkImage(dark_image=Image.open("B.png"), size=(300, 400))
    imagen2B = ctk.CTkImage(dark_image=Image.open("bolivia.png"), size=(400, 400))
    
    letraB_label = ctk.CTkLabel(letra_b_frame, image=letraB, text="LETRA B/b:", compound="bottom")
    imagen1B_label = ctk.CTkLabel(letra_b_frame, image=imagen1B, text="Seña:", compound="bottom")
    imagen2B_label = ctk.CTkLabel(letra_b_frame, image=imagen2B, text="Otra palabra con esta letra: Bolivia", compound="bottom")
   
   
    letraB_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraB_label.configure(bg_color='#101652')
    letraB_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1B_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1B_label.configure(bg_color='#0c8f8f')
    imagen1B_label.configure(font=("Cooper Black", 40))
    
    imagen2B_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2B_label.configure(bg_color='#0c8f8f')
    imagen2B_label.configure(font=("Cooper Black", 40))
    
    B_label = ctk.CTkLabel(letra_b_frame, text="B de banana.")
    B_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    B_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    B_label.configure(font=("Cooper Black", 70))

def volver_al_menu_letra_b():
    show_abecedario()
    letra_b_frame.place_forget()
    pág_siguiente_b_button.place_forget()
    pág_anterior_b_button.place_forget()
    
def pág_siguiente_b():
    letra_c()
    letra_b_frame.place_forget()
    
def pág_anterior_b():
    letra_a()
    letra_b_frame.place_forget()

#Función C
def letra_c():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_c_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_c_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_c_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_c_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_c_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraC = ctk.CTkImage(dark_image=Image.open("letraC.png"), size=(250, 250))
    imagen1C = ctk.CTkImage(dark_image=Image.open("C.png"), size=(300, 400))
    imagen2C = ctk.CTkImage(dark_image=Image.open("cangrejo.png"), size=(400, 400))
    
    letraC_label = ctk.CTkLabel(letra_c_frame, image=letraC, text="LETRA C/c:", compound="bottom")
    imagen1C_label = ctk.CTkLabel(letra_c_frame, image=imagen1C, text="Seña:", compound="bottom")
    imagen2C_label = ctk.CTkLabel(letra_c_frame, image=imagen2C, text="Otra palabra con esta letra: Cangrejo", compound="bottom")
   
   
    letraC_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraC_label.configure(bg_color='#101652')
    letraC_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1C_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1C_label.configure(bg_color='#0c8f8f')
    imagen1C_label.configure(font=("Cooper Black", 40))
    
    imagen2C_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2C_label.configure(bg_color='#0c8f8f')
    imagen2C_label.configure(font=("Cooper Black", 40))
    
    C_label = ctk.CTkLabel(letra_c_frame, text="C de conejo.")
    C_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    C_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    C_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_c():
    show_abecedario()
    letra_c_frame.place_forget()
    pág_siguiente_c_button.place_forget()
    pág_anterior_c_button.place_forget()
    
def pág_siguiente_c():
    letra_d()
    letra_c_frame.place_forget()
    
def pág_anterior_c():
    letra_b()
    letra_c_frame.place_forget()

#Función D
def letra_d():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_d_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_d_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_d_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_d_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_d_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraD = ctk.CTkImage(dark_image=Image.open("letraD.png"), size=(250, 250))
    imagen1D = ctk.CTkImage(dark_image=Image.open("D.png"), size=(300, 400))
    imagen2D = ctk.CTkImage(dark_image=Image.open("durazno.png"), size=(400, 400))
    
    letraD_label = ctk.CTkLabel(letra_d_frame, image=letraD, text="LETRA D/d:", compound="bottom")
    imagen1D_label = ctk.CTkLabel(letra_d_frame, image=imagen1D, text="Seña:", compound="bottom")
    imagen2D_label = ctk.CTkLabel(letra_d_frame, image=imagen2D, text="Otra palabra con esta letra: Durazno", compound="bottom")
   
   
    letraD_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraD_label.configure(bg_color='#101652')
    letraD_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1D_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1D_label.configure(bg_color='#0c8f8f')
    imagen1D_label.configure(font=("Cooper Black", 40))
    
    imagen2D_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2D_label.configure(bg_color='#0c8f8f')
    imagen2D_label.configure(font=("Cooper Black", 40))
    
    D_label = ctk.CTkLabel(letra_d_frame, text="D de dinosaurio.")
    D_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    D_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    D_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_d():
    show_abecedario()
    letra_d_frame.place_forget()
    pág_siguiente_d_button.place_forget()
    pág_anterior_d_button.place_forget()
    
def pág_siguiente_d():
    letra_e()
    letra_d_frame.place_forget()
    
def pág_anterior_d():
    letra_c()
    letra_d_frame.place_forget()

#Función E
def letra_e():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_e_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_e_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_e_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_e_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_e_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraE = ctk.CTkImage(dark_image=Image.open("letraE.png"), size=(250, 250))
    imagen1E = ctk.CTkImage(dark_image=Image.open("E.png"), size=(300, 400))
    imagen2E = ctk.CTkImage(dark_image=Image.open("escoba.png"), size=(400, 400))
    
    letraE_label = ctk.CTkLabel(letra_e_frame, image=letraE, text="LETRA E/e:", compound="bottom")
    imagen1E_label = ctk.CTkLabel(letra_e_frame, image=imagen1E, text="Seña:", compound="bottom")
    imagen2E_label = ctk.CTkLabel(letra_e_frame, image=imagen2E, text="Otra palabra con esta letra: Escoba", compound="bottom")
   
   
    letraE_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraE_label.configure(bg_color='#101652')
    letraE_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1E_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1E_label.configure(bg_color='#0c8f8f')
    imagen1E_label.configure(font=("Cooper Black", 40))
    
    imagen2E_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2E_label.configure(bg_color='#0c8f8f')
    imagen2E_label.configure(font=("Cooper Black", 40))
    
    E_label = ctk.CTkLabel(letra_e_frame, text="E de elefante.")
    E_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    E_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    E_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_e():
    show_abecedario()
    letra_e_frame.place_forget()
    pág_siguiente_e_button.place_forget()
    pág_anterior_e_button.place_forget()
    
def pág_siguiente_e():
    letra_f()
    letra_e_frame.place_forget()
    
def pág_anterior_e():
    letra_d()
    letra_e_frame.place_forget()

#Función F
def letra_f():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_f_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_f_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_f_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_f_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_f_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraF = ctk.CTkImage(dark_image=Image.open("letraF.png"), size=(250, 250))
    imagen1F = ctk.CTkImage(dark_image=Image.open("F.png"), size=(300, 400))
    imagen2F = ctk.CTkImage(dark_image=Image.open("foco.png"), size=(400, 400))
    
    letraF_label = ctk.CTkLabel(letra_f_frame, image=letraF, text="LETRA F/f:", compound="bottom")
    imagen1F_label = ctk.CTkLabel(letra_f_frame, image=imagen1F, text="Seña:", compound="bottom")
    imagen2F_label = ctk.CTkLabel(letra_f_frame, image=imagen2F, text="Otra palabra con esta letra: Foco", compound="bottom")
   
   
    letraF_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraF_label.configure(bg_color='#101652')
    letraF_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1F_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1F_label.configure(bg_color='#0c8f8f')
    imagen1F_label.configure(font=("Cooper Black", 40))
    
    imagen2F_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2F_label.configure(bg_color='#0c8f8f')
    imagen2F_label.configure(font=("Cooper Black", 40))
    
    F_label = ctk.CTkLabel(letra_f_frame, text="F de foca.")
    F_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    F_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    F_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_f():
    show_abecedario()
    letra_f_frame.place_forget()
    pág_siguiente_f_button.place_forget()
    pág_anterior_f_button.place_forget()
    
def pág_siguiente_f():
    letra_g()
    letra_f_frame.place_forget()
    
def pág_anterior_f():
    letra_e()
    letra_f_frame.place_forget()

#Función G
def letra_g():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_g_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_g_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_g_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_g_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_g_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraG = ctk.CTkImage(dark_image=Image.open("letraG.png"), size=(250, 250))
    imagen1G= ctk.CTkImage(dark_image=Image.open("G.png"), size=(300, 400))
    imagen2G = ctk.CTkImage(dark_image=Image.open("gelatina.png"), size=(400, 400))
    
    letraG_label = ctk.CTkLabel(letra_g_frame, image=letraG, text="LETRA G/g:", compound="bottom")
    imagen1G_label = ctk.CTkLabel(letra_g_frame, image=imagen1G, text="Seña:", compound="bottom")
    imagen2G_label = ctk.CTkLabel(letra_g_frame, image=imagen2G, text="Otra palabra con esta letra: Gelatina", compound="bottom")
   
   
    letraG_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraG_label.configure(bg_color='#101652')
    letraG_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1G_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1G_label.configure(bg_color='#0c8f8f')
    imagen1G_label.configure(font=("Cooper Black", 40))
    
    imagen2G_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2G_label.configure(bg_color='#0c8f8f')
    imagen2G_label.configure(font=("Cooper Black", 40))
    
    G_label = ctk.CTkLabel(letra_g_frame, text="G de gato.")
    G_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    G_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    G_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_g():
    show_abecedario()
    letra_g_frame.place_forget()
    pág_siguiente_g_button.place_forget()
    pág_anterior_g_button.place_forget()
    
def pág_siguiente_g():
    letra_h()
    letra_g_frame.place_forget()
    
def pág_anterior_g():
    letra_f()
    letra_g_frame.place_forget()

#Función H
def letra_h():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_h_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_h_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_h_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_h_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_h_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraH = ctk.CTkImage(dark_image=Image.open("letraH.png"), size=(250, 250))
    imagen1H = ctk.CTkImage(dark_image=Image.open("H.png"), size=(300, 400))
    imagen2H = ctk.CTkImage(dark_image=Image.open("hielo.png"), size=(400, 400))
    
    letraH_label = ctk.CTkLabel(letra_h_frame, image=letraH, text="LETRA H/h:", compound="bottom")
    imagen1H_label = ctk.CTkLabel(letra_h_frame, image=imagen1H, text="Seña:", compound="bottom")
    imagen2H_label = ctk.CTkLabel(letra_h_frame, image=imagen2H, text="Otra palabra con esta letra: Hielo", compound="bottom")
   
   
    letraH_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraH_label.configure(bg_color='#101652')
    letraH_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1H_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1H_label.configure(bg_color='#0c8f8f')
    imagen1H_label.configure(font=("Cooper Black", 40))
    
    imagen2H_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2H_label.configure(bg_color='#0c8f8f')
    imagen2H_label.configure(font=("Cooper Black", 40))
    
    H_label = ctk.CTkLabel(letra_h_frame, text="H de hipopótamo.")
    H_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    H_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    H_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_h():
    show_abecedario()
    letra_h_frame.place_forget()
    pág_siguiente_h_button.place_forget()
    pág_anterior_h_button.place_forget()
    
def pág_siguiente_h():
    letra_i()
    letra_h_frame.place_forget()
    
def pág_anterior_h():
    letra_g()
    letra_h_frame.place_forget()

#Función I
def letra_i():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_i_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_i_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_i_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_i_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_i_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraI = ctk.CTkImage(dark_image=Image.open("letraI.png"), size=(250, 250))
    imagen1I = ctk.CTkImage(dark_image=Image.open("I.png"), size=(300, 400))
    imagen2I = ctk.CTkImage(dark_image=Image.open("iglesia.png"), size=(400, 400))
    
    letraI_label = ctk.CTkLabel(letra_i_frame, image=letraI, text="LETRA I/i:", compound="bottom")
    imagen1I_label = ctk.CTkLabel(letra_i_frame, image=imagen1I, text="Seña:", compound="bottom")
    imagen2I_label = ctk.CTkLabel(letra_i_frame, image=imagen2I, text="Otra palabra con esta letra: Iglesia", compound="bottom")
   
   
    letraI_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraI_label.configure(bg_color='#101652')
    letraI_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1I_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1I_label.configure(bg_color='#0c8f8f')
    imagen1I_label.configure(font=("Cooper Black", 40))
    
    imagen2I_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2I_label.configure(bg_color='#0c8f8f')
    imagen2I_label.configure(font=("Cooper Black", 40))
    
    I_label = ctk.CTkLabel(letra_i_frame, text="I de iguana.")
    I_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    I_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    I_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_i():
    show_abecedario()
    letra_i_frame.place_forget()
    pág_siguiente_i_button.place_forget()
    pág_anterior_i_button.place_forget()
    
def pág_siguiente_i():
    letra_j()
    letra_i_frame.place_forget()
    
    
def pág_anterior_i():
    letra_h()
    letra_i_frame.place_forget()

#Función J
def letra_j():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_j_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_j_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_j_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_j_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_j_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraJ = ctk.CTkImage(dark_image=Image.open("letraJ.png"), size=(250, 250))
    imagen1J = ctk.CTkImage(dark_image=Image.open("J.png"), size=(300, 400))
    imagen2J = ctk.CTkImage(dark_image=Image.open("jarra.png"), size=(400, 400))
    
    letraJ_label = ctk.CTkLabel(letra_j_frame, image=letraJ, text="LETRA J/j:", compound="bottom")
    imagen1J_label = ctk.CTkLabel(letra_j_frame, image=imagen1J, text="Seña:", compound="bottom")
    imagen2J_label = ctk.CTkLabel(letra_j_frame, image=imagen2J, text="Otra palabra con esta letra: Jarra", compound="bottom")
   
   
    letraJ_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraJ_label.configure(bg_color='#101652')
    letraJ_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1J_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1J_label.configure(bg_color='#0c8f8f')
    imagen1J_label.configure(font=("Cooper Black", 40))
    
    imagen2J_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2J_label.configure(bg_color='#0c8f8f')
    imagen2J_label.configure(font=("Cooper Black", 40))
    
    J_label = ctk.CTkLabel(letra_j_frame, text="J de jirafa.")
    J_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    J_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    J_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_j():
    show_abecedario()
    letra_j_frame.place_forget()
    pág_siguiente_j_button.place_forget()
    pág_anterior_j_button.place_forget()
    
def pág_siguiente_j():
    letra_k()
    letra_j_frame.place_forget()
    
def pág_anterior_j():
    letra_i()
    letra_j_frame.place_forget()

#Función K
def letra_k():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_k_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_k_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_k_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_k_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_k_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraK = ctk.CTkImage(dark_image=Image.open("letraK.png"), size=(250, 250))
    imagen1K = ctk.CTkImage(dark_image=Image.open("K.png"), size=(300, 400))
    imagen2K = ctk.CTkImage(dark_image=Image.open("kiwi.png"), size=(400, 400))
    
    letraK_label = ctk.CTkLabel(letra_k_frame, image=letraK, text="LETRA K/k:", compound="bottom")
    imagen1K_label = ctk.CTkLabel(letra_k_frame, image=imagen1K, text="Seña:", compound="bottom")
    imagen2K_label = ctk.CTkLabel(letra_k_frame, image=imagen2K, text="Otra palabra con esta letra: Kiwi", compound="bottom")
   
   
    letraK_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraK_label.configure(bg_color='#101652')
    letraK_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1K_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1K_label.configure(bg_color='#0c8f8f')
    imagen1K_label.configure(font=("Cooper Black", 40))
    
    imagen2K_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2K_label.configure(bg_color='#0c8f8f')
    imagen2K_label.configure(font=("Cooper Black", 40))
    
    K_label = ctk.CTkLabel(letra_k_frame, text="K de koala.")
    K_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    K_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    K_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_k():
    show_abecedario()
    letra_k_frame.place_forget()
    pág_siguiente_k_button.place_forget()
    pág_anterior_k_button.place_forget()
    
def pág_siguiente_k():
    letra_l()
    letra_k_frame.place_forget()
    
def pág_anterior_k():
    letra_j()
    letra_k_frame.place_forget()

#Función L
def letra_l():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_l_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_l_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_l_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_l_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_l_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraL = ctk.CTkImage(dark_image=Image.open("letraL.png"), size=(250, 250))
    imagen1L = ctk.CTkImage(dark_image=Image.open("L.png"), size=(300, 400))
    imagen2L = ctk.CTkImage(dark_image=Image.open("lámpara.png"), size=(400, 400))
    
    letraL_label = ctk.CTkLabel(letra_l_frame, image=letraL, text="LETRA L/l:", compound="bottom")
    imagen1L_label = ctk.CTkLabel(letra_l_frame, image=imagen1L, text="Seña:", compound="bottom")
    imagen2L_label = ctk.CTkLabel(letra_l_frame, image=imagen2L, text="Otra palabra con esta letra: Lámpara", compound="bottom")
   
   
    letraL_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraL_label.configure(bg_color='#101652')
    letraL_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1L_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1L_label.configure(bg_color='#0c8f8f')
    imagen1L_label.configure(font=("Cooper Black", 40))
    
    imagen2L_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2L_label.configure(bg_color='#0c8f8f')
    imagen2L_label.configure(font=("Cooper Black", 40))
    
    L_label = ctk.CTkLabel(letra_l_frame, text="L de león.")
    L_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    L_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    L_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_l():
    show_abecedario()
    letra_l_frame.place_forget()
    pág_siguiente_l_button.place_forget()
    pág_anterior_l_button.place_forget()
    
def pág_siguiente_l():
    letra_m()
    letra_l_frame.place_forget()
    
def pág_anterior_l():
    letra_k()
    letra_l_frame.place_forget()

#Función M
def letra_m():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_m_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_m_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_m_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_m_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_m_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraM = ctk.CTkImage(dark_image=Image.open("letraM.png"), size=(250, 250))
    imagen1M = ctk.CTkImage(dark_image=Image.open("M.png"), size=(300, 400))
    imagen2M = ctk.CTkImage(dark_image=Image.open("moto.png"), size=(400, 400))
    
    letraM_label = ctk.CTkLabel(letra_m_frame, image=letraM, text="LETRA M/m:", compound="bottom")
    imagen1M_label = ctk.CTkLabel(letra_m_frame, image=imagen1M, text="Seña:", compound="bottom")
    imagen2M_label = ctk.CTkLabel(letra_m_frame, image=imagen2M, text="Otra palabra con esta letra: Motocicleta", compound="bottom")
   
   
    letraM_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraM_label.configure(bg_color='#101652')
    letraM_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1M_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1M_label.configure(bg_color='#0c8f8f')
    imagen1M_label.configure(font=("Cooper Black", 40))
    
    imagen2M_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2M_label.configure(bg_color='#0c8f8f')
    imagen2M_label.configure(font=("Cooper Black", 40))
    
    M_label = ctk.CTkLabel(letra_m_frame, text="M de mono.")
    M_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    M_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    M_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_m():
    show_abecedario()
    letra_m_frame.place_forget()
    pág_siguiente_m_button.place_forget()
    pág_anterior_m_button.place_forget()
    
def pág_siguiente_m():
    letra_n()
    letra_m_frame.place_forget()
    
def pág_anterior_m():
    letra_l()
    letra_m_frame.place_forget()

#Función N
def letra_n():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_n_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_n_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_n_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_n_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_n_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraN = ctk.CTkImage(dark_image=Image.open("letraN.png"), size=(250, 250))
    imagen1N = ctk.CTkImage(dark_image=Image.open("N.png"), size=(300, 400))
    imagen2N = ctk.CTkImage(dark_image=Image.open("nido.png"), size=(400, 400))
    
    letraN_label = ctk.CTkLabel(letra_n_frame, image=letraN, text="LETRA N/n:", compound="bottom")
    imagen1N_label = ctk.CTkLabel(letra_n_frame, image=imagen1N, text="Seña:", compound="bottom")
    imagen2N_label = ctk.CTkLabel(letra_n_frame, image=imagen2N, text="Otra palabra con esta letra: Nido", compound="bottom")
   
   
    letraN_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraN_label.configure(bg_color='#101652')
    letraN_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1N_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1N_label.configure(bg_color='#0c8f8f')
    imagen1N_label.configure(font=("Cooper Black", 40))
    
    imagen2N_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2N_label.configure(bg_color='#0c8f8f')
    imagen2N_label.configure(font=("Cooper Black", 40))
    
    N_label = ctk.CTkLabel(letra_n_frame, text="N de naranja.")
    N_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    N_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    N_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_n():
    show_abecedario()
    letra_n_frame.place_forget()
    pág_siguiente_n_button.place_forget()
    pág_anterior_n_button.place_forget()
    
def pág_siguiente_n():
    letra_ñ()
    letra_n_frame.place_forget()
    
def pág_anterior_n():
    letra_m()
    letra_n_frame.place_forget()
    
#Función Ñ
def letra_ñ():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_ñ_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_ñ_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_ñ_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_ñ_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_ñ_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraÑ = ctk.CTkImage(dark_image=Image.open("letraÑ.png"), size=(250, 250))
    imagen1Ñ = ctk.CTkImage(dark_image=Image.open("Ñ.png"), size=(300, 400))
    imagen2Ñ = ctk.CTkImage(dark_image=Image.open("ñandu.png"), size=(400, 400))

    letraÑ_label = ctk.CTkLabel(letra_ñ_frame, image=letraÑ, text="LETRA Ñ/ñ:", compound="bottom")
    imagen1Ñ_label = ctk.CTkLabel(letra_ñ_frame, image=imagen1Ñ, text="Seña:", compound="bottom")
    imagen2Ñ_label = ctk.CTkLabel(letra_ñ_frame, image=imagen2Ñ, text="Otra palabra con esta letra: Ñandú", compound="bottom")
   
   
    letraÑ_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraÑ_label.configure(bg_color='#101652')
    letraÑ_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1Ñ_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1Ñ_label.configure(bg_color='#0c8f8f')
    imagen1Ñ_label.configure(font=("Cooper Black", 40))
    
    imagen2Ñ_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2Ñ_label.configure(bg_color='#0c8f8f')
    imagen2Ñ_label.configure(font=("Cooper Black", 40))
    
    Ñ_label = ctk.CTkLabel(letra_ñ_frame, text="Ñ de Ñu.")
    Ñ_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    Ñ_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    Ñ_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_ñ():
    show_abecedario()
    letra_ñ_frame.place_forget()
    pág_siguiente_ñ_button.place_forget()
    pág_anterior_ñ_button.place_forget()
    
def pág_siguiente_ñ():
    letra_o()
    letra_ñ_frame.place_forget()
    
def pág_anterior_ñ():
    letra_n()
    letra_ñ_frame.place_forget()


#Función O
def letra_o():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_o_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_o_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_o_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_o_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_o_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraO = ctk.CTkImage(dark_image=Image.open("letraO.png"), size=(250, 250))
    imagen1O = ctk.CTkImage(dark_image=Image.open("O.png"), size=(300, 400))
    imagen2O = ctk.CTkImage(dark_image=Image.open("ojo.png"), size=(400, 400))
    
    letraO_label = ctk.CTkLabel(letra_o_frame, image=letraO, text="LETRA O/o:", compound="bottom")
    imagen1O_label = ctk.CTkLabel(letra_o_frame, image=imagen1O, text="Seña:", compound="bottom")
    imagen2O_label = ctk.CTkLabel(letra_o_frame, image=imagen2O, text="Otra palabra con esta letra: Ojo", compound="bottom")
   
   
    letraO_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraO_label.configure(bg_color='#101652')
    letraO_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1O_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1O_label.configure(bg_color='#0c8f8f')
    imagen1O_label.configure(font=("Cooper Black", 40))
    
    imagen2O_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2O_label.configure(bg_color='#0c8f8f')
    imagen2O_label.configure(font=("Cooper Black", 40))
    
    O_label = ctk.CTkLabel(letra_o_frame, text="O de oso.")
    O_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    O_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    O_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_o():
    show_abecedario()
    letra_o_frame.place_forget()
    pág_siguiente_o_button.place_forget()
    pág_anterior_o_button.place_forget()
    
def pág_siguiente_o():
    letra_p()
    letra_o_frame.place_forget()
    
def pág_anterior_o():
    letra_ñ()
    letra_o_frame.place_forget()

#Función P
def letra_p():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_p_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_p_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_p_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_p_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_p_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraP = ctk.CTkImage(dark_image=Image.open("letraP.png"), size=(250, 250))
    imagen1P = ctk.CTkImage(dark_image=Image.open("P.png"), size=(300, 400))
    imagen2P = ctk.CTkImage(dark_image=Image.open("perro.jpg"), size=(400, 400))
    
    letraP_label = ctk.CTkLabel(letra_p_frame, image=letraP, text="LETRA P/p:", compound="bottom")
    imagen1P_label = ctk.CTkLabel(letra_p_frame, image=imagen1P, text="Seña:", compound="bottom")
    imagen2P_label = ctk.CTkLabel(letra_p_frame, image=imagen2P, text="Otra palabra con esta letra: Perro/a", compound="bottom")
   
   
    letraP_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraP_label.configure(bg_color='#101652')
    letraP_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1P_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1P_label.configure(bg_color='#0c8f8f')
    imagen1P_label.configure(font=("Cooper Black", 40))
    
    imagen2P_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2P_label.configure(bg_color='#0c8f8f')
    imagen2P_label.configure(font=("Cooper Black", 40))
    
    P_label = ctk.CTkLabel(letra_p_frame, text="P de panda.")
    P_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    P_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    P_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_p():
    show_abecedario()
    letra_p_frame.place_forget()
    pág_siguiente_p_button.place_forget()
    pág_anterior_p_button.place_forget()
    
def pág_siguiente_p():
    letra_q()
    letra_p_frame.place_forget()
    
def pág_anterior_p():
    letra_o()
    letra_p_frame.place_forget()

#Función Q
def letra_q():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_q_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_q_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_q_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_q_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_q_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraQ = ctk.CTkImage(dark_image=Image.open("letraQ.png"), size=(250, 250))
    imagen1Q = ctk.CTkImage(dark_image=Image.open("Q.png"), size=(300, 400))
    imagen2Q = ctk.CTkImage(dark_image=Image.open("quena.png"), size=(400, 400))
    
    letraQ_label = ctk.CTkLabel(letra_q_frame, image=letraQ, text="LETRA Q/q:", compound="bottom")
    imagen1Q_label = ctk.CTkLabel(letra_q_frame, image=imagen1Q, text="Seña:", compound="bottom")
    imagen2Q_label = ctk.CTkLabel(letra_q_frame, image=imagen2Q, text="Otra palabra con esta letra: Quena", compound="bottom")
   
   
    letraQ_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraQ_label.configure(bg_color='#101652')
    letraQ_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1Q_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1Q_label.configure(bg_color='#0c8f8f')
    imagen1Q_label.configure(font=("Cooper Black", 40))
    
    imagen2Q_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2Q_label.configure(bg_color='#0c8f8f')
    imagen2Q_label.configure(font=("Cooper Black", 40))
    
    Q_label = ctk.CTkLabel(letra_q_frame, text="Q de queso.")
    Q_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    Q_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    Q_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_q():
    show_abecedario()
    letra_q_frame.place_forget()
    pág_siguiente_q_button.place_forget()
    pág_anterior_q_button.place_forget()
    
def pág_siguiente_q():
    letra_r()
    letra_q_frame.place_forget()
    
def pág_anterior_q():
    letra_p()
    letra_q_frame.place_forget()

#Función R
def letra_r():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_r_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_r_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_r_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_r_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_r_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraR = ctk.CTkImage(dark_image=Image.open("letraR.png"), size=(250, 250))
    imagen1R = ctk.CTkImage(dark_image=Image.open("R.png"), size=(300, 400))
    imagen2R = ctk.CTkImage(dark_image=Image.open("reloj.png"), size=(400, 400))
    
    letraR_label = ctk.CTkLabel(letra_r_frame, image=letraR, text="LETRA R/r:", compound="bottom")
    imagen1R_label = ctk.CTkLabel(letra_r_frame, image=imagen1R, text="Seña:", compound="bottom")
    imagen2R_label = ctk.CTkLabel(letra_r_frame, image=imagen2R, text="Otra palabra con esta letra: Reloj", compound="bottom")
   
   
    letraR_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraR_label.configure(bg_color='#101652')
    letraR_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1R_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1R_label.configure(bg_color='#0c8f8f')
    imagen1R_label.configure(font=("Cooper Black", 40))
    
    imagen2R_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2R_label.configure(bg_color='#0c8f8f')
    imagen2R_label.configure(font=("Cooper Black", 40))
    
    R_label = ctk.CTkLabel(letra_r_frame, text="R de ratón.")
    R_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    R_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    R_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_r():
    show_abecedario()
    letra_r_frame.place_forget()
    pág_siguiente_r_button.place_forget()
    pág_anterior_r_button.place_forget()
    
def pág_siguiente_r():
    letra_s()
    letra_r_frame.place_forget()
    
def pág_anterior_r():
    letra_q()
    letra_r_frame.place_forget()

#Función S
def letra_s():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_s_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_s_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_s_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_s_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_s_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraS = ctk.CTkImage(dark_image=Image.open("letraS.png"), size=(250, 250))
    imagen1S = ctk.CTkImage(dark_image=Image.open("S.png"), size=(300, 400))
    imagen2S = ctk.CTkImage(dark_image=Image.open("silla.png"), size=(400, 400))
    
    letraS_label = ctk.CTkLabel(letra_s_frame, image=letraS, text="LETRA S/s:", compound="bottom")
    imagen1S_label = ctk.CTkLabel(letra_s_frame, image=imagen1S, text="Seña:", compound="bottom")
    imagen2S_label = ctk.CTkLabel(letra_s_frame, image=imagen2S, text="Otra palabra con esta letra: Silla", compound="bottom")
   
   
    letraS_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraS_label.configure(bg_color='#101652')
    letraS_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1S_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1S_label.configure(bg_color='#0c8f8f')
    imagen1S_label.configure(font=("Cooper Black", 40))
    
    imagen2S_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2S_label.configure(bg_color='#0c8f8f')
    imagen2S_label.configure(font=("Cooper Black", 40))
    
    S_label = ctk.CTkLabel(letra_s_frame, text="S de serpiente.")
    S_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    S_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    S_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_s():
    show_abecedario()
    letra_s_frame.place_forget()
    pág_siguiente_s_button.place_forget()
    pág_anterior_s_button.place_forget()
    
def pág_siguiente_s():
    letra_t()
    letra_s_frame.place_forget()
    
def pág_anterior_s():
    letra_r()
    letra_s_frame.place_forget()
    
#Función T
def letra_t():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_t_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_t_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_t_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_t_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_t_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraT = ctk.CTkImage(dark_image=Image.open("letraT.png"), size=(250, 250))
    imagen1T = ctk.CTkImage(dark_image=Image.open("T.png"), size=(300, 400))
    imagen2T = ctk.CTkImage(dark_image=Image.open("torta.png"), size=(400, 400))
    
    letraT_label = ctk.CTkLabel(letra_t_frame, image=letraT, text="LETRA T/t:", compound="bottom")
    imagen1T_label = ctk.CTkLabel(letra_t_frame, image=imagen1T, text="Seña:", compound="bottom")
    imagen2T_label = ctk.CTkLabel(letra_t_frame, image=imagen2T, text="Otra palabra con esta letra: Torta", compound="bottom")
   
   
    letraT_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraT_label.configure(bg_color='#101652')
    letraT_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1T_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1T_label.configure(bg_color='#0c8f8f')
    imagen1T_label.configure(font=("Cooper Black", 40))
    
    imagen2T_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2T_label.configure(bg_color='#0c8f8f')
    imagen2T_label.configure(font=("Cooper Black", 40))
    
    T_label = ctk.CTkLabel(letra_t_frame, text="T de tortuga.")
    T_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    T_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    T_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_t():
    show_abecedario()
    letra_t_frame.place_forget()
    pág_siguiente_t_button.place_forget()
    pág_anterior_t_button.place_forget()
    
def pág_siguiente_t():
    letra_u()
    letra_t_frame.place_forget()
    
def pág_anterior_t():
    letra_s()
    letra_t_frame.place_forget()

#Función U
def letra_u():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_u_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_u_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_u_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_u_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_u_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraU = ctk.CTkImage(dark_image=Image.open("letraU.png"), size=(250, 250))
    imagen1U = ctk.CTkImage(dark_image=Image.open("U.png"), size=(300, 400))
    imagen2U = ctk.CTkImage(dark_image=Image.open("uña.png"), size=(400, 400))
    
    letraU_label = ctk.CTkLabel(letra_u_frame, image=letraU, text="LETRA U/u:", compound="bottom")
    imagen1U_label = ctk.CTkLabel(letra_u_frame, image=imagen1U, text="Seña:", compound="bottom")
    imagen2U_label = ctk.CTkLabel(letra_u_frame, image=imagen2U, text="Otra palabra con esta letra: Uña", compound="bottom")
   
   
    letraU_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraU_label.configure(bg_color='#101652')
    letraU_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1U_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1U_label.configure(bg_color='#0c8f8f')
    imagen1U_label.configure(font=("Cooper Black", 40))
    
    imagen2U_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2U_label.configure(bg_color='#0c8f8f')
    imagen2U_label.configure(font=("Cooper Black", 40))
    
    U_label = ctk.CTkLabel(letra_u_frame, text="U de uva.")
    U_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    U_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    U_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_u():
    show_abecedario()
    letra_u_frame.place_forget()
    pág_siguiente_u_button.place_forget()
    pág_anterior_u_button.place_forget()
    

def pág_siguiente_u():
    letra_v()
    letra_u_frame.place_forget()
    
def pág_anterior_u():
    letra_t()
    letra_u_frame.place_forget()

#Función V
def letra_v():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_v_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_v_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_v_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_v_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_v_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraV = ctk.CTkImage(dark_image=Image.open("letraV.png"), size=(250, 250))
    imagen1V = ctk.CTkImage(dark_image=Image.open("V.png"), size=(300, 400))
    imagen2V = ctk.CTkImage(dark_image=Image.open("vino.png"), size=(400, 400))
    
    letraV_label = ctk.CTkLabel(letra_v_frame, image=letraV, text="LETRA V/v:", compound="bottom")
    imagen1V_label = ctk.CTkLabel(letra_v_frame, image=imagen1V, text="Seña:", compound="bottom")
    imagen2V_label = ctk.CTkLabel(letra_v_frame, image=imagen2V, text="Otra palabra con esta letra: Vino", compound="bottom")
   
   
    letraV_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraV_label.configure(bg_color='#101652')
    letraV_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1V_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1V_label.configure(bg_color='#0c8f8f')
    imagen1V_label.configure(font=("Cooper Black", 40))
    
    imagen2V_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2V_label.configure(bg_color='#0c8f8f')
    imagen2V_label.configure(font=("Cooper Black", 40))
    
    V_label = ctk.CTkLabel(letra_v_frame, text="V de vaca.")
    V_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    V_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    V_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_v():
    show_abecedario()
    letra_v_frame.place_forget()
    pág_siguiente_v_button.place_forget()
    pág_anterior_v_button.place_forget()
    
def pág_siguiente_v():
    letra_w()
    letra_v_frame.place_forget()
    
def pág_anterior_v():
    letra_u()
    letra_v_frame.place_forget()

#Función W
def letra_w():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_w_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_w_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_w_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_w_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_w_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraW = ctk.CTkImage(dark_image=Image.open("letraW.png"), size=(250, 250))
    imagen1W = ctk.CTkImage(dark_image=Image.open("W.png"), size=(300, 400))
    imagen2W = ctk.CTkImage(dark_image=Image.open("wafle.png"), size=(400, 400))
    
    letraW_label = ctk.CTkLabel(letra_w_frame, image=letraW, text="LETRA W/w:", compound="bottom")
    imagen1W_label = ctk.CTkLabel(letra_w_frame, image=imagen1W, text="Seña:", compound="bottom")
    imagen2W_label = ctk.CTkLabel(letra_w_frame, image=imagen2W, text="Otra palabra con esta letra: Wafle", compound="bottom")
   
   
    letraW_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraW_label.configure(bg_color='#101652')
    letraW_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1W_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1W_label.configure(bg_color='#0c8f8f')
    imagen1W_label.configure(font=("Cooper Black", 40))
    
    imagen2W_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2W_label.configure(bg_color='#0c8f8f')
    imagen2W_label.configure(font=("Cooper Black", 40))
    
    W_label = ctk.CTkLabel(letra_w_frame, text="W de Wi-Fi.")
    W_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    W_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    W_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_w():
    show_abecedario()
    letra_w_frame.place_forget()
    pág_siguiente_w_button.place_forget()
    pág_anterior_w_button.place_forget()
    
def pág_siguiente_w():
    letra_x()
    letra_w_frame.place_forget()
    
def pág_anterior_w():
    letra_v()
    letra_w_frame.place_forget()

#Función X
def letra_x():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_x_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_x_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_x_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_x_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_x_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraX = ctk.CTkImage(dark_image=Image.open("letraX.png"), size=(250, 250))
    imagen1X = ctk.CTkImage(dark_image=Image.open("X.png"), size=(300, 400))
    
    letraX_label = ctk.CTkLabel(letra_x_frame, image=letraX, text="LETRA X/x:", compound="bottom")
    imagen1X_label = ctk.CTkLabel(letra_x_frame, image=imagen1X, text="Seña:", compound="bottom")
   
   
    letraX_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraX_label.configure(bg_color='#101652')
    letraX_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1X_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1X_label.configure(bg_color='#0c8f8f')
    imagen1X_label.configure(font=("Cooper Black", 40))
    
    
    X_label = ctk.CTkLabel(letra_x_frame, text="X de xilofono.")
    X_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    X_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    X_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_x():
    show_abecedario()
    letra_x_frame.place_forget()
    pág_siguiente_x_button.place_forget()
    pág_anterior_x_button.place_forget()
    
def pág_siguiente_x():
    letra_y()
    letra_x_frame.place_forget()
    
def pág_anterior_x():
    letra_w()
    letra_x_frame.place_forget()

#Función Y
def letra_y():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_y_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_y_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_y_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_siguiente_y_button.place(relx=0.95, rely=0.05, anchor="ne")
    pág_anterior_y_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraY = ctk.CTkImage(dark_image=Image.open("letraY.png"), size=(250, 250))
    imagen1Y = ctk.CTkImage(dark_image=Image.open("Y.png"), size=(300, 400))
    imagen2Y = ctk.CTkImage(dark_image=Image.open("yema.png"), size=(400, 400))
    
    letraY_label = ctk.CTkLabel(letra_y_frame, image=letraY, text="LETRA Y/y:", compound="bottom")
    imagen1Y_label = ctk.CTkLabel(letra_y_frame, image=imagen1Y, text="Seña:", compound="bottom")
    imagen2Y_label = ctk.CTkLabel(letra_y_frame, image=imagen2Y, text="Otra palabra con esta letra: Yema", compound="bottom")
   
   
    letraY_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraY_label.configure(bg_color='#101652')
    letraY_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1Y_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1Y_label.configure(bg_color='#0c8f8f')
    imagen1Y_label.configure(font=("Cooper Black", 40))
    
    imagen2Y_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2Y_label.configure(bg_color='#0c8f8f')
    imagen2Y_label.configure(font=("Cooper Black", 40))
    
    Y_label = ctk.CTkLabel(letra_y_frame, text="Y de yoyo.")
    Y_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    Y_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    Y_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_y():
    show_abecedario()
    letra_y_frame.place_forget()
    pág_siguiente_y_button.place_forget()
    pág_anterior_y_button.place_forget()
    
def pág_siguiente_y():
    letra_z()
    letra_y_frame.place_forget()
    
def pág_anterior_y():
    letra_x()
    letra_y_frame.place_forget()

#Función Z
def letra_z():
    reproducir_sonidoClick()
    hide_current_screen()
    letra_z_frame.place(relx=0.5, rely=0.5, anchor="center")
    letra_z_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_letra_z_button.grid(row=7, column=0, pady=20, columnspan=4)
    pág_anterior_z_button.place(relx=0.05, rely=0.05, anchor="nw")
    
    letraZ = ctk.CTkImage(dark_image=Image.open("letraZ.png"), size=(250, 250))
    imagen1Z = ctk.CTkImage(dark_image=Image.open("Z.png"), size=(300, 400))
    imagen2Z = ctk.CTkImage(dark_image=Image.open("zapato.png"), size=(400, 400))
    
    letraZ_label = ctk.CTkLabel(letra_z_frame, image=letraZ, text="LETRA Z/z:", compound="bottom")
    imagen1Z_label = ctk.CTkLabel(letra_z_frame, image=imagen1Z, text="Seña:", compound="bottom")
    imagen2Z_label = ctk.CTkLabel(letra_z_frame, image=imagen2Z, text="Otra palabra con esta letra: Zapato", compound="bottom")
   
   
    letraZ_label.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    letraZ_label.configure(bg_color='#101652')
    letraZ_label.configure(font=("Bodoni MT Black", 50))
    
    imagen1Z_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    imagen1Z_label.configure(bg_color='#0c8f8f')
    imagen1Z_label.configure(font=("Cooper Black", 40))
    
    imagen2Z_label.grid(row=1, column=2, padx=(20, 40), pady=(20, 40))
    imagen2Z_label.configure(bg_color='#0c8f8f')
    imagen2Z_label.configure(font=("Cooper Black", 40))
    
    Z_label = ctk.CTkLabel(letra_z_frame, text="Z de zorro.")
    Z_label.grid(row=0, column=2, padx=(20, 40), pady=(20, 40))
    Z_label.configure(bg_color="#0c8f8f", text_color="#e8bf56")
    Z_label.configure(font=("Cooper Black", 70))
    
def volver_al_menu_letra_z():
    show_abecedario()
    letra_z_frame.place_forget()
    pág_anterior_z_button.place_forget()
    
def pág_anterior_z():
    letra_y()
    letra_z_frame.place_forget()


#familia funciones

def show_familia():
    reproducir_sonidoClick()
    hide_current_screen()

    familia_frame.place(relx=0.5, rely=0.5, anchor="center")
    familia_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    familia_fondo = ctk.CTkImage(dark_image=Image.open("familia fondo.png"), size=(630, 200))
    familia_fondo_label = ctk.CTkLabel(root, image=familia_fondo, text="", bg_color="#0c8f8f")
    familia_fondo_label.place(relx=0.5, rely=0.863, anchor="center")

    familia1_button.grid(row=0, column=0, padx=(20, 40), pady=(20, 40), columnspan=2)
    padres_button.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    hijos_button.grid(row=1, column=1, padx=(20, 40), pady=(20, 40))
    mamá_button.grid(row=2, column=0, padx=(20, 40), pady=(20, 40))
    papá_button.grid(row=2, column=1, padx=(20, 40), pady=(20, 40))
    hermano_a_button.grid(row=3, column=0, padx=(20, 40), pady=(20, 40))
    abuelo_a_button.grid(row=3, column=1, padx=(20, 40), pady=(20, 40))
    tío_a_button.grid(row=4, column=0, padx=(20, 40), pady=(20, 40))
    primo_a_button.grid(row=4, column=1, padx=(20, 40), pady=(20, 40))
    volver_menu_familia_button.grid(row=7, column=0, padx=(20, 40), pady=(20, 40), columnspan=2)


def volver_al_menu_familia():
    reproducir_sonidoClick()
    show_menu()
    familia_frame.place_forget()
    
#Función mamá
def mamá():
    reproducir_sonidoClick()
    hide_current_screen()
    mamá_frame.place(relx=0.5, rely=0.5, anchor="center")
    mamá_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_mamá_button.grid(row=7, column=0, pady=20, columnspan=4)
    
 
    gif_image = Image.open("Mamá.gif")
    gif_frames = gif_image.n_frames

    converted_frames = []
    for frame in range(gif_frames):
        gif_image.seek(frame)
        converted_frame = ImageTk.PhotoImage(gif_image)
        converted_frames.append(converted_frame)

  
    gif_label = ctk.CTkLabel(mamá_frame, text="M-A-M-Á", compound="bottom", image=converted_frames[0])
    gif_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    gif_label.configure(font=("Cooper Black", 50))

  
    def update_gif(frame):
        gif_label.configure(image=converted_frames[frame])


    frame_index = 0

    def animate_gif():
        nonlocal frame_index
        update_gif(frame_index)
        frame_index = (frame_index + 1) % gif_frames
        mamá_frame.after(100, animate_gif)

    animate_gif()

def volver_al_menu_mamá():
    show_familia()
    mamá_frame.place_forget()

#Función papá
def papá():
    reproducir_sonidoClick()
    hide_current_screen()
    papá_frame.place(relx=0.5, rely=0.5, anchor="center")
    papá_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_papá_button.grid(row=7, column=0, pady=20, columnspan=4)

    
 
    gif_image = Image.open("Papá.gif")
    gif_frames = gif_image.n_frames

    converted_frames = []
    for frame in range(gif_frames):
        gif_image.seek(frame)
        converted_frame = ImageTk.PhotoImage(gif_image)
        converted_frames.append(converted_frame)

  
    gif_label = ctk.CTkLabel(papá_frame, text="P-A-P-Á", compound="bottom", image=converted_frames[0])
    gif_label.grid(row=1, column=0, padx=(20, 40), pady=(20, 40))
    gif_label.configure(font=("Cooper Black", 50))

  
    def update_gif(frame):
        gif_label.configure(image=converted_frames[frame])


    frame_index = 0

    def animate_gif():
        nonlocal frame_index
        update_gif(frame_index)
        frame_index = (frame_index + 1) % gif_frames
        papá_frame.after(100, animate_gif)

    animate_gif()

    
def volver_al_menu_papá():
    show_familia()
    papá_frame.place_forget()
    
#Función hermano/a

def hermano_a():
    reproducir_sonidoClick()
    hide_current_screen()
    hermano_a_frame.place(relx=0.5, rely=0.5, anchor="center")
    hermano_a_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")

    volver_menu_hermano_a_button.grid(row=7, column=0, pady=20, columnspan=4)

    gif_image_hermano = Image.open("Hermano.gif")
    gif_frames_hermano = gif_image_hermano.n_frames

    converted_frames_hermano = []
    for frame in range(gif_frames_hermano):
        gif_image_hermano.seek(frame)
        converted_frame_hermano = ImageTk.PhotoImage(gif_image_hermano)
        converted_frames_hermano.append(converted_frame_hermano)

    gif_label_hermano = ctk.CTkLabel(hermano_a_frame, text="H-E-R-M-A-N-O", compound="bottom", image=converted_frames_hermano[0])
    gif_label_hermano.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_hermano.configure(font=("Cooper Black", 50))

    def update_gif_hermano(frame):
        gif_label_hermano.configure(image=converted_frames_hermano[frame])

    frame_index_hermano = 0

    def animate_gif_hermano():
        nonlocal frame_index_hermano
        update_gif_hermano(frame_index_hermano)
        frame_index_hermano = (frame_index_hermano + 1) % gif_frames_hermano
        hermano_a_frame.after(100, animate_gif_hermano)

    animate_gif_hermano()

    gif_image_hermana = Image.open("Hermana.gif")
    gif_frames_hermana = gif_image_hermana.n_frames

    converted_frames_hermana = []
    for frame in range(gif_frames_hermana):
        gif_image_hermana.seek(frame)
        converted_frame_hermana = ImageTk.PhotoImage(gif_image_hermana)
        converted_frames_hermana.append(converted_frame_hermana)

    gif_label_hermana = ctk.CTkLabel(hermano_a_frame, text="H-E-R-M-A-N-A", compound="bottom", image=converted_frames_hermana[0])
    gif_label_hermana.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    gif_label_hermana.configure(font=("Cooper Black", 50))

    def update_gif_hermana(frame):
        gif_label_hermana.configure(image=converted_frames_hermana[frame])

    frame_index_hermana = 0

    def animate_gif_hermana():
        nonlocal frame_index_hermana
        update_gif_hermana(frame_index_hermana)
        frame_index_hermana = (frame_index_hermana + 1) % gif_frames_hermana
        hermano_a_frame.after(100, animate_gif_hermana)

    animate_gif_hermana()

def volver_al_menu_hermano_a():
    show_familia()
    hermano_a_frame.place_forget()


#Función abuelo/a
def abuelo_a():
    reproducir_sonidoClick()
    hide_current_screen()
    abuelo_a_frame.place(relx=0.5, rely=0.5, anchor="center")
    abuelo_a_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_abuelo_a_button.grid(row=7, column=0, pady=20, columnspan=4)
    
    gif_image_abuelo = Image.open("Abuelo.gif")
    gif_frames_abuelo = gif_image_abuelo.n_frames

    converted_frames_abuelo = []
    for frame in range(gif_frames_abuelo):
        gif_image_abuelo.seek(frame)
        converted_frame_abuelo = ImageTk.PhotoImage(gif_image_abuelo)
        converted_frames_abuelo.append(converted_frame_abuelo)

    gif_label_abuelo = ctk.CTkLabel(abuelo_a_frame, text="A-B-U-E-L-O", compound="bottom", image=converted_frames_abuelo[0])
    gif_label_abuelo.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_abuelo.configure(font=("Cooper Black", 50))

    def update_gif_abuelo(frame):
        gif_label_abuelo.configure(image=converted_frames_abuelo[frame])

    frame_index_abuelo = 0

    def animate_gif_abuelo():
        nonlocal frame_index_abuelo
        update_gif_abuelo(frame_index_abuelo)
        frame_index_abuelo = (frame_index_abuelo+ 1) % gif_frames_abuelo
        abuelo_a_frame.after(100, animate_gif_abuelo)

    animate_gif_abuelo()

    gif_image_abuela = Image.open("Abuela.gif")
    gif_frames_abuela = gif_image_abuela.n_frames

    converted_frames_abuela = []
    for frame in range(gif_frames_abuela):
        gif_image_abuela.seek(frame)
        converted_frame_abuela = ImageTk.PhotoImage(gif_image_abuela)
        converted_frames_abuela.append(converted_frame_abuela)

    gif_label_abuela = ctk.CTkLabel(abuelo_a_frame, text="A-B-U-E-L-A", compound="bottom", image=converted_frames_abuela[0])
    gif_label_abuela.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    gif_label_abuela.configure(font=("Cooper Black", 50))

    def update_gif_abuela(frame):
        gif_label_abuela.configure(image=converted_frames_abuela[frame])

    frame_index_abuela = 0

    def animate_gif_abuela():
        nonlocal frame_index_abuela
        update_gif_abuela(frame_index_abuela)
        frame_index_abuela = (frame_index_abuela + 1) % gif_frames_abuela
        abuelo_a_frame.after(100, animate_gif_abuela)

    animate_gif_abuela()
    
def volver_al_menu_abuelo_a():
    show_familia()
    abuelo_a_frame.place_forget()

#Función tío/a
def tío_a():
    reproducir_sonidoClick()
    hide_current_screen()
    tío_a_frame.place(relx=0.5, rely=0.5, anchor="center")
    tío_a_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_tío_a_button.grid(row=7, column=0, pady=20, columnspan=4)
    
    gif_image_tío = Image.open("Tío.gif")
    gif_frames_tío = gif_image_tío.n_frames

    converted_frames_tío = []
    for frame in range(gif_frames_tío):
        gif_image_tío.seek(frame)
        converted_frame_tío = ImageTk.PhotoImage(gif_image_tío)
        converted_frames_tío.append(converted_frame_tío)

    gif_label_tío = ctk.CTkLabel(tío_a_frame, text="T-Í-O", compound="bottom", image=converted_frames_tío[0])
    gif_label_tío.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_tío.configure(font=("Cooper Black", 50))

    def update_gif_tío(frame):
        gif_label_tío.configure(image=converted_frames_tío[frame])

    frame_index_tío = 0

    def animate_gif_tío():
        nonlocal frame_index_tío
        update_gif_tío(frame_index_tío)
        frame_index_tío = (frame_index_tío+ 1) % gif_frames_tío
        tío_a_frame.after(100, animate_gif_tío)

    animate_gif_tío()

    gif_image_tía = Image.open("Tía.gif")
    gif_frames_tía = gif_image_tía.n_frames

    converted_frames_tía = []
    for frame in range(gif_frames_tía):
        gif_image_tía.seek(frame)
        converted_frame_tía = ImageTk.PhotoImage(gif_image_tía)
        converted_frames_tía.append(converted_frame_tía)

    gif_label_tía = ctk.CTkLabel(tío_a_frame, text="T-Í-A", compound="bottom", image=converted_frames_tía[0])
    gif_label_tía.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    gif_label_tía.configure(font=("Cooper Black", 50))

    def update_gif_tía(frame):
        gif_label_tía.configure(image=converted_frames_tía[frame])

    frame_index_tía = 0

    def animate_gif_tía():
        nonlocal frame_index_tía
        update_gif_tía(frame_index_tía)
        frame_index_tía = (frame_index_tía + 1) % gif_frames_tía
        tío_a_frame.after(100, animate_gif_tía)

    animate_gif_tía()
    
def volver_al_menu_tío_a():
    show_familia()
    tío_a_frame.place_forget()

#Función primo/a
def primo_a():
    reproducir_sonidoClick()
    hide_current_screen()
    primo_a_frame.place(relx=0.5, rely=0.5, anchor="center")
    primo_a_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_primo_a_button.grid(row=7, column=0, pady=20, columnspan=4)
    
    gif_image_primo = Image.open("Primo.gif")
    gif_frames_primo = gif_image_primo.n_frames

    converted_frames_primo = []
    for frame in range(gif_frames_primo):
        gif_image_primo.seek(frame)
        converted_frame_primo = ImageTk.PhotoImage(gif_image_primo)
        converted_frames_primo.append(converted_frame_primo)

    gif_label_primo= ctk.CTkLabel(primo_a_frame, text="P-R-I-M-O", compound="bottom", image=converted_frames_primo[0])
    gif_label_primo.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_primo.configure(font=("Cooper Black", 50))

    def update_gif_primo(frame):
        gif_label_primo.configure(image=converted_frames_primo[frame])

    frame_index_primo = 0

    def animate_gif_primo():
        nonlocal frame_index_primo
        update_gif_primo(frame_index_primo)
        frame_index_primo = (frame_index_primo+ 1) % gif_frames_primo
        primo_a_frame.after(100, animate_gif_primo)

    animate_gif_primo()

    gif_image_prima = Image.open("Prima.gif")
    gif_frames_prima = gif_image_prima.n_frames

    converted_frames_prima = []
    for frame in range(gif_frames_prima):
        gif_image_prima.seek(frame)
        converted_frame_prima = ImageTk.PhotoImage(gif_image_prima)
        converted_frames_prima.append(converted_frame_prima)

    gif_label_prima = ctk.CTkLabel(primo_a_frame, text="P-R-I-M-A", compound="bottom", image=converted_frames_prima[0])
    gif_label_prima.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    gif_label_prima.configure(font=("Cooper Black", 50))

    def update_gif_prima(frame):
        gif_label_prima.configure(image=converted_frames_prima[frame])

    frame_index_prima = 0

    def animate_gif_prima():
        nonlocal frame_index_prima
        update_gif_prima(frame_index_prima)
        frame_index_prima = (frame_index_prima + 1) % gif_frames_prima
        primo_a_frame.after(100, animate_gif_prima)

    animate_gif_prima()
def volver_al_menu_primo_a():
    show_familia()
    primo_a_frame.place_forget()
    
#Función Padres
def padres():
    reproducir_sonidoClick()
    hide_current_screen()
    padres_frame.place(relx=0.5, rely=0.5, anchor="center")
    padres_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_padres_button.grid(row=7, column=0, pady=20, columnspan=4)

    gif_image_padres = Image.open("Padres.gif")
    gif_frames_padres = gif_image_padres.n_frames

    converted_frames_padres = []
    for frame in range(gif_frames_padres):
        gif_image_padres.seek(frame)
        converted_frame_padres = ImageTk.PhotoImage(gif_image_padres)
        converted_frames_padres.append(converted_frame_padres)

    gif_label_padres = ctk.CTkLabel(padres_frame, text="P-A-D-R-E-S", compound="bottom", image=converted_frames_padres[0])
    gif_label_padres.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_padres.configure(font=("Cooper Black", 50))

    def update_gif_padres(frame):
        gif_label_padres.configure(image=converted_frames_padres[frame])

    frame_index_padres = 0

    def animate_gif_padres():
        nonlocal frame_index_padres
        update_gif_padres(frame_index_padres)
        frame_index_padres = (frame_index_padres + 1) % gif_frames_padres
        padres_frame.after(100, animate_gif_padres)

    animate_gif_padres()
 
      
def volver_al_menu_padres():
    show_familia()
    padres_frame.place_forget()
    
#Función Hijos
def hijos():
    reproducir_sonidoClick()
    hide_current_screen()
    hijos_frame.place(relx=0.5, rely=0.5, anchor="center")
    hijos_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_hijos_button.grid(row=7, column=0, pady=20, columnspan=4)

    gif_image_hijo = Image.open("Hijo.gif")
    gif_frames_hijo = gif_image_hijo.n_frames

    converted_frames_hijo = []
    for frame in range(gif_frames_hijo):
        gif_image_hijo.seek(frame)
        converted_frame_hijo = ImageTk.PhotoImage(gif_image_hijo)
        converted_frames_hijo.append(converted_frame_hijo)

    gif_label_hijo = ctk.CTkLabel(hijos_frame, text="H-I-J-O", compound="bottom", image=converted_frames_hijo[0])
    gif_label_hijo.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_hijo.configure(font=("Cooper Black", 50))

    def update_gif_hijo(frame):
        gif_label_hijo.configure(image=converted_frames_hijo[frame])

    frame_index_hijo = 0

    def animate_gif_hijo():
        nonlocal frame_index_hijo
        update_gif_hijo(frame_index_hijo)
        frame_index_hijo = (frame_index_hijo+ 1) % gif_frames_hijo
        hijos_frame.after(100, animate_gif_hijo)

    animate_gif_hijo()

    gif_image_hija = Image.open("Hija.gif")
    gif_frames_hija = gif_image_hija.n_frames

    converted_frames_hija = []
    for frame in range(gif_frames_hija):
        gif_image_hija.seek(frame)
        converted_frame_hija = ImageTk.PhotoImage(gif_image_hija)
        converted_frames_hija.append(converted_frame_hija)

    gif_label_hija = ctk.CTkLabel(hijos_frame, text="H-I-J-A", compound="bottom", image=converted_frames_hija[0])
    gif_label_hija.grid(row=0, column=0, padx=(20, 40), pady=(20, 40))
    gif_label_hija.configure(font=("Cooper Black", 50))

    def update_gif_hija(frame):
        gif_label_hija.configure(image=converted_frames_hija[frame])

    frame_index_hija = 0

    def animate_gif_hija():
        nonlocal frame_index_hija
        update_gif_hija(frame_index_hija)
        frame_index_hija = (frame_index_hija + 1) % gif_frames_hija
        hijos_frame.after(100, animate_gif_hija)

    animate_gif_hija()
 
      
def volver_al_menu_hijos():
    show_familia()
    hijos_frame.place_forget()
    
#Función familia
def familia1():
    reproducir_sonidoClick()
    hide_current_screen()
    familia1_frame.place(relx=0.5, rely=0.5, anchor="center")
    familia1_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_familia1_button.grid(row=7, column=0, pady=20, columnspan=4)

    gif_image_familia1 = Image.open("Familia.gif")
    gif_frames_familia1 = gif_image_familia1.n_frames

    converted_frames_familia1 = []
    for frame in range(gif_frames_familia1):
        gif_image_familia1.seek(frame)
        converted_frame_familia1 = ImageTk.PhotoImage(gif_image_familia1)
        converted_frames_familia1.append(converted_frame_familia1)

    gif_label_familia1 = ctk.CTkLabel(familia1_frame, text="F-A-M-I-L-I-A", compound="bottom", image=converted_frames_familia1[0])
    gif_label_familia1.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_familia1.configure(font=("Cooper Black", 50))

    def update_gif_familia1(frame):
        gif_label_familia1.configure(image=converted_frames_familia1[frame])

    frame_index_familia1 = 0

    def animate_gif_familia1():
        nonlocal frame_index_familia1
        update_gif_familia1(frame_index_familia1)
        frame_index_familia1 = (frame_index_familia1 + 1) % gif_frames_familia1
        familia1_frame.after(100, animate_gif_familia1)

    animate_gif_familia1()
 
      
def volver_al_menu_familia1():
    show_familia()
    familia1_frame.place_forget()


#saludos funciones

def show_saludos():
    reproducir_sonidoClick()
    hide_current_screen()
    saludos_frame.place(relx=0.5, rely=0.5, anchor="center")
    saludos_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")

    volver_menu_saludos_button.place(relx=0.5, rely=0.9, anchor="center")

    saludos_fondo = ctk.CTkImage(dark_image=Image.open("frases.jpg"), size=(750, 750))
    saludos_fondo_label = ctk.CTkLabel(saludos_frame, image=saludos_fondo, text="", bg_color="#0c8f8f")
    saludos_fondo_label.place(relx=0.5, rely=0.5, anchor="center")

    buscador_entry.place(relx=0.5, rely=0.05, anchor="center")

    buscador_button.place(relx=0.5, rely=0.10, anchor="center")

def volver_al_menu_saludos():
    show_menu()
    saludos_frame.place_forget()
    
#Hola

def hola():
    hide_current_screen()
    hola_frame.place(relx=0.5, rely=0.5, anchor="center")
    hola_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")

    volver_menu_hola_button.grid(row=7, column=0, pady=20, columnspan=4)

    gif_image_hola = Image.open("Hola.gif")
    gif_frames_hola = gif_image_hola.n_frames

    converted_frames_hola = []
    for frame in range(gif_frames_hola):
        gif_image_hola.seek(frame)
        converted_frame_hola = ImageTk.PhotoImage(gif_image_hola)
        converted_frames_hola.append(converted_frame_hola)

    gif_label_hola = ctk.CTkLabel(hola_frame, text="HOLA", compound="bottom", image=converted_frames_hola[0])
    gif_label_hola.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_hola.configure(font=("Cooper Black", 50))

    def update_gif_hola(frame):
        gif_label_hola.configure(image=converted_frames_hola[frame])

    frame_index_hola = 0

    def animate_gif_hola():
        nonlocal frame_index_hola
        update_gif_hola(frame_index_hola)
        frame_index_hola = (frame_index_hola + 1) % gif_frames_hola
        hola_frame.after(100, animate_gif_hola)

    animate_gif_hola()

    
def volver_al_menu_hola():
    show_saludos()
    hola_frame.place_forget()
    
#Adios

def adios():
    hide_current_screen()
    adios_frame.place(relx=0.5, rely=0.5, anchor="center")
    adios_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")

    volver_menu_adios_button.grid(row=7, column=0, pady=20, columnspan=4)

    gif_image_adios = Image.open("Adiós.gif")
    gif_frames_adios = gif_image_adios.n_frames

    converted_frames_adios = []
    for frame in range(gif_frames_adios):
        gif_image_adios.seek(frame)
        converted_frame_adios = ImageTk.PhotoImage(gif_image_adios)
        converted_frames_adios.append(converted_frame_adios)

    gif_label_adios = ctk.CTkLabel(adios_frame, text="ADIÓS", compound="bottom", image=converted_frames_adios[0])
    gif_label_adios.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_adios.configure(font=("Cooper Black", 50))

    def update_gif_adios(frame):
        gif_label_adios.configure(image=converted_frames_adios[frame])

    frame_index_adios = 0

    def animate_gif_adios():
        nonlocal frame_index_adios
        update_gif_adios(frame_index_adios)
        frame_index_adios = (frame_index_adios + 1) % gif_frames_adios
        adios_frame.after(100, animate_gif_adios)

    animate_gif_adios()
    
def volver_al_menu_adios():
    show_saludos()
    adios_frame.place_forget()

#Qué Tal

def queTal():
    hide_current_screen()
    queTal_frame.place(relx=0.5, rely=0.5, anchor="center")
    queTal_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_queTal_button.grid(row=7, column=0, pady=20, columnspan=4)
    
    gif_image_queTal = Image.open("Qué tal.gif")
    gif_frames_queTal = gif_image_queTal.n_frames

    converted_frames_queTal = []
    for frame in range(gif_frames_queTal):
        gif_image_queTal.seek(frame)
        converted_frame_queTal = ImageTk.PhotoImage(gif_image_queTal)
        converted_frames_queTal.append(converted_frame_queTal)

    gif_label_queTal= ctk.CTkLabel(queTal_frame, text="¿Qué tal?", compound="bottom", image=converted_frames_queTal[0])
    gif_label_queTal.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_queTal.configure(font=("Cooper Black", 50))

    def update_gif_queTal(frame):
        gif_label_queTal.configure(image=converted_frames_queTal[frame])

    frame_index_queTal = 0

    def animate_gif_queTal():
        nonlocal frame_index_queTal
        update_gif_queTal(frame_index_queTal)
        frame_index_queTal = (frame_index_queTal+ 1) % gif_frames_queTal
        queTal_frame.after(100, animate_gif_queTal)

    animate_gif_queTal()
    
def volver_al_menu_queTal():
    show_saludos()
    queTal_frame.place_forget()
    
#Bien
    
def bien():
    hide_current_screen()
    bien_frame.place(relx=0.5, rely=0.5, anchor="center")
    bien_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_bien_button.grid(row=7, column=0, pady=20, columnspan=4)
    
    gif_image_bien = Image.open("Bien.gif")
    gif_frames_bien = gif_image_bien.n_frames

    converted_frames_bien = []
    for frame in range(gif_frames_bien):
        gif_image_bien.seek(frame)
        converted_frame_bien = ImageTk.PhotoImage(gif_image_bien)
        converted_frames_bien.append(converted_frame_bien)

    gif_label_bien= ctk.CTkLabel(bien_frame, text="BIEN", compound="bottom", image=converted_frames_bien[0])
    gif_label_bien.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_bien.configure(font=("Cooper Black", 50))

    def update_gif_bien(frame):
        gif_label_bien.configure(image=converted_frames_bien[frame])

    frame_index_bien = 0

    def animate_gif_bien():
        nonlocal frame_index_bien
        update_gif_bien(frame_index_bien)
        frame_index_bien = (frame_index_bien+ 1) % gif_frames_bien
        bien_frame.after(100, animate_gif_bien)

    animate_gif_bien()
    
def volver_al_menu_bien():
    show_saludos()
    bien_frame.place_forget()

# Mal

def mal():
    hide_current_screen()
    mal_frame.place(relx=0.5, rely=0.5, anchor="center")
    mal_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_mal_button.grid(row=7, column=0, pady=20, columnspan=4)
    
    gif_image_mal = Image.open("Mal.gif")
    gif_frames_mal = gif_image_mal.n_frames

    converted_frames_mal = []
    for frame in range(gif_frames_mal):
        gif_image_mal.seek(frame)
        converted_frame_mal = ImageTk.PhotoImage(gif_image_mal)
        converted_frames_mal.append(converted_frame_mal)

    gif_label_mal= ctk.CTkLabel(mal_frame, text="MAL", compound="bottom", image=converted_frames_mal[0])
    gif_label_mal.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_mal.configure(font=("Cooper Black", 50))

    def update_gif_mal(frame):
        gif_label_mal.configure(image=converted_frames_mal[frame])

    frame_index_mal = 0

    def animate_gif_mal():
        nonlocal frame_index_mal
        update_gif_mal(frame_index_mal)
        frame_index_mal = (frame_index_mal+ 1) % gif_frames_mal
        mal_frame.after(100, animate_gif_mal)

    animate_gif_mal()
    
def volver_al_menu_mal():
    show_saludos()
    mal_frame.place_forget()
    
# Regular

def regular():
    hide_current_screen()
    regular_frame.place(relx=0.5, rely=0.5, anchor="center")
    regular_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_regular_button.grid(row=7, column=0, pady=20, columnspan=4)
    
    gif_image_regular = Image.open("Regular.gif")
    gif_frames_regular = gif_image_regular.n_frames

    converted_frames_regular = []
    for frame in range(gif_frames_regular):
        gif_image_regular.seek(frame)
        converted_frame_regular = ImageTk.PhotoImage(gif_image_regular)
        converted_frames_regular.append(converted_frame_regular)

    gif_label_regular= ctk.CTkLabel(regular_frame, text="REGULAR", compound="bottom", image=converted_frames_regular[0])
    gif_label_regular.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_regular.configure(font=("Cooper Black", 50))

    def update_gif_regular(frame):
        gif_label_regular.configure(image=converted_frames_regular[frame])

    frame_index_regular = 0

    def animate_gif_regular():
        nonlocal frame_index_regular
        update_gif_regular(frame_index_regular)
        frame_index_regular = (frame_index_regular+ 1) % gif_frames_regular
        regular_frame.after(100, animate_gif_regular)

    animate_gif_regular()

def volver_al_menu_regular():
    show_saludos()
    regular_frame.place_forget()

# Buenos Días

def buenosDias():
    hide_current_screen()
    buenosDias_frame.place(relx=0.5, rely=0.5, anchor="center")
    buenosDias_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_buenosDias_button.grid(row=7, column=0, pady=20, columnspan=4)
    
    gif_image_buenosDias = Image.open("BuenosDias.gif")
    gif_frames_buenosDias = gif_image_buenosDias.n_frames

    converted_frames_buenosDias = []
    for frame in range(gif_frames_buenosDias):
        gif_image_buenosDias.seek(frame)
        converted_frame_buenosDias = ImageTk.PhotoImage(gif_image_buenosDias)
        converted_frames_buenosDias.append(converted_frame_buenosDias)

    gif_label_buenosDias= ctk.CTkLabel(buenosDias_frame, text="BUENOS DÍAS", compound="bottom", image=converted_frames_buenosDias[0])
    gif_label_buenosDias.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_buenosDias.configure(font=("Cooper Black", 50))

    def update_gif_buenosDias(frame):
        gif_label_buenosDias.configure(image=converted_frames_buenosDias[frame])

    frame_index_buenosDias = 0

    def animate_gif_buenosDias():
        nonlocal frame_index_buenosDias
        update_gif_buenosDias(frame_index_buenosDias)
        frame_index_buenosDias = (frame_index_buenosDias+ 1) % gif_frames_buenosDias
        buenosDias_frame.after(100, animate_gif_buenosDias)

    animate_gif_buenosDias()
    
def volver_al_menu_buenosDias():
    show_saludos()
    buenosDias_frame.place_forget()
    
# Buenas Tardes
    
def buenasTardes():
    hide_current_screen()
    buenasTardes_frame.place(relx=0.5, rely=0.5, anchor="center")
    buenasTardes_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_buenasTardes_button.grid(row=7, column=0, pady=20, columnspan=4)
    
    gif_image_buenasTardes = Image.open("BuenasTardes.gif")
    gif_frames_buenasTardes = gif_image_buenasTardes.n_frames

    converted_frames_buenasTardes = []
    for frame in range(gif_frames_buenasTardes):
        gif_image_buenasTardes.seek(frame)
        converted_frame_buenasTardes = ImageTk.PhotoImage(gif_image_buenasTardes)
        converted_frames_buenasTardes.append(converted_frame_buenasTardes)

    gif_label_buenasTardes= ctk.CTkLabel(buenasTardes_frame, text="BUENAS TARDES", compound="bottom", image=converted_frames_buenasTardes[0])
    gif_label_buenasTardes.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_buenasTardes.configure(font=("Cooper Black", 50))

    def update_gif_buenasTardes(frame):
        gif_label_buenasTardes.configure(image=converted_frames_buenasTardes[frame])

    frame_index_buenasTardes = 0

    def animate_gif_buenasTardes():
        nonlocal frame_index_buenasTardes
        update_gif_buenasTardes(frame_index_buenasTardes)
        frame_index_buenasTardes = (frame_index_buenasTardes+ 1) % gif_frames_buenasTardes
        buenasTardes_frame.after(100, animate_gif_buenasTardes)

    animate_gif_buenasTardes()
    
def volver_al_menu_buenasTardes():
    show_saludos()
    buenasTardes_frame.place_forget()
    
# Buenas Noches   
    
def buenasNoches():
    hide_current_screen()
    buenasNoches_frame.place(relx=0.5, rely=0.5, anchor="center")
    buenasNoches_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_buenasNoches_button.grid(row=7, column=0, pady=20, columnspan=4)
    
    gif_image_buenasNoches = Image.open("BuenasNoches.gif")
    gif_frames_buenasNoches = gif_image_buenasNoches.n_frames

    converted_frames_buenasNoches = []
    for frame in range(gif_frames_buenasNoches):
        gif_image_buenasNoches.seek(frame)
        converted_frame_buenasNoches = ImageTk.PhotoImage(gif_image_buenasNoches)
        converted_frames_buenasNoches.append(converted_frame_buenasNoches)

    gif_label_buenasNoches= ctk.CTkLabel(buenasNoches_frame, text="Buenas Noches", compound="bottom", image=converted_frames_buenasNoches[0])
    gif_label_buenasNoches.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_buenasNoches.configure(font=("Cooper Black", 50))

    def update_gif_buenasNoches(frame):
        gif_label_buenasNoches.configure(image=converted_frames_buenasNoches[frame])

    frame_index_buenasNoches = 0

    def animate_gif_buenasNoches():
        nonlocal frame_index_buenasNoches
        update_gif_buenasNoches(frame_index_buenasNoches)
        frame_index_buenasNoches = (frame_index_buenasNoches+ 1) % gif_frames_buenasNoches
        buenasNoches_frame.after(100, animate_gif_buenasNoches)

    animate_gif_buenasNoches()
    
def volver_al_menu_buenasNoches():
    show_saludos()
    buenasNoches_frame.place_forget()
    
# Mi Nombre

def miNombre():
    hide_current_screen()
    miNombre_frame.place(relx=0.5, rely=0.5, anchor="center")
    miNombre_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_miNombre_button.grid(row=7, column=0, pady=20, columnspan=4)
    
    gif_image_miNombre = Image.open("MiNombre.gif")
    gif_frames_miNombre = gif_image_miNombre.n_frames

    converted_frames_miNombre = []
    for frame in range(gif_frames_miNombre):
        gif_image_miNombre.seek(frame)
        converted_frame_miNombre = ImageTk.PhotoImage(gif_image_miNombre)
        converted_frames_miNombre.append(converted_frame_miNombre)

    gif_label_miNombre= ctk.CTkLabel(miNombre_frame, text="Mi nombre", compound="bottom", image=converted_frames_miNombre[0])
    gif_label_miNombre.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_miNombre.configure(font=("Cooper Black", 50))

    def update_gif_miNombre(frame):
        gif_label_miNombre.configure(image=converted_frames_miNombre[frame])

    frame_index_miNombre = 0

    def animate_gif_miNombre():
        nonlocal frame_index_miNombre
        update_gif_miNombre(frame_index_miNombre)
        frame_index_miNombre = (frame_index_miNombre+ 1) % gif_frames_miNombre
        miNombre_frame.after(100, animate_gif_miNombre)

    animate_gif_miNombre()
    
def volver_al_menu_miNombre():
    show_saludos()
    miNombre_frame.place_forget()
    
# Yo Soy Sordo

def yoSoySordo():
    hide_current_screen()
    yoSoySordo_frame.place(relx=0.5, rely=0.5, anchor="center")
    yoSoySordo_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_yoSoySordo_button.grid(row=7, column=0, pady=20, columnspan=4)
    
    gif_image_yoSoySordo = Image.open("Sordo.gif")
    gif_frames_yoSoySordo = gif_image_yoSoySordo.n_frames

    converted_frames_yoSoySordo = []
    for frame in range(gif_frames_yoSoySordo):
        gif_image_yoSoySordo.seek(frame)
        converted_frame_yoSoySordo = ImageTk.PhotoImage(gif_image_yoSoySordo)
        converted_frames_yoSoySordo.append(converted_frame_yoSoySordo)

    gif_label_yoSoySordo= ctk.CTkLabel(yoSoySordo_frame, text="Yo soy sordo", compound="bottom", image=converted_frames_yoSoySordo[0])
    gif_label_yoSoySordo.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_yoSoySordo.configure(font=("Cooper Black", 50))

    def update_gif_yoSoySordo(frame):
        gif_label_yoSoySordo.configure(image=converted_frames_yoSoySordo[frame])

    frame_index_yoSoySordo = 0

    def animate_gif_yoSoySordo():
        nonlocal frame_index_yoSoySordo
        update_gif_yoSoySordo(frame_index_yoSoySordo)
        frame_index_yoSoySordo = (frame_index_yoSoySordo+ 1) % gif_frames_yoSoySordo
        yoSoySordo_frame.after(100, animate_gif_yoSoySordo)

    animate_gif_yoSoySordo()
    
def volver_al_menu_yoSoySordo():
    show_saludos()
    yoSoySordo_frame.place_forget()
    
    
# Hasta Mañana
    
def hastaMañana():
    hide_current_screen()
    hastaMañana_frame.place(relx=0.5, rely=0.5, anchor="center")
    hastaMañana_frame.configure(bg_color="#0c8f8f", fg_color="#0c8f8f")
    
    volver_menu_hastaMañana_button.grid(row=7, column=0, pady=20, columnspan=4)
    
    gif_image_hastaMañana = Image.open("HastaMañana.gif")
    gif_frames_hastaMañana = gif_image_hastaMañana.n_frames

    converted_frames_hastaMañana = []
    for frame in range(gif_frames_hastaMañana):
        gif_image_hastaMañana.seek(frame)
        converted_frame_hastaMañana = ImageTk.PhotoImage(gif_image_hastaMañana)
        converted_frames_hastaMañana.append(converted_frame_hastaMañana)

    gif_label_hastaMañana= ctk.CTkLabel(hastaMañana_frame, text="Hasta mañana", compound="bottom", image=converted_frames_hastaMañana[0])
    gif_label_hastaMañana.grid(row=0, column=1, padx=(20, 40), pady=(20, 40))
    gif_label_hastaMañana.configure(font=("Cooper Black", 50))

    def update_gif_hastaMañana(frame):
        gif_label_hastaMañana.configure(image=converted_frames_hastaMañana[frame])

    frame_index_hastaMañana = 0

    def animate_gif_hastaMañana():
        nonlocal frame_index_hastaMañana
        update_gif_hastaMañana(frame_index_hastaMañana)
        frame_index_hastaMañana = (frame_index_hastaMañana+ 1) % gif_frames_hastaMañana
        yoSoySordo_frame.after(100, animate_gif_hastaMañana)

    animate_gif_hastaMañana()
    
def volver_al_menu_hastaMañana():
    show_saludos()
    hastaMañana_frame.place_forget()



#Buscador
def buscador():
    buscador = buscador_entry.get()
    if buscador == "Hola" or buscador == "hola":
        hola()
    elif buscador == "adios" or buscador == "adiós" or buscador == "Adiós" or buscador == "Adios":
        adios()
    elif buscador == "Qué tal" or buscador == "que tal" or buscador == "qué tal" or buscador == "¿Qué tal?" or buscador == "¿qué tal?":
        queTal()
    elif buscador == "Bien" or buscador == "bien":
        bien()
    elif buscador == "Mal" or buscador == "mal":
        mal()
    elif buscador == "Regular" or buscador == "regular":
        regular()
    elif buscador == "Buenos días" or buscador == "buenos días" or buscador == "buenos dias" or buscador == "Buenos dias":
        buenosDias()
    elif buscador == "Buenas tardes" or buscador == "buenas tardes":
        buenasTardes()
    elif buscador == "Buenas noches" or buscador == "buenas noches":
        buenasNoches()
    elif buscador == "Mi nombre" or buscador == "mi nombre":
        miNombre()
    elif buscador == "Yo soy sordo" or buscador == "yo soy sordo":
        yoSoySordo()
    elif buscador == "Hasta mañana" or buscador == "hasta mañana":
        hastaMañana()
    else:
        print("Palabra no encontrada")


#forget
def hide_current_screen():
    for widget in root.place_slaves():
        widget.place_forget()



#pantalla de inicio
root = ctk.CTk()
root.geometry("1100x1000")
root.title("enSeñaMe")
ctk.set_default_color_theme("green")
root.config(bg="#0c8f8f")

name_label = ctk.CTkLabel(root, text="Ingresa tu nombre:")
name_label.place(relx=0.5, rely=0.4, anchor="center")
name_label.configure(bg_color="#0c8f8f")
name_label.configure(font=("Bernard MT Condensed", 20))

name_entry = ctk.CTkEntry(root)
name_entry.place(relx=0.5, rely=0.5, anchor="center")
name_entry.configure(bg_color="black", fg_color="black", border_color="black", width= 170, height=40)

name_button = ctk.CTkButton(root, text="Aceptar", command=show_welcome_message, fg_color="black", bg_color="green").place(relx=0.5, rely=0.7, anchor="center")

menu_button = ctk.CTkButton(root, text="Ir al menú", command=show_menu, fg_color="black", bg_color="green").place(relx=0.5, rely=0.8, anchor="center")

logo = ctk.CTkImage(dark_image=Image.open("logoAlex.png"), size=(550, 550))
logo_label = ctk.CTkLabel(root, image=logo, text="", bg_color="#0c8f8f")
logo_label.place(relx=0.5, rely=0.2, anchor="center")


#menú
menú_frame = ctk.CTkFrame(root)

abc_imagen = ctk.CTkImage(dark_image=Image.open("ABC.png"), size=(570, 150))
abecedario_button = ctk.CTkButton(menú_frame, text="Aprende el abecedario", command=show_abecedario, image=abc_imagen, fg_color='black', compound="top", height=70)
abecedario_button.configure(font=("Impact", 25))

familia_imagen = ctk.CTkImage(dark_image=Image.open("familia.png"), size=(200, 200))
familia_button = ctk.CTkButton(menú_frame, text="Aprende los miembros de la familia", command=show_familia, image=familia_imagen, compound="left", bg_color='sky blue', fg_color='black', height=70)
familia_button.configure(font=("Impact", 25))

saludos_imagen = ctk.CTkImage(dark_image=Image.open("saludos.png"), size=(570, 150))
saludos_button = ctk.CTkButton(menú_frame, text="Aprende los saludos", command=show_saludos,image=saludos_imagen, bg_color='sky blue', compound="bottom", fg_color='black', height=70)
saludos_button.configure(font=("Impact", 25))


#abecedario menú
abecedario_frame = ctk.CTkFrame(root)

a_imagen = ctk.CTkImage(dark_image=Image.open("letraA.png"), size=(70,70))
letra_a_button= ctk.CTkButton(abecedario_frame, text="", command=letra_a, image=a_imagen, bg_color='sky blue', fg_color='black')

b_imagen = ctk.CTkImage(dark_image=Image.open("letraB.png"), size=(70,70))
letra_b_button= ctk.CTkButton(abecedario_frame, text="", command=letra_b, image=b_imagen, bg_color='sky blue', fg_color='black')

c_imagen = ctk.CTkImage(dark_image=Image.open("letraC.png"), size=(70,70))
letra_c_button= ctk.CTkButton(abecedario_frame, text="", command=letra_c, image=c_imagen, bg_color='sky blue', fg_color='black')

d_imagen = ctk.CTkImage(dark_image=Image.open("letraD.png"), size=(70,70))
letra_d_button= ctk.CTkButton(abecedario_frame, text="", command=letra_d, image=d_imagen, bg_color='sky blue', fg_color='black')

e_imagen = ctk.CTkImage(dark_image=Image.open("letraE.png"), size=(70,70))
letra_e_button= ctk.CTkButton(abecedario_frame, text="", command=letra_e, image=e_imagen, bg_color='sky blue', fg_color='black')

f_imagen = ctk.CTkImage(dark_image=Image.open("letraF.png"), size=(70,70))
letra_f_button= ctk.CTkButton(abecedario_frame, text="", command=letra_f, image=f_imagen, bg_color='sky blue', fg_color='black')

g_imagen = ctk.CTkImage(dark_image=Image.open("letraG.png"), size=(70,70))
letra_g_button= ctk.CTkButton(abecedario_frame, text="", command=letra_g, image=g_imagen, bg_color='sky blue', fg_color='black')

h_imagen = ctk.CTkImage(dark_image=Image.open("letraH.png"), size=(70,70))
letra_h_button= ctk.CTkButton(abecedario_frame, text="", command=letra_h, image=h_imagen, bg_color='sky blue', fg_color='black')

i_imagen = ctk.CTkImage(dark_image=Image.open("letraI.png"), size=(70,70))
letra_i_button= ctk.CTkButton(abecedario_frame, text="", command=letra_i, image=i_imagen, bg_color='sky blue', fg_color='black')

j_imagen = ctk.CTkImage(dark_image=Image.open("letraJ.png"), size=(70,70))
letra_j_button= ctk.CTkButton(abecedario_frame, text="", command=letra_j, image=j_imagen, bg_color='sky blue', fg_color='black')

k_imagen = ctk.CTkImage(dark_image=Image.open("letraK.png"), size=(70,70))
letra_k_button= ctk.CTkButton(abecedario_frame, text="", command=letra_k, image=k_imagen, bg_color='sky blue', fg_color='black')

l_imagen = ctk.CTkImage(dark_image=Image.open("letraL.png"), size=(70,70))
letra_l_button= ctk.CTkButton(abecedario_frame, text="", command=letra_l, image=l_imagen, bg_color='sky blue', fg_color='black')

m_imagen = ctk.CTkImage(dark_image=Image.open("letraM.png"), size=(70,70))
letra_m_button= ctk.CTkButton(abecedario_frame, text="", command=letra_m, image=m_imagen, bg_color='sky blue', fg_color='black')

n_imagen = ctk.CTkImage(dark_image=Image.open("letraN.png"), size=(70,70))
letra_n_button= ctk.CTkButton(abecedario_frame, text="", command=letra_n, image=n_imagen, bg_color='sky blue', fg_color='black')

ñ_imagen = ctk.CTkImage(dark_image=Image.open("letraÑ.png"), size=(70,70))
letra_ñ_button= ctk.CTkButton(abecedario_frame, text="", command=letra_ñ, image=ñ_imagen, bg_color='sky blue', fg_color='black')

o_imagen = ctk.CTkImage(dark_image=Image.open("letraO.png"), size=(70,70))
letra_o_button= ctk.CTkButton(abecedario_frame, text="", command=letra_o, image=o_imagen, bg_color='sky blue', fg_color='black')

p_imagen = ctk.CTkImage(dark_image=Image.open("letraP.png"), size=(70,70))
letra_p_button= ctk.CTkButton(abecedario_frame, text="", command=letra_p, image=p_imagen, bg_color='sky blue', fg_color='black')

q_imagen = ctk.CTkImage(dark_image=Image.open("letraQ.png"), size=(70,70))
letra_q_button= ctk.CTkButton(abecedario_frame, text="", command=letra_q, image=q_imagen, bg_color='sky blue', fg_color='black')

r_imagen = ctk.CTkImage(dark_image=Image.open("letraR.png"), size=(70,70))
letra_r_button= ctk.CTkButton(abecedario_frame, text="", command=letra_r, image=r_imagen, bg_color='sky blue', fg_color='black')

s_imagen = ctk.CTkImage(dark_image=Image.open("letraS.png"), size=(70,70))
letra_s_button= ctk.CTkButton(abecedario_frame, text="", command=letra_s, image=s_imagen, bg_color='sky blue', fg_color='black')

t_imagen = ctk.CTkImage(dark_image=Image.open("letraT.png"), size=(70,70))
letra_t_button= ctk.CTkButton(abecedario_frame, text="", command=letra_t, image=t_imagen, bg_color='sky blue', fg_color='black')

u_imagen = ctk.CTkImage(dark_image=Image.open("letraU.png"), size=(70,70))
letra_u_button= ctk.CTkButton(abecedario_frame, text="", command=letra_u, image=u_imagen, bg_color='sky blue', fg_color='black')

v_imagen = ctk.CTkImage(dark_image=Image.open("letraV.png"), size=(70,70))
letra_v_button= ctk.CTkButton(abecedario_frame, text="", command=letra_v, image=v_imagen, bg_color='sky blue', fg_color='black')

w_imagen = ctk.CTkImage(dark_image=Image.open("letraW.png"), size=(70,70))
letra_w_button= ctk.CTkButton(abecedario_frame, text="", command=letra_w, image=w_imagen, bg_color='sky blue', fg_color='black')

x_imagen = ctk.CTkImage(dark_image=Image.open("letraX.png"), size=(70,70))
letra_x_button= ctk.CTkButton(abecedario_frame, text="", command=letra_x, image=x_imagen, bg_color='sky blue', fg_color='black')

y_imagen = ctk.CTkImage(dark_image=Image.open("letraY.png"), size=(70,70))
letra_y_button= ctk.CTkButton(abecedario_frame, text="", command=letra_y, image=y_imagen, bg_color='sky blue', fg_color='black')

z_imagen = ctk.CTkImage(dark_image=Image.open("letraZ.png"), size=(70,70))
letra_z_button= ctk.CTkButton(abecedario_frame, text="", command=letra_z, image=z_imagen, bg_color='sky blue', fg_color='black')

menú_imagen = ctk.CTkImage(dark_image=Image.open("menú.png"), size=(30,30))
volver_menu_abecedario_button = ctk.CTkButton(abecedario_frame, text="", command=volver_al_menu_abecedario, image=menú_imagen, bg_color='sky blue', fg_color='black')

#Letra A
letra_a_frame = ctk.CTkFrame(root)
menú_imagen = ctk.CTkImage(dark_image=Image.open("menú.png"), size=(30,30))
flecha_imagen = ctk.CTkImage(dark_image=Image.open("flecha.png"), size=(130,130))
flecha_imagen_izquierda = ctk.CTkImage(dark_image=Image.open("flecha2.png"), size=(130,130))

volver_menu_letra_a_button = ctk.CTkButton(letra_a_frame, text="", command=volver_al_menu_letra_a, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_a_button = ctk.CTkButton(root, text="", command=pág_siguiente_a, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra B
letra_b_frame = ctk.CTkFrame(root)
volver_menu_letra_b_button = ctk.CTkButton(letra_b_frame, text="", command=volver_al_menu_letra_b, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_b_button = ctk.CTkButton(root, text="", command=pág_siguiente_b, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_b_button = ctk.CTkButton(root, text="", command=pág_anterior_b, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra C
letra_c_frame = ctk.CTkFrame(root)
volver_menu_letra_c_button = ctk.CTkButton(letra_c_frame, text="", command=volver_al_menu_letra_c, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_c_button = ctk.CTkButton(root, text="", command=pág_siguiente_c, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_c_button = ctk.CTkButton(root, text="", command=pág_anterior_c, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra D
letra_d_frame = ctk.CTkFrame(root)
volver_menu_letra_d_button = ctk.CTkButton(letra_d_frame, text="", command=volver_al_menu_letra_d, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_d_button = ctk.CTkButton(root, text="", command=pág_siguiente_d, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_d_button = ctk.CTkButton(root, text="", command=pág_anterior_d, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra E
letra_e_frame = ctk.CTkFrame(root)
volver_menu_letra_e_button = ctk.CTkButton(letra_e_frame, text="", command=volver_al_menu_letra_e, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_e_button = ctk.CTkButton(root, text="", command=pág_siguiente_e, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_e_button = ctk.CTkButton(root, text="", command=pág_anterior_e, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra F
letra_f_frame = ctk.CTkFrame(root)
volver_menu_letra_f_button = ctk.CTkButton(letra_f_frame, text="", command=volver_al_menu_letra_f, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_f_button = ctk.CTkButton(root, text="", command=pág_siguiente_f, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_f_button = ctk.CTkButton(root, text="", command=pág_anterior_f, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra G
letra_g_frame = ctk.CTkFrame(root)
volver_menu_letra_g_button = ctk.CTkButton(letra_g_frame, text="", command=volver_al_menu_letra_g, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_g_button = ctk.CTkButton(root, text="", command=pág_siguiente_g, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_g_button = ctk.CTkButton(root, text="", command=pág_anterior_g, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra H
letra_h_frame = ctk.CTkFrame(root)
volver_menu_letra_h_button = ctk.CTkButton(letra_h_frame, text="", command=volver_al_menu_letra_h, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_h_button = ctk.CTkButton(root, text="", command=pág_siguiente_h, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_h_button = ctk.CTkButton(root, text="", command=pág_anterior_h, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra I
letra_i_frame = ctk.CTkFrame(root)
volver_menu_letra_i_button = ctk.CTkButton(letra_i_frame, text="", command=volver_al_menu_letra_i, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_i_button = ctk.CTkButton(root, text="", command=pág_siguiente_i, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_i_button = ctk.CTkButton(root, text="", command=pág_anterior_i, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra J
letra_j_frame = ctk.CTkFrame(root)
volver_menu_letra_j_button = ctk.CTkButton(letra_j_frame, text="", command=volver_al_menu_letra_j, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_j_button = ctk.CTkButton(root, text="", command=pág_siguiente_j, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_j_button = ctk.CTkButton(root, text="", command=pág_anterior_j, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra K
letra_k_frame = ctk.CTkFrame(root)
volver_menu_letra_k_button = ctk.CTkButton(letra_k_frame, text="", command=volver_al_menu_letra_k, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_k_button = ctk.CTkButton(root, text="", command=pág_siguiente_k, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_k_button = ctk.CTkButton(root, text="", command=pág_anterior_k, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra L
letra_l_frame = ctk.CTkFrame(root)
volver_menu_letra_l_button = ctk.CTkButton(letra_l_frame, text="", command=volver_al_menu_letra_l, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_l_button = ctk.CTkButton(root, text="", command=pág_siguiente_l, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_l_button = ctk.CTkButton(root, text="", command=pág_anterior_l, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra M
letra_m_frame = ctk.CTkFrame(root)
volver_menu_letra_m_button = ctk.CTkButton(letra_m_frame, text="", command=volver_al_menu_letra_m, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_m_button = ctk.CTkButton(root, text="", command=pág_siguiente_m, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_m_button = ctk.CTkButton(root, text="", command=pág_anterior_m, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra N
letra_n_frame = ctk.CTkFrame(root)
volver_menu_letra_n_button = ctk.CTkButton(letra_n_frame, text="", command=volver_al_menu_letra_n, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_n_button = ctk.CTkButton(root, text="", command=pág_siguiente_n, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_n_button = ctk.CTkButton(root, text="", command=pág_anterior_n, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra Ñ
letra_ñ_frame = ctk.CTkFrame(root)
volver_menu_letra_ñ_button = ctk.CTkButton(letra_ñ_frame, text="", command=volver_al_menu_letra_ñ, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_ñ_button = ctk.CTkButton(root, text="", command=pág_siguiente_ñ, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_ñ_button = ctk.CTkButton(root, text="", command=pág_anterior_ñ, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra O
letra_o_frame = ctk.CTkFrame(root)
volver_menu_letra_o_button = ctk.CTkButton(letra_o_frame, text="", command=volver_al_menu_letra_o, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_o_button = ctk.CTkButton(root, text="", command=pág_siguiente_o, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_o_button = ctk.CTkButton(root, text="", command=pág_anterior_o, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra P
letra_p_frame = ctk.CTkFrame(root)
volver_menu_letra_p_button = ctk.CTkButton(letra_p_frame, text="", command=volver_al_menu_letra_p, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_p_button = ctk.CTkButton(root, text="", command=pág_siguiente_p, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_p_button = ctk.CTkButton(root, text="", command=pág_anterior_p, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra Q
letra_q_frame = ctk.CTkFrame(root)
volver_menu_letra_q_button = ctk.CTkButton(letra_q_frame, text="", command=volver_al_menu_letra_q, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_q_button = ctk.CTkButton(root, text="", command=pág_siguiente_q, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_q_button = ctk.CTkButton(root, text="", command=pág_anterior_q, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra R
letra_r_frame = ctk.CTkFrame(root)
volver_menu_letra_r_button = ctk.CTkButton(letra_r_frame, text="", command=volver_al_menu_letra_r, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_r_button = ctk.CTkButton(root, text="", command=pág_siguiente_r, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_r_button = ctk.CTkButton(root, text="", command=pág_anterior_r, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra S
letra_s_frame = ctk.CTkFrame(root)
volver_menu_letra_s_button = ctk.CTkButton(letra_s_frame, text="", command=volver_al_menu_letra_s, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_s_button = ctk.CTkButton(root, text="", command=pág_siguiente_s, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_s_button = ctk.CTkButton(root, text="", command=pág_anterior_s, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra T
letra_t_frame = ctk.CTkFrame(root)
volver_menu_letra_t_button = ctk.CTkButton(letra_t_frame, text="", command=volver_al_menu_letra_t, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_t_button = ctk.CTkButton(root, text="", command=pág_siguiente_t, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_t_button = ctk.CTkButton(root, text="", command=pág_anterior_t, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra U
letra_u_frame = ctk.CTkFrame(root)
volver_menu_letra_u_button = ctk.CTkButton(letra_u_frame, text="", command=volver_al_menu_letra_u, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_u_button = ctk.CTkButton(root, text="", command=pág_siguiente_u, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_u_button = ctk.CTkButton(root, text="", command=pág_anterior_u, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra V
letra_v_frame = ctk.CTkFrame(root)
volver_menu_letra_v_button = ctk.CTkButton(letra_v_frame, text="", command=volver_al_menu_letra_v, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_v_button = ctk.CTkButton(root, text="", command=pág_siguiente_v, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_v_button = ctk.CTkButton(root, text="", command=pág_anterior_v, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra W
letra_w_frame = ctk.CTkFrame(root)
volver_menu_letra_w_button = ctk.CTkButton(letra_w_frame, text="", command=volver_al_menu_letra_w, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_w_button = ctk.CTkButton(root, text="", command=pág_siguiente_w, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_w_button = ctk.CTkButton(root, text="", command=pág_anterior_w, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra X
letra_x_frame = ctk.CTkFrame(root)
volver_menu_letra_x_button = ctk.CTkButton(letra_x_frame, text="", command=volver_al_menu_letra_x, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_x_button = ctk.CTkButton(root, text="", command=pág_siguiente_x, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_x_button = ctk.CTkButton(root, text="", command=pág_anterior_x, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra Y
letra_y_frame = ctk.CTkFrame(root)
volver_menu_letra_y_button = ctk.CTkButton(letra_y_frame, text="", command=volver_al_menu_letra_y, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_siguiente_y_button = ctk.CTkButton(root, text="", command=pág_siguiente_y, image=flecha_imagen, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')
pág_anterior_y_button = ctk.CTkButton(root, text="", command=pág_anterior_y, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#Letra Z
letra_z_frame = ctk.CTkFrame(root)
volver_menu_letra_z_button = ctk.CTkButton(letra_z_frame, text="", command=volver_al_menu_letra_z, image=menú_imagen, bg_color='sky blue', fg_color='black')
pág_anterior_z_button = ctk.CTkButton(root, text="", command=pág_anterior_z, image=flecha_imagen_izquierda, width=100, height=100, bg_color='#0c8f8f', fg_color='#0c8f8f')

#familia menú
familia_frame = ctk.CTkFrame(root)

mamá_button= ctk.CTkButton(familia_frame, text="Mamá", command=mamá, bg_color="#f4324a", fg_color="#f4324a")
mamá_button.configure(font=("Impact", 25))

papá_button= ctk.CTkButton(familia_frame, text="Papá", command=papá, bg_color="#f4324a", fg_color="#f4324a")
papá_button.configure(font=("Impact", 25))

hermano_a_button= ctk.CTkButton(familia_frame, text="Hermano/a", command=hermano_a, bg_color="#f4324a", fg_color="#f4324a")
hermano_a_button.configure(font=("Impact", 25))

abuelo_a_button= ctk.CTkButton(familia_frame, text="Abuelo/a", command=abuelo_a, bg_color="#f4324a", fg_color="#f4324a")
abuelo_a_button.configure(font=("Impact", 25))

tío_a_button= ctk.CTkButton(familia_frame, text="Tío/a", command=tío_a, bg_color="#f4324a", fg_color="#f4324a")
tío_a_button.configure(font=("Impact", 25))

primo_a_button= ctk.CTkButton(familia_frame, text="Primo/a", command=primo_a, bg_color="#f4324a", fg_color="#f4324a")
primo_a_button.configure(font=("Impact", 25))

padres_button= ctk.CTkButton(familia_frame, text="Padres", command=padres, bg_color="#f4324a", fg_color="#f4324a")
padres_button.configure(font=("Impact", 25))

hijos_button= ctk.CTkButton(familia_frame, text="Hijo/a", command=hijos, bg_color="#f4324a", fg_color="#f4324a")
hijos_button.configure(font=("Impact", 25))

familia1_button= ctk.CTkButton(familia_frame, text="Familia", command=familia1, bg_color="#f4324a", fg_color="#f4324a")
familia1_button.configure(font=("Impact", 25))

volver_menu_familia_button= ctk.CTkButton(familia_frame, text="", command=volver_al_menu_familia, image=menú_imagen, bg_color="#f4324a", fg_color="#f4324a")

#Mamá
mamá_frame = ctk.CTkFrame(root)
volver_menu_mamá_button = ctk.CTkButton(mamá_frame, text="", command=volver_al_menu_mamá, image=menú_imagen, bg_color='sky blue', fg_color='black')

#Papá
papá_frame = ctk.CTkFrame(root)
volver_menu_papá_button = ctk.CTkButton(papá_frame, text="", command=volver_al_menu_papá, image=menú_imagen, bg_color='sky blue', fg_color='black')

#Hermano/a
hermano_a_frame = ctk.CTkFrame(root)
volver_menu_hermano_a_button = ctk.CTkButton(hermano_a_frame, text="", command=volver_al_menu_hermano_a, image=menú_imagen, bg_color='sky blue', fg_color='black')

#Abuelo/a
abuelo_a_frame = ctk.CTkFrame(root)
volver_menu_abuelo_a_button = ctk.CTkButton(abuelo_a_frame, text="", command=volver_al_menu_abuelo_a, image=menú_imagen, bg_color='sky blue', fg_color='black')

#Tío/a
tío_a_frame = ctk.CTkFrame(root)
volver_menu_tío_a_button = ctk.CTkButton(tío_a_frame, text="", command=volver_al_menu_tío_a, image=menú_imagen, bg_color='sky blue', fg_color='black')

#Primo/a
primo_a_frame = ctk.CTkFrame(root)
volver_menu_primo_a_button = ctk.CTkButton(primo_a_frame, text="", command=volver_al_menu_primo_a, image=menú_imagen, bg_color='sky blue', fg_color='black')

#Padres
padres_frame = ctk.CTkFrame(root)
volver_menu_padres_button = ctk.CTkButton(padres_frame, text="", command=volver_al_menu_padres, image=menú_imagen, bg_color='sky blue', fg_color='black')

#Hijos
hijos_frame = ctk.CTkFrame(root)
volver_menu_hijos_button = ctk.CTkButton(hijos_frame, text="", command=volver_al_menu_hijos, image=menú_imagen, bg_color='sky blue', fg_color='black')

#Familia
familia1_frame = ctk.CTkFrame(root)
volver_menu_familia1_button = ctk.CTkButton(familia1_frame, text="", command=volver_al_menu_familia1, image=menú_imagen, bg_color='sky blue', fg_color='black')


#saludos menú
saludos_frame = ctk.CTkFrame(root, width=1000, height=1000)

volver_menu_saludos_button = ctk.CTkButton(saludos_frame, text="", command=volver_al_menu_saludos, image=menú_imagen, bg_color="black", fg_color="black")

lupa_imagen = ctk.CTkImage(dark_image=Image.open("lupa.png"), size=(40, 40))

buscador_entry = ctk.CTkEntry(saludos_frame)
buscador_entry.configure(bg_color="black", fg_color="black", border_color="black", width=200, height=40)
buscador_entry.place(relx=0.5, rely=0.35, anchor="center")

buscador_button = ctk.CTkButton(saludos_frame, text="Buscar", image=lupa_imagen, command=buscador, width=40, height=40, fg_color="black", bg_color="black", border_color="black", compound="right")
buscador_button.place(relx=0.5, rely=0.45, anchor="center")





#saludos_frames
hola_frame = ctk.CTkFrame(root)
volver_menu_hola_button = ctk.CTkButton(hola_frame, text="", command=volver_al_menu_hola, image=menú_imagen, bg_color='sky blue', fg_color='black')

adios_frame = ctk.CTkFrame(root)
volver_menu_adios_button = ctk.CTkButton(adios_frame, text="", command=volver_al_menu_adios, image=menú_imagen, bg_color='sky blue', fg_color='black')

queTal_frame = ctk.CTkFrame(root)
volver_menu_queTal_button = ctk.CTkButton(queTal_frame, text="", command=volver_al_menu_queTal, image=menú_imagen, bg_color='sky blue', fg_color='black')

bien_frame = ctk.CTkFrame(root)
volver_menu_bien_button = ctk.CTkButton(bien_frame, text="", command=volver_al_menu_bien, image=menú_imagen, bg_color='sky blue', fg_color='black')

mal_frame = ctk.CTkFrame(root)
volver_menu_mal_button = ctk.CTkButton(mal_frame, text="", command=volver_al_menu_mal, image=menú_imagen, bg_color='sky blue', fg_color='black')

regular_frame = ctk.CTkFrame(root)
volver_menu_regular_button = ctk.CTkButton(regular_frame, text="", command=volver_al_menu_regular, image=menú_imagen, bg_color='sky blue', fg_color='black')

buenosDias_frame = ctk.CTkFrame(root)
volver_menu_buenosDias_button = ctk.CTkButton(buenosDias_frame, text="", command=volver_al_menu_buenosDias, image=menú_imagen, bg_color='sky blue', fg_color='black')

buenasTardes_frame = ctk.CTkFrame(root)
volver_menu_buenasTardes_button = ctk.CTkButton(buenasTardes_frame, text="", command=volver_al_menu_buenasTardes, image=menú_imagen, bg_color='sky blue', fg_color='black')

buenasNoches_frame = ctk.CTkFrame(root)
volver_menu_buenasNoches_button = ctk.CTkButton(buenasNoches_frame, text="", command=volver_al_menu_buenasNoches, image=menú_imagen, bg_color='sky blue', fg_color='black')

miNombre_frame = ctk.CTkFrame(root)
volver_menu_miNombre_button = ctk.CTkButton(miNombre_frame, text="", command=volver_al_menu_miNombre, image=menú_imagen, bg_color='sky blue', fg_color='black')

yoSoySordo_frame = ctk.CTkFrame(root)
volver_menu_yoSoySordo_button = ctk.CTkButton(yoSoySordo_frame, text="", command=volver_al_menu_yoSoySordo, image=menú_imagen, bg_color='sky blue', fg_color='black')

hastaMañana_frame = ctk.CTkFrame(root)
volver_menu_hastaMañana_button = ctk.CTkButton(hastaMañana_frame, text="", command=volver_al_menu_hastaMañana, image=menú_imagen, bg_color='sky blue', fg_color='black')

root.mainloop()
