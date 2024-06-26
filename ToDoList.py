from tkinter import*
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        task_Listbox.insert(END, task)
        entry.delete(0,END)
    else:
        messagebox.showwarning(("Warning", "You must enter a task."))
def delete_task():
    try:
        select_task_index = task_Listbox.curselection()
        task_Listbox.delete(select_task_index)
    except:
        messagebox.showwarning(("Warning", "You must  select a task to delete"))

root = Tk()
root.title("to-do List")
task_Listbox = Listbox(root, width=50, height=10 , bd=2, selectbackground="red")
task_Listbox.pack(fill=BOTH, pady=10)

entry= Entry(root, width=50, bg='Light Blue', fg='red')
entry.pack(pady=10)

add_button= Button(root, text="Add task", command=add_task)
add_button.pack(pady=5)

delete_button = Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)
root.mainloop()
