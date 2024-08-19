import tkinter as tk

# функция (добавляем задачу в список новых задач)
def add_task():
    task = new_task_entry.get() #забираем из поля ввода
    if task:
        new_task_listbox.insert(tk.END, task) #кладем в первый список
        new_task_entry.delete(0, tk.END) #зачистка ввода

# функция (удаляем задачу и перемещаем в колонку удаленных, 4 раздел)
def delete_task(task_listbox):
    selected_task = task_listbox.curselection()
    if selected_task:
        task = task_listbox.get(selected_task)
        task_listbox.delete(selected_task)
        deleted_task_listbox.insert(tk.END, task)

# функция (перемещает из новых задач в раздел в работе))
def mark_task_in_progress():
    selected_task = new_task_listbox.curselection()
    if selected_task:
        task = new_task_listbox.get(selected_task)
        new_task_listbox.delete(selected_task)
        in_progress_task_listbox.insert(tk.END, task)

# функция (перемещение из блока в работе в выполненные))
def mark_task_completed():
    selected_task = in_progress_task_listbox.curselection()
    if selected_task:
        task = in_progress_task_listbox.get(selected_task)
        in_progress_task_listbox.delete(selected_task)
        completed_task_listbox.insert(tk.END, task)

# функция (возврат из выполненных в работу))
def move_to_in_progress_from_completed():
    selected_task = completed_task_listbox.curselection()
    if selected_task:
        task = completed_task_listbox.get(selected_task)
        completed_task_listbox.delete(selected_task)
        in_progress_task_listbox.insert(tk.END, task)

# функция (перемещение из удаленных в работу)
def move_to_in_progress_from_deleted():
    selected_task = deleted_task_listbox.curselection()
    if selected_task:
        task = deleted_task_listbox.get(selected_task)
        deleted_task_listbox.delete(selected_task)
        in_progress_task_listbox.insert(tk.END, task)

# функция (из удаленных в новые))
def move_to_new_from_deleted():
    selected_task = deleted_task_listbox.curselection()
    if selected_task:
        task = deleted_task_listbox.get(selected_task)
        deleted_task_listbox.delete(selected_task)
        new_task_listbox.insert(tk.END, task)

# главное окно приложения
root = tk.Tk()
root.title("Task List")
root.configure(background="white")

# элементы в главном окне
text1 = tk.Label(root, text="Введите задачу", bg="white")
text1.grid(row=0, column=0, padx=10, pady=5, columnspan=2) # спасибо ЧАТу, надо с этим разобраться подробнее

new_task_entry = tk.Entry(root, width=40, bg="lightgray")
new_task_entry.grid(row=1, column=0, padx=10, pady=5, columnspan=2) # спасибо ЧАТу, надо с этим разобраться подробнее

add_task_button = tk.Button(root, text="Добавить", command=add_task, bg="lightblue")
add_task_button.grid(row=1, column=1, padx=10, pady=5) # спасибо ЧАТу, надо с этим разобраться подробнее

# ЧАТ при доработке моей версии предложил фреймы, надо углубиться в это
new_tasks_frame = tk.Frame(root, bg="white")
new_tasks_frame.grid(row=2, column=0, padx=10, pady=5, sticky="n")
in_progress_tasks_frame = tk.Frame(root, bg="white")
in_progress_tasks_frame.grid(row=2, column=1, padx=10, pady=5, sticky="n")
completed_tasks_frame = tk.Frame(root, bg="white")
completed_tasks_frame.grid(row=2, column=2, padx=10, pady=5, sticky="n")
deleted_tasks_frame = tk.Frame(root, bg="white")
deleted_tasks_frame.grid(row=2, column=3, padx=10, pady=5, sticky="n")

# список новых задач и кнопки этого раздела
new_task_label = tk.Label(new_tasks_frame, text="Новые задачи", bg="white")
new_task_label.pack(pady=5)

new_task_listbox = tk.Listbox(new_tasks_frame, height=15, width=30, bg="lightblue", selectbackground="white")
new_task_listbox.pack(pady=5)

mark_in_progress_button = tk.Button(new_tasks_frame, text="В работе", command=mark_task_in_progress, bg="lightgreen")
mark_in_progress_button.pack(pady=5)

delete_task_button_new = tk.Button(new_tasks_frame, text="Удалить", command=lambda: delete_task(new_task_listbox), bg="lightcoral") # правка от ЧАТа, он функцию удаления объединил
delete_task_button_new.pack(pady=5)

# список новых задач и кнопки этого раздела
in_progress_task_label = tk.Label(in_progress_tasks_frame, text="Задачи в работе", bg="white")
in_progress_task_label.pack(pady=5)

in_progress_task_listbox = tk.Listbox(in_progress_tasks_frame, height=15, width=30, bg="lightgreen", selectbackground="white")
in_progress_task_listbox.pack(pady=5)

mark_completed_button = tk.Button(in_progress_tasks_frame, text="Выполнено", command=mark_task_completed, bg="lightyellow")
mark_completed_button.pack(pady=5)

delete_task_button_in_progress = tk.Button(in_progress_tasks_frame, text="Удалить", command=lambda: delete_task(in_progress_task_listbox), bg="lightcoral")
delete_task_button_in_progress.pack(pady=5)

# выполненные задачи и кнопки раздела
completed_task_label = tk.Label(completed_tasks_frame, text="Выполненные задачи", bg="white")
completed_task_label.pack(pady=5)

completed_task_listbox = tk.Listbox(completed_tasks_frame, height=15, width=30, bg="lightyellow", selectbackground="white")
completed_task_listbox.pack(pady=5)

move_to_in_progress_button = tk.Button(completed_tasks_frame, text="В работу", command=move_to_in_progress_from_completed, bg="lightgreen")
move_to_in_progress_button.pack(pady=5)

delete_task_button_completed = tk.Button(completed_tasks_frame, text="Удалить", command=lambda: delete_task(completed_task_listbox), bg="lightcoral")
delete_task_button_completed.pack(pady=5)

# удаленные задачи и кнопки раздела (все было сильно проще, пока мне не пришло в голову опция возврата)
deleted_task_label = tk.Label(deleted_tasks_frame, text="Удаленные задачи", bg="white")
deleted_task_label.pack(pady=5)

deleted_task_listbox = tk.Listbox(deleted_tasks_frame, height=15, width=30, bg="lightgray", selectbackground="white")
deleted_task_listbox.pack(pady=5)

move_to_in_progress_from_deleted_button = tk.Button(deleted_tasks_frame, text="В работу", command=move_to_in_progress_from_deleted, bg="lightgreen")
move_to_in_progress_from_deleted_button.pack(pady=5)

move_to_new_from_deleted_button = tk.Button(deleted_tasks_frame, text="В новые задачи", command=move_to_new_from_deleted, bg="lightblue")
move_to_new_from_deleted_button.pack(pady=5)

delete_task_button_deleted = tk.Button(deleted_tasks_frame, text="Удалить", command=lambda: delete_task(deleted_task_listbox), bg="lightcoral")
delete_task_button_deleted.pack(pady=5)

root.mainloop()


