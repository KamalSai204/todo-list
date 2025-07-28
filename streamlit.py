import functions
import FreeSimpleGUI as sg
label = sg.Text("To-Do-List App")
input_box=sg.InputText(tooltip="Enter a task",key="todo")
add_button = sg.Button("Add")
label2=sg.Text("Add a task to the list")
input2=sg.Input()
add1 = sg.FolderBrowse("Add")
compress=sg.Button("Compress")
window = sg.Window("To-Do-List App", layout=[[label,input_box,add_button],[label2, input2, add1],[compress],]  ,font=("helvetica",20))
while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos=functions.get()
            new=values["todo"]+"\n"
            todos.append(new)
            functions.write(todos)
        case sg.WIN_CLOSED:
            break
window.close()