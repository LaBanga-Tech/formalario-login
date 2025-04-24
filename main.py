from customtkinter import (
    CTk,
    CTkFrame,
    CTkLabel,
    CTkButton,
    CTkEntry,
    CTkCheckBox,
    IntVar,
    StringVar,
)
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

win = CTk()
width = 900
height = 600
pad_left = (win.winfo_screenwidth() - width) // 2
pad_top = (win.winfo_screenheight() - height) // 2
win.geometry(f"{width}x{height}+{pad_left}+{pad_top}")
win.resizable(False, False)
win.title("Login")

# ! FRAME 1
frame1 = CTkFrame(win, width=(width / 2), height=height, corner_radius=1)
frame1.grid(column=0, row=0)

image_tk = ImageTk.PhotoImage(
    Image.open("./imagens/back.png").resize(((width // 2), height))
)

label_image = CTkLabel(frame1, image=image_tk, text=None)
label_image.pack()

# ? FRAME 2
frame2 = CTkFrame(
    win, fg_color="#123456", width=(width / 2), height=height, corner_radius=1
)
frame2.grid(column=1, row=0)

# LABEL EMAIL
CTkLabel(frame2, text="Email", font=("Corbel", 17, "bold"), text_color="#f1f1f1").place(
    relx=0.05, y=170
)

# ENTRY - EMAIL
email = StringVar()


def Email_Validator(ev):
    lower_chars()
    if "@" not in email.get():
        entry_email.configure(border_color="red")
        return
    else:
        entry_email.configure(
            border_color="#131c25",
        )
        return


def lower_chars():
    prev_text = email.get().lower()
    email.set(prev_text)


entry_email = CTkEntry(
    frame2,
    width=((width // 2) - 50),
    height=40,
    corner_radius=1,
    border_width=1,
    border_color="#131c25",
    bg_color="#fff",
    fg_color="#131c25",
    text_color="#f1f1f1",
    textvariable=email,
)
entry_email.bind("<KeyRelease>", Email_Validator)
entry_email.place(relx=0.05, y=200)

# LABEL SENHA
CTkLabel(
    frame2,
    text="Palavra Passe",
    font=("Corbel", 17, "bold"),
    text_color="#f1f1f1",
).place(relx=0.05, y=260)

# ENTRY - SENHA
password = StringVar()
entry_password = CTkEntry(
    frame2,
    width=((width // 2) - 50),
    height=40,
    corner_radius=1,
    border_width=1,
    border_color="#131c25",
    bg_color="#fff",
    fg_color="#131c25",
    text_color="#f1f1f1",
    textvariable=password,
    show="●",
)
entry_password.place(relx=0.05, y=290)


# CHECKBOX - MOSTRAR/ESCONDER SENHA
def Show_Hidde_Password():
    value = checkbox_state.get()
    if value == 1:
        entry_password.configure(show="")
    else:
        entry_password.configure(show="●")


checkbox_state = IntVar(value=0)
ckeckbox_show = CTkCheckBox(
    frame2,
    text="Mostrar palavra passe",
    checkbox_width=17,
    checkbox_height=17,
    border_width=1,
    border_color="#e6a00a",
    corner_radius=0,
    checkmark_color="#ffffff",
    fg_color="#e6a00a",
    font=("Corbel", 13),
    text_color="#f1f1f1",
    hover_color="#926605",
    variable=checkbox_state,
    command=Show_Hidde_Password,
)
ckeckbox_show.place(relx=0.05, y=350)


def Login():
    connection = sqlite3.connect("./database.db")

    cursor = connection.cursor()

    if email.get() != "" and password.get() != "":
        data = cursor.execute(
            f"SELECT * FROM clientes WHERE email='{email.get().lower()}' AND password='{password.get().lower()}';"
        ).fetchall()

        if len(data) > 0:
            messagebox.showinfo("Sucesso", f"{data[0][3]} está cadastrado(a)!")
        else:
            messagebox.showerror("Aviso", "Acesso Negado!")

    else:
        messagebox.showwarning("Aviso", "Preencha os dados correctamente!")


# BUTTON - LOGIN
btn_login = CTkButton(
    frame2,
    text="Login",
    width=(width // 2 - 50),
    height=40,
    corner_radius=1,
    fg_color="#e6a00a",
    text_color="#ffffff",
    hover_color="#926605",
    font=("Corbel", 18, "bold"),
    command=Login,
)
btn_login.place(relx=0.05, y=400)
win.mainloop()
