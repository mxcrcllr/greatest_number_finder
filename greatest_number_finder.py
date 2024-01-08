import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Greatest Number Finder")

def greatest_num():
    
        # Ask user for the 1st number input
        num_one = float(entry_num_one.get())

        # Ask user for the 2nd number input
        num_two = float(entry_num_two.get())

        # Ask user for the 3rd number input
        num_three = float(entry_num_three.get())
        
        # Check if the 1st number is greater than both the 2nd and 3rd numbers
        if num_one > num_two and num_one > num_three:
            # If true, print 1st number
            result_label.config(text=f"{num_one}")
        
        # If false, go to the next condition
        else:
            #Check if the 2nd number is greater than both the 1st and 3rd numbers
            if num_two > num_one and num_two > num_three:
                # If true, print 2nd number
                result_label.config(text=f"{num_two}")

            # If both of the conditions are false, go to the next condition
            else:
                #Check if the 3rd number is greater than both the 1st and 2nd numbers
                if num_three > num_one and num_three > num_two:
                    #If true, print 3rd number
                    result_label.config(text=f"{num_three}")

                #If all conditions are false, print that they're all equal
                else:
                    #print("They're all equal!")
                    result_label.config(text=f"They're all equal!")

label_num_one = tk.Label(root, text="Enter the first number:")
label_num_one.pack()

entry_num_one = tk.Entry(root)
entry_num_one.pack()

label_num_two = tk.Label(root, text="Enter the second number:")
label_num_two.pack()

entry_num_two = tk.Entry(root)
entry_num_two.pack()

label_num_three = tk.Label(root, text="Enter the third number:")
label_num_three.pack()

entry_num_three = tk.Entry(root)
entry_num_three.pack()

button = tk.Button(root, text="Find Greatest Number", command=greatest_num)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

