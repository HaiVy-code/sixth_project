from guizero import App, Text, Box, TextBox, ListBox, PushButton, info
cuaso = App(title = "todo app")
box1 = Box(cuaso, layout = "grid")
chu = Text(box1, text = "cong viec:", grid = [0, 0])
textbox = TextBox(box1, width = 30, grid = [1, 0])
listbox = ListBox(cuaso, width = 480, height = 400, scrollbar = True)
def them():
    if not textbox.value:
        info("thong bao", "vui long nhap noi dung")
        return
    elif textbox.value in listbox.items:
        info("thong bao", "da co cong viec nay roi")
    else:
        listbox.append(textbox.value)
        with open("todo.txt", "a", encoding = "utf-8") as file:
            file.write(textbox.value + "\n")
        textbox.clear()
def xoa():
    listbox.remove(listbox.value)
    with open("todo.txt", "w") as file:
        for i in listbox.items:
            file.write(i + "\n")
def doc():
    listbox.clear()
with open("todo.txt", "r") as f:
    for line in f:
        listbox.append(line.strip())
button1 = PushButton(box1, text = "add", grid = [2, 0], command = them, width = 5)
button2 = PushButton(box1, text = "delete", grid = [2, 1], command = xoa, width = 5)
cuaso.display()