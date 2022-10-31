#Test 1
from tkinter import *
from tkinter.ttk import *

def change(event):
    b['text'] = 'Thanks for your click. ;)'

root = Tk()

b = Button(text='Click me!')
b.bind('<Button-1>', change)
b.bind('<Return>', change)
b.pack()

root.mainloop()

#Test 2
from tkinter import *
from tkinter.ttk import *

def change(event):
    b['text'] = 'Thanks for your click. ;)'

root = Tk()

b = Button(text='Click me!')
b.bind('<Button-1>', change)
b.bind('<Return>', change)
b.pack()

root.mainloop()

#Test 3
from tkinter import *
from tkinter.ttk import *


def font1(event):
    l['font'] = "Verdana"

def font2(event):
    l['font'] = "Times"

root = Tk()

l = Label(text="Hello World")
l.bind('<Button-1>', font1)  # ЛКМ
l.bind('<Button-3>', font2)  # ПКМ
l.pack()

root.mainloop()

#Test 4
from tkinter import *

def changeFont(font):
    l['font'] = font

root = Tk()
l = Label(text="Hello World")
l.pack()
Button(text="Verdana", command=lambda f="Verdana": changeFont(f)).pack()
Button(text="Times", command=lambda f="Times": changeFont(f)).pack()

root.mainloop()

#Test 5
from tkinter import *

def b1(event):
    root.title("Левая кнопка мыши")
def b3(event):
    root.title("Правая кнопка мыши")
def move(event):
    x = event.x
    y = event.y
    s = "Движение мышью {}x{}".format(x, y)
    root.title(s)

root = Tk()
root.minsize(width = 500, height=400)

root.bind('<Button-1>', b1)
root.bind('<Button-3>', b3)
root.bind('<Motion>', move)

root.mainloop()

#Test 6
from tkinter import *

def show_key(event):
    root.title(str(event))

root = Tk()
root.bind('<Key>', show_key)
root.mainloop()

#Test 7
import time

for _ in range(5):
    print(int(time.time()))             # общее количество секунд
    print(time.strftime("%H:%M:%S"))    # время ввиде строки
    time.sleep(1)                       # задержка 1 сек.

#Test 8
from tkinter import *
from tkinter.ttk import *

def get_status():
    pass

def get_task():
    pass

def set_result():
    pass

def set_time():
    pass


root = Tk()
root.title('Literary note')

text = Text(wrap=WORD, width=30)
text.pack(side=LEFT, expand=1, fill=BOTH)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)

frame_right = Frame()
frame_right.pack(side=LEFT, fill=Y)


frame_task = LabelFrame(frame_right, text='Task:')
frame_task.pack(fill=X)

Label(frame_task, text='Min words:').pack()
entry_min_words = Entry(frame_task, justify=RIGHT)
entry_min_words.insert(END, 70)
entry_min_words.pack(fill=X)

Label(frame_task, text='Max words:').pack()
entry_max_words = Entry(frame_task, justify=RIGHT)
entry_max_words.insert(END, 90)
entry_max_words.pack(fill=X)

Label(frame_task, text='Number of words in a sentence:').pack()
entry_sentence_len = Entry(frame_task, justify=RIGHT)
entry_sentence_len.insert(END, 7)
entry_sentence_len.pack(fill=X)

label_sentence_start = Label(frame_task, text="Number of start sentences: 2 - 3")
label_sentence_start.pack(fill=X)
label_sentence_main = Label(frame_task, text="Number of main sentences: 5 - 7")
label_sentence_main.pack(fill=X)
label_sentence_end = Label(frame_task, text="Number of end sentences: 2 - 3")
label_sentence_end.pack(fill=X)


frame_status = LabelFrame(frame_right, text='Status:')
frame_status.pack(fill=X)
label_written_words = Label(frame_status, text='Written words: 0')
label_written_words.pack(fill=X)
label_written_sentences = Label(frame_status, text='Written sentences: 0')
label_written_sentences.pack(fill=X)

label_written_sentence_start = Label(frame_status, text="Written start sentences: 0")
label_written_sentence_start.pack(fill=X)
label_written_sentence_main = Label(frame_status, text="Written main sentences: 0")
label_written_sentence_main.pack(fill=X)
label_written_sentence_end = Label(frame_status, text="Written end sentences: 0")
label_written_sentence_end.pack(fill=X)


frame_result = LabelFrame(frame_right, text='Result:')
frame_result.pack(fill=X)
label_time_spent = Label(frame_result, text='Spent time: 00:00:00')
label_time_spent.pack(fill=X)
label_result = Label(frame_result, text="Result: Less.../Ready!/Much...")
label_result.pack(fill=X)

root.mainloop()