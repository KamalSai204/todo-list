def  get(filepath="thht.txt"):
        with open(filepath,"r") as file:
                ui=file.readlines()
        return ui
def write(a_arg,filepath="thht.txt"):
        with open(filepath,"w") as file:
                file.writelines(a_arg)
if __name__=="__main__":
        print("hello")
        print(get())