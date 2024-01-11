import tkinter as tk
from tkinter import messagebox, Label, font

root = tk.Tk()
root.title("Number Comparator: Greatest Number Finder")
root.geometry("460x340")
root.configure(bg='black')

font_tahoma = font.Font(family="Microsoft JhengHei UI", size=13, weight="normal")
font_palatino = font.Font(family="Palatino", size=12, weight="bold")

entry_style = {'font': ('Tahoma', 13),'highlightcolor': 'green', 'bg': '#FFFFFF', 'fg': 'red', 'borderwidth': 5, 'relief': 'sunken', 'width': 20}

def greatest_num():
    try:
        # Ask user for the 1st number input
        num_one = float(entry_num_one.get())

        # Ask user for the 2nd number input
        num_two = float(entry_num_two.get())

        # Ask user for the 3rd number input
        num_three = float(entry_num_three.get())
        
        # Check if the 1st number is greater than both the 2nd and 3rd numbers
        if num_one > num_two and num_one > num_three:
            # If true, print 1st number
            result_label.config(text=f"The greatest number is {num_one}")
        
        # If false, go to the next condition
        else:
            #Check if the 2nd number is greater than both the 1st and 3rd numbers
            if num_two > num_one and num_two > num_three:
                # If true, print 2nd number
                result_label.config(text=f"The greatest number is {num_two}")

            # If both of the conditions are false, go to the next condition
            else:
                #Check if the 3rd number is greater than both the 1st and 2nd numbers
                if num_three > num_one and num_three > num_two:
                    #If true, print 3rd number
                    result_label.config(text=f"The greatest number is {num_three}")

                #If all conditions are false, print that they're all equal
                else:
                    #print("They're all equal!")
                    result_label.config(text=f"They're all equal!")

    except ValueError:
        messagebox.showerror("Error detected", "Please enter valid numbers only.")


def on_button_release(event):
    button.config(bg='green')

label_num_one = tk.Label(root, text="\nEnter the first number:", font=font_tahoma, fg='#66FCF1', bg='black')
label_num_one.pack()

entry_num_one = tk.Entry(root, entry_style)
entry_num_one.pack()

label_num_two = tk.Label(root, text="\nEnter the second number:", font=font_tahoma, fg='#66FCF1', bg='black')
label_num_two.pack()

entry_num_two = tk.Entry(root, entry_style)
entry_num_two.pack()

label_num_three = tk.Label(root, text="\nEnter the third number:", font=font_tahoma, fg='#66FCF1', bg='black')
label_num_three.pack()

entry_num_three = tk.Entry(root, entry_style)
entry_num_three.pack()

tk.Label(root, text="", bg='black').pack()

button = tk.Button(root, text="Generate", command=greatest_num, font=font_tahoma, padx=20, borderwidth=5, relief=tk.GROOVE)
button.pack()

button.bind('<ButtonRelease-1>', on_button_release)

result_label = tk.Label(root, text="\n\n", fg='white', bg='black', font=font_palatino)
result_label.pack()

root.mainloop()
