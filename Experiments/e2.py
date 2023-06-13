# user_prompt = "Enter a todo:"
# todos = []
# while len(todos) < 5:
#     todo = input(user_prompt)
#     todos.append(todo.capitalize())
# print(todos)

with open("../Files/e", "r") as file:
    file.read()
    content = file.read()

print("hello:", content) ##prints nothing since the read method is exhausted the second time when we use file.read()