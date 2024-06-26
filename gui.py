import functions
import FreeSimpleGUI as fsg
import time

fsg.theme('Black')

clock = fsg.Text('', key='clock')
label = fsg.Text('Type in a to-do ')
input_box = fsg.InputText(tooltip='Enter a to-do', key='todo')
add_button = fsg.Button('Add')
list_box = fsg.Listbox(values=functions.get_todo(), key='todos',
                       enable_events=True, size=[30, 10])
edit_button = fsg.Button('Edit')
complete_button = fsg.Button('Complete')
exit_button = fsg.Button('Exit')

window = fsg.Window('My To-Do App',
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=10)
    window['clock'].update(time.strftime('%d-%b-%Y and the time is %H:%M:%S'))

    match event:
        case 'Add':
            todos = functions.get_todo()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo )
            functions.write_todo(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'

                todos = functions.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todo(todos)
                window['todos'].update(values=todos)
            except IndexError:
                fsg.popup('Please select an item first.', font=('Helvetica', 20))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todo()
                todos.remove(todo_to_complete)
                functions.write_todo(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                fsg.popup('Please select an item first.', font=('Helvetica', 20))
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case fsg.WIN_CLOSED:
            break

window.close()

