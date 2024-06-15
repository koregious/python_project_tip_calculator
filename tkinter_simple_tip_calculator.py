from tkinter import *

# Window
window = Tk()
window.title("Simple Tip Calculator")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def tip_calc():
    tot_bill = float(tot_bill_input.get())
    tip_percent = float(tip_input.get())
    num_people = int(num_of_people_input.get())
    tip_value = (tip_percent / 100) + 1
    new_tot_bill = tot_bill * tip_value
    raw_bill_per_person = new_tot_bill / num_people
    bill_per_person = "{:.2f}".format(raw_bill_per_person)
    final_bill_label.config(text="{}".format(bill_per_person))
    # final_bill_label.config(text=bill_per_person)


# Entry

tot_bill_input = Entry(width=6)
tot_bill_input.grid(row=0, column=1)

tip_input = Entry(width=6)
tip_input.grid(row=1, column=1)

num_of_people_input = Entry(width=6)
num_of_people_input.grid(row=2, column=1)

# Label

tot_bill_label = Label(text="Total Bill is: ")
tot_bill_label.grid(row=0, column=0)

currency_label = Label(text="ZAR")
currency_label.grid(row=0, column=2)

tip_label = Label(text="Tip")
tip_label.grid(row=1, column=0)

percent_label = Label(text="%")
percent_label.grid(row=1, column=2)

num_of_people_label = Label(text="How many people are splitting bill?: ")
num_of_people_label.grid(row=2, column=0)

bill_per_person_label = Label(text="Bill per person is: ")
bill_per_person_label.grid(row=3, column=0)

final_bill_label = Label(text="0")
final_bill_label.grid(row=3, column=1)

final_bill_currency_label = Label(text="ZAR")
final_bill_currency_label.grid(row=3, column=2)

# Button
# trigger tip-per-person calculation when user clicks the calculate button

calculate_button = Button(text="Calculate", command=tip_calc)
calculate_button.grid(row=4, column=1)

window.mainloop()
