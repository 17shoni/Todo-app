from functions import get_todo, write_todo
import time

now = time.strftime('%d-%b-%Y and the time is %H:%M:%S')
print(f"Today is {now}")
while True:
    user_action =input('type add,show,edit,complete and exit: ').lower()
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todo()

        todos.append(todo + '\n')

        write_todo(todos)

    elif user_action.startswith('show'):
        todos = get_todo('file.txt')

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todo()

            new_todo = input('enter new todo item: ')
            todos[number] = new_todo + '\n'

            write_todo(todos)
        except ValueError:
            print('invalid command! please enter a number associated with the todo.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todo()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todo(todos)
            print(f"{todo_to_remove} was removed from the list")
        except IndexError:
            print('There is no todo associated the number.Try again')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Invalid Choice!!!, try again')

print('Bye')

