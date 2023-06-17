import functions as fs
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=fs.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = fs.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            fs.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'

            todos = fs.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            fs.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todo_to_remove = values['todos'][0]
            todos = fs.get_todos()
            todos.remove(todo_to_remove)
            fs.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            break

print('Bye!')
window.close()
