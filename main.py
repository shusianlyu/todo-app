import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)


def main():
    while True:
        # get user input and strip spaces chars from it
        user_action = input("Type add, show, edit, complete or exit: ")
        user_action = user_action.strip()

        if user_action.startswith('add'):
            todo = user_action[4:] + '\n'

            todos = functions.get_todos('todos.txt')

            todos.append(todo)

            functions.write_todos(todos, 'todos.txt')

        elif user_action.startswith('show'):
            todos = functions.get_todos('todos.txt')

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}-{item}")

        elif user_action.startswith('edit'):
            try:
                number = int(user_action[5:])

                number = number - 1

                todos = functions.get_todos('todos.txt')

                if number >= len(todos):
                    print("Index out of length")
                else:
                    new_todo = input("Enter new todo: ")
                    todos[number] = new_todo + '\n'
                    functions.write_todos(todos, 'todos.txt')
            except ValueError:
                print("Your command is not valid")
                continue

        elif user_action.startswith('complete'):
            try:
                number = int(user_action[9:])
                index = number - 1

                todos = functions.get_todos('todos.txt')

                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)
                functions.write_todos(todos, 'todos.txt')
                message = f"Todo {todo_to_remove} was removed from the list."
                print(message)
            except IndexError:
                print("There is no item with that number")
                continue
            except ValueError:
                print("Your command is not valid")

        elif user_action.startswith('exit'):
            break

        else:
            print("Hey, you entered an unknown command")

    print("Bye!")


if __name__ == '__main__':
    main()
