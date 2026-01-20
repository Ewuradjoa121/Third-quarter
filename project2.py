from customtkinter import *


my_tasks = []


def add_task():
    task_text = task_entry.get()  
    if task_text != "":           
        my_tasks.append(task_text)  
        task_display.insert("end", "• " + task_text + "\n")  
        task_entry.delete(0, "end")  


def clear_tasks():
    task_display.delete("1.0", "end")  
    my_tasks.clear()                    

window = CTk()
window.title("My Simple Task App")
window.geometry("400x500")
window.resizable(0, 0)


main_frame = CTkFrame(window, width=400, height=500, fg_color="white")
main_frame.place(relx=0,rely=0)

title_label = CTkLabel(main_frame, text=" My Tasks", font=("Arial", 16), text_color="black")
title_label.place(relx=0.38, rely=0.05)


task_entry = CTkEntry(main_frame, width=300, placeholder_text="Type your task here...")
task_entry.place(relx=0.12, rely=0.15)


add_button = CTkButton(main_frame, text="Add Task", width=300, command=add_task)
add_button.place(relx=0.12, rely=0.25)

task_display = CTkTextbox(main_frame, width=300, height=200)
task_display.place(relx=0.12, rely=0.35)


clear_button = CTkButton(main_frame, text="Clear All Tasks", width=300, command=clear_tasks)
clear_button.place(relx=0.12, rely=0.8)


window.mainloop()
