class Handler():
    def handlerLogin(self,username,password,msg_obj):
        if(username == "admin" and password=="pass@123"):
            msg_obj.showinfo("Success",f"Welcome {username}")
        else:
            msg_obj.showerror("Failed attempt!")
    
    #def handerRegister(self,username,password,email,contact):
