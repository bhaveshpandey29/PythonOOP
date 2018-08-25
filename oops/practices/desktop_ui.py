import tkinter as tk
from tkinter import messagebox as msg
from datahandler import Handler
class UserPanel(Handler):

    def __init__(self):
        self.loginPanel=tk.Tk()
        self.loginPanel.title("Login Panel")
        self.loginPanel.geometry("500x500")
        self.AddLoginWidgets()

        self.loginPanel.mainloop()

    def AddLoginWidgets(self):
        self.loginUserNameLable = tk.Label(self.loginPanel,text="UserName ",padx=50,pady=50)
        self.loginUserNameLable.grid(row =1,column=1 )
        self.loginUserNameEntry = tk.Entry(self.loginPanel)
        self.loginUserNameEntry.grid(row =1, column=2)
        #Password
        self.loginPasswordLable = tk.Label(self.loginPanel,text="Password ",padx=10,pady=10)
        self.loginPasswordLable.grid(row =2,column=1 )
        self.loginPasswordEntry = tk.Entry(self.loginPanel,show="*")
        self.loginPasswordEntry.grid(row =2, column=2)
        #SubmitButton
        self.loginSubmitButton = tk.Button(self.loginPanel,text = "Submit",command = self.checkLogin)
        self.loginSubmitButton.grid(row = 4,column =2,padx=10,pady=10)
        #RegisterButton
        self.loginRegisterButton = tk.Button(self.loginPanel,text = "Register",command = self.registerPanel)
        self.loginRegisterButton.grid(row = 5,column =2,padx=10,pady=10)
    
    def registerPanel(self):
        self.loginPanel.destroy()
        self.registerPanel=tk.Tk()
        self.registerPanel.title("Register Panel")
        self.registerPanel.geometry("500x500")
        #User Name
        self.fullNameLable = tk.Label(self.registerPanel,text="Username ",padx=50,pady=50)
        self.fullNameLable.grid(row =1,column=1 )
        self.fullNameEntry = tk.Entry(self.registerPanel)
        self.fullNameEntry.grid(row =1, column=2)
        #Password
        self.loginPasswordLable = tk.Label(self.registerPanel,text="Password ",padx=10,pady=10)
        self.loginPasswordLable.grid(row =2,column=1 )
        self.loginPasswordEntry = tk.Entry(self.registerPanel,show="*")
        self.loginPasswordEntry.grid(row =2, column=2)
        #Contact Number
        self.contactNumberLable = tk.Label(self.registerPanel,text="Contact number ",padx=50,pady=50)
        self.contactNumberLable.grid(row =3,column=1 )
        self.contactNumberEntry = tk.Entry(self.registerPanel)
        self.contactNumberEntry.grid(row =3, column=2)
        #email
        self.emailLable = tk.Label(self.registerPanel,text="Email ",padx=50,pady=50)
        self.emailLable.grid(row =4,column=1 )
        self.emailEntry = tk.Entry(self.registerPanel)
        self.emailEntry.grid(row =4, column=2)
        #submit button
        self.registerSubmitButton = tk.Button(self.registerPanel,text = "Submit",command = self)
        self.registerSubmitButton.grid(row = 5,column =2,padx=10,pady=10)

    def checkLogin(self):
        self.__username = self.loginUserNameEntry.get()
        self.__password = self.loginPasswordEntry.get()
        self.handlerLogin(self.__username,self.__password,msg)
        # print(self.__username)
        # print(self.__password)
    
    def registerUser(self):
        self.__username = self.fullNameEntry.get()
        self.__password = self.loginPasswordEntry.get()
        self.__contactNo = self.contactNumberEntry.get()
        self.email = self.emailEntry.get()
        self.handlerRegister(self.__username,self.__password,self.__contactNo,self.email,msg,self.registerPanel)


if __name__ == '__main__':
    UserPanel()