import tkinter as tk


def calculate_discount_percentage(total):
    if total >= 100:
        discount = 20
    elif total > 0 and total < 100:
        discount = 10
    return discount


def calculate_discount(total):
    discount_percentage = calculate_discount_percentage(total)
    discount = total - total / 100 * discount_percentage
    return discount


def get_bill_total():
    entered_bill_total = entry_box.get()

    try:
        bill_total = float(entered_bill_total)
    except ValueError:
        textbox["text"] = "Incorrect value entered"
        return

    final_total = format(calculate_discount(bill_total), '.2f')
    textbox["text"] = "£" + final_total

    print(entered_bill_total)


# create the window
window = tk.Tk()
window.geometry("400x210")
window.title("Billing Programme")

# create a lable
label = tk.Label(text="Enter Bill Total:")
label.place(x=10, y=20, height=25)
label.config(bg="lightgreen", padx=0)

# craete entry box
entry_box = tk.Entry(text="")
entry_box.place(x=10, y=40, width=110, height=25)

# create a button
button = tk.Button(text="Calculate Bill", command=get_bill_total)
button.config(font="16")
button.place(x=10, y=170, width=380, height=35)

# create a lable for total after discount
label2 = tk.Label(text="Total Price (After Discount):")
label2.place(x=140, y=20)
label2.config(bg="lightgreen", padx=0)
textbox = tk.Message(text="£0.00", width=200, font="16")
textbox.config(bg="lightgreen", padx=0)
textbox.place(x=140, y=40)


window.mainloop()


# def calculate_discount_percentage(total):
#     if total >= 100:
#         discount = 20
#     elif total > 0 and total < 100:
#         discount = 10
#     return discount


# def calculate_discount(total):
#     discount_percentage = calculate_discount_percentage(total)
#     discount = total - total / 100 * discount_percentage
#     return discount


# def get_bill_total():

#     try:
#         bill_total = float(input("Enter the amount: "))
#     except ValueError as e:
#         print('Incorrect value entered')
#         # quit() This function (callable instance objects) should only be used in the interpreter.
#         # exit()
#         sys.exit()

#     if bill_total < 1:
#         print('Incorrect value entered')
#         sys.exit()

#     final_total = format(calculate_discount(bill_total), '.2f')
#     return final_total


# def main():
#     total = get_bill_total()
#     print("£" + total)


# main()
