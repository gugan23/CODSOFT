import tkinter as tk 
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql
from tkinter import font

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty')
    else:
        tasks.append(task_string)
        the_cursor.execute('INSERT INTO tasks (title) VALUES (?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
            the_cursor.execute('DELETE FROM tasks WHERE title = ?', (the_value,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    message_box = messagebox.askyesno("Delete All", "Are you sure you want to delete all tasks?")
    if message_box:
        while len(tasks) != 0:
            tasks.pop()
        the_cursor.execute('DELETE FROM tasks')
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    print(tasks)
    the_connection.commit()
    the_cursor.close()
    guiWindow.destroy()

def retrieve_database():
    while len(tasks) != 0:
        tasks.pop()
    for row in the_cursor.execute('SELECT title FROM tasks'):
        tasks.append(row[0])

if __name__ == '__main__':
    guiWindow = tk.Tk()

    guiWindow.title('To-do List - codesoft')

    guiWindow.geometry('2000x1000')



    guiWindow.configure(bg='pink')

    the_connection = sql.connect('todo.db')

    the_cursor = the_connection.cursor()

    the_cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')

    tasks = []

    header_frame = tk.Frame(guiWindow, bg='SeaGreen1')
    functions_frame = tk.Frame(guiWindow, bg='SeaGreen1')
    listbox_frame = tk.Frame(guiWindow, bg='SeaGreen1')

    header_frame.pack(fill='both')
    functions_frame.pack(side='left', expand=True, fill='both')
    listbox_frame.pack(side='right', expand=True, fill='both')

    header_label = ttk.Label(header_frame, text='THE TO-DO LIST', font=('Algerian', 40),background = 'SeaGreen1', foreground='saddlebrown')
    header_label.pack(padx=20, pady=20)

    task_label = ttk.Label(functions_frame, text='Enter The Task:', font=("Consolas", 35, "bold"),background = 'SeaGreen1',foreground='saddlebrown')
    task_label.place(x=30, y=40)

    task_field = ttk.Entry(functions_frame, font=("Consolas", 12), width=40)
    task_field.place(x=30, y=90)

    add_button = ttk.Button(functions_frame, text='Add Task', width=35, command=add_task)
    del_button = ttk.Button(functions_frame, text='Delete Task', width=35, command=delete_task)
    del_all_button = ttk.Button(functions_frame, text='Delete All Tasks', width=35, command=delete_all_tasks)
    exit_button = ttk.Button(functions_frame, text='Exit', width=35,command=close)

    add_button.place(x=30, y=130)
    del_button.place(x=30, y=170)
    del_all_button.place(x=30, y=210)
    exit_button.place(x=30, y=250)
    listbox_font = font.Font (size=15)
    task_listbox = tk.Listbox(listbox_frame, width=100, height=70, selectmode='SINGLE', background='white', foreground='black', selectbackground='MediumOrchid1', selectforeground='purple',font = listbox_font)
    task_listbox.place(x=10, y=20)

    retrieve_database()
    list_update()

    guiWindow.mainloop()

    the_connection.commit()
    the_cursor.close()
