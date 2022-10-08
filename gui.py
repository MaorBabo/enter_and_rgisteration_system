import tkinter as tk
from tkinter import messagebox
import signup as ps
import signin as sn

# the main window:
root = tk.Tk()

# The title of the program:
root.title("SIGNUP SYSTEM")

# Frames:
signinFrame = tk.LabelFrame(text='SIGN IN', padx=16, pady=10, bg='grey')
signupFrame = tk.LabelFrame(text='SIGN UP', padx=16, pady=10, bg='grey')
up_buttonsFrame = tk.LabelFrame(text='options', padx=21, pady=15, bg='grey')
in_buttonsFrame = tk.LabelFrame(text='options', padx=21, pady=15, bg='grey')

# Sign up Entries:
userNameEntry = tk.Entry(signupFrame, width=28, bg="silver", bd=5)
userNameEntry.insert(0, "")
passwordEntry = tk.Entry(signupFrame, width=28, bg="silver", bd=5)
passwordEntry.insert(0, "")

# Sign in Entries:
in_userNameEntry = tk.Entry(signinFrame, width=28, bg="silver", bd=5)
in_userNameEntry.insert(0, "")
in_passwordEntry = tk.Entry(signinFrame, width=28, bg="silver", bd=5)
in_passwordEntry.insert(0, "")

# user and password object:
UaP = ps.UserNamePassword(userNameEntry.get(), passwordEntry.get())


def changeMessageLabel(userName, password):
    """
    set a new account to the system and show appropriate message.
    :param userName: str
    :param password: str
    :return: message
    """
    # Making a password object:
    UaP.changeUserAndPassword(userName, password)

    # Clear the entries:
    userNameEntry.delete(0, tk.END)
    passwordEntry.delete(0, tk.END)

    # Showing a success window:
    if UaP.setUserAndPassword() == ps.SUCCESS:
        messagebox.showinfo("showinfo", "Success!")

    # Showing an error message:
    else:
        messagebox.showerror("ERROR", UaP.setUserAndPassword())


def deleteAccount(userName, password):
    """
    This function deleting the account from the system.
    :param userName: str
    :param password: ste
    :return: None
    """
    info = UaP.delete(userName, password)

    if info == ps.DELETED:
        messagebox.showinfo("showinfo", info)

    else:
        messagebox.showerror("ERROR", info)

    # Clear the entries:
    userNameEntry.delete(0, tk.END)
    passwordEntry.delete(0, tk.END)


def sign_in():
    """
    sign the user in and show appropriate message.
    :return: message
    """

    sign_in_object = sn.SignIn(in_userNameEntry.get(), in_passwordEntry.get())

    # Clear the entries:
    in_userNameEntry.delete(0, tk.END)
    in_passwordEntry.delete(0, tk.END)

    # Showing a success window:
    if sign_in_object.setUserActive() == sn.SUCCESS:
        messagebox.showinfo("showinfo", "Success!")

    # Showing an error message:
    else:
        messagebox.showerror("ERROR", sign_in_object.setUserActive())


def on_enter_signUpButton(e):
    signUpButton['background'] = '#76EE00'


def on_leave_signUpButton(e):
    signUpButton['background'] = 'silver'


def on_enter_quitButton(e):
    quitButton['background'] = '#76EE00'


def on_leave_quitButton(e):
    quitButton['background'] = 'silver'


def on_enter_delete_account(e):
    delete_account['background'] = '#76EE00'


def on_leave_delete_account(e):
    delete_account['background'] = 'silver'


def on_enter_signInButton(e):
    signInButton['background'] = '#76EE00'


def on_leave_signInButton(e):
    signInButton['background'] = 'silver'


# SignUp Labels:
userNameLabel = tk.Label(signupFrame, text="User name:", padx=55, pady=10, bg="silver", bd=5)
passwordLabel = tk.Label(signupFrame, text="Password:", padx=58, pady=10, bg="silver", bd=5)

# SignIn Labels:
inUserNameLabel = tk.Label(signinFrame, text="User name:", padx=55, pady=10, bg="silver", bd=5)
inPasswordLabel = tk.Label(signinFrame, text="Password:", padx=58, pady=10, bg="silver", bd=5)
blankLabel = tk.Label(in_buttonsFrame, text="           ", padx=62, pady=20, bg='silver')

# Buttons:
signUpButton = tk.Button(up_buttonsFrame, text="SIGN UP", padx=59, pady=20, bg='silver', activebackground='#76EE00',
                         command=lambda: changeMessageLabel(userNameEntry.get(), passwordEntry.get()))
quitButton = tk.Button(in_buttonsFrame, text="QUIT", padx=67, pady=20, bg='silver', activebackground='#76EE00',
                       command=root.quit)
delete_account = tk.Button(up_buttonsFrame, text="DELETE", padx=62, pady=20, bg='silver', activebackground='#76EE00',
                           command=lambda: deleteAccount(userNameEntry.get(), passwordEntry.get()))

signInButton = tk.Button(in_buttonsFrame, text="SIGN IN", padx=59, pady=20, bg='silver', activebackground='#76EE00',
                         command=sign_in)


def mainLoop():
    signinFrame.grid(row=0, column=800)
    signupFrame.grid(row=0, column=750)
    up_buttonsFrame.grid(row=6, column=750)
    in_buttonsFrame.grid(row=6, column=800)

    # Griding the sign up widgets:
    userNameLabel.grid(row=0, column=750)
    userNameEntry.grid(row=2, column=750)

    # Packing the password label and its entry:
    passwordLabel.grid(row=3, column=750)
    passwordEntry.grid(row=5, column=750)

    # Packing the buttons:
    signUpButton.grid(row=10, column=750)

    delete_account.grid(row=11, column=750)

    signUpButton.bind("<Enter>", on_enter_signUpButton)
    signUpButton.bind("<Leave>", on_leave_signUpButton)

    delete_account.bind("<Enter>", on_enter_delete_account)
    delete_account.bind("<Leave>", on_leave_delete_account)

    # Griding the sign in widgets:
    inUserNameLabel.grid(row=0, column=800)
    in_userNameEntry.grid(row=2, column=800)

    inPasswordLabel.grid(row=3, column=800)
    in_passwordEntry.grid(row=5, column=800)

    signInButton.grid(row=10, column=800)
    quitButton.grid(row=12, column=800)
    blankLabel.grid(row=12, column=800)

    quitButton.bind("<Enter>", on_enter_quitButton)
    quitButton.bind("<Leave>", on_leave_quitButton)

    signInButton.bind("<Enter>", on_enter_signInButton)
    signInButton.bind("<Leave>", on_leave_signInButton)
    root.mainloop()
