from customtkinter import *

app = CTk()
app.title('Number Comparator: Greatest Number Finder')
app.geometry("430x340")

set_appearance_mode('dark')

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
            result_label.configure(text=f"The greatest number is {num_one}")
        
        # If false, go to the next condition
        else:
            # Check if the 2nd number is greater than both the 1st and 3rd numbers
            if num_two > num_one and num_two > num_three:
                # If true, print 2nd number
                result_label.configure(text=f"The greatest number is {num_two}")

            # If both of the conditions are false, go to the next condition
            else:
                # Check if the 3rd number is greater than both the 1st and 2nd numbers
                if num_three > num_one and num_three > num_two:
                    # If true, print 3rd number
                    result_label.configure(text=f"The greatest number is {num_three}")

                # If all conditions are false, print that they're all equal
                else:
                    result_label.configure(text="They're all equal!")

    except Exception:
        error_label.configure(text=f"Error detected! Please input valid numbers only.")

label_num_one = CTkLabel(master=app, text="\nEnter the first number: ", font=("Tahoma", 15), text_color="#66FCF1")
label_num_one.pack()

entry_num_one = CTkEntry(master=app, placeholder_text="ex. 123", width=210, text_color="white")
entry_num_one.pack()

label_num_two = CTkLabel(master=app, text="\nEnter the second number: ", font=("Tahoma", 15), text_color="#66FCF1")
label_num_two.pack()

entry_num_two = CTkEntry(master=app, placeholder_text="ex. 123", width=210, text_color="white")
entry_num_two.pack()

label_num_three = CTkLabel(master=app, text="\nEnter the third number: ", font=("Tahoma", 15), text_color="#66FCF1")
label_num_three.pack()

entry_num_three = CTkEntry(master=app, placeholder_text="ex. 123", width=210, text_color="white")
entry_num_three.pack()

button = CTkButton(app, text="Generate", command=greatest_num, fg_color="#45A29E",border_color="#45A29E", border_width=2)
button.pack(padx=20, pady=20)

result_label = CTkLabel(app, text="", font=("Tahoma", 14), text_color="white")
result_label.pack()

error_label = CTkLabel(app, text="", font=("Tahoma", 14), text_color="red")
error_label.pack()

app.mainloop()
