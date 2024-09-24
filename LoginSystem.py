"""
======================================================================================================================
Author:                         {root@lonedevwolf}
Language:                       Python
Modules:                        tkinter
Description:                    Create Account and Login System
======================================================================================================================
[!]: Create a Create account and login page that saves data in a Graphical User Interface (GUI)

"""

import tkinter as tk

root = tk.Tk()

root.geometry('800x500')
root.title("Wolf Secret Vault")
#
# labelTitle = tk.Label(root, text="Wolf Vault", font=("Tahoma", 24))
# labelTitle.pack(padx=20, pady=50)
#
# labelSubTitle = tk.Label(root, text="Create Account", font=("Tahoma", 12))
# labelSubTitle.pack()
#
# firstName = tk.Label(root, text="First Name:")
# firstName.pack(padx=5, pady=10)
#
# firstNameEntry = tk.Entry(root, width=40, font=("Tahoma", 10))
# firstNameEntry.pack()
#
# lastName = tk.Label(root, text="Last Name:")
# lastName.pack(padx=5, pady=10)
#
# lastNameEntry = tk.Entry(root, width=40, font=("Tahoma", 10))
# lastNameEntry.pack()
#
# emailAddress = tk.Label(root, text="Email Address:")
# emailAddress.pack(padx=5, pady=10)
#
# emailAddress = tk.Entry(root, width=40, font=("Tahoma", 10))
# emailAddress.pack()
#
# submitBtn = tk.Button(root, text="Submit", font=("Tahoma", 12))
# submitBtn.pack(padx=5, pady=10)


newPass = tk.Label(root, text='Old Password:')
newPass.grid(row=0, sticky="w")
# Label(master, text='New Password:').grid(row=1, sticky=W)
# Label(master, text='Enter New Password Again:').grid(row=2,
# sticky=W)



root.mainloop()
