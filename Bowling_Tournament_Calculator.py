import tkinter as tk

def calculate_handicap():
    # get the average scores from the entry widgets
    last_year_handicap = float(last_year_handicap_entry.get())
    this_year_avg = float(this_year_avg_entry.get())

    # calculate the average of the two scores
    lyhandicap = last_year_handicap
    nhandicap = (200 - this_year_avg) * 0.9
    # calculate the handicap using the formula

    handicap = lyhandicap+nhandicap/2

    # calculate handicap with %20 Rule (incomplete)
    up20 = lyhandicap+(lyhandicap*.2)
    down20 = lyhandicap-(lyhandicap*.2)
    if float(handicap)>float(up20):
        handicap = handicap+(handicap*.2)
    elif float(handicap)<float(down20):
        handicap = handicap-(handicap*.2)

    # set the label text to the calculated handicap
    handicap_label.config(text=f"Handicap: {handicap:.1f}")

# create the main window
window = tk.Tk()
window.title("Handicap Calculator")

# create a label for the last year's average score
New_Player_Label = tk.Label(window, text="New Players Beginning Handicap",fg='Red')
New_Player_Label.pack()
New_Player_options_Label1 = tk.Label(window, text="Men 16+ Years = 45 | Women 16+ Years = 72",fg='Red')
New_Player_options_Label1.pack()
New_Player_options_Label1 = tk.Label(window, text="14-16 Years = 81 | 12-14 Years = 90 | 10-11 Years = 108",fg='Red')
New_Player_options_Label1.pack()
last_year_handicap_label = tk.Label(window, text="Last Year's Handicap:")
last_year_handicap_label.pack()

# create an entry widget for the last year's average score
last_year_handicap_entry = tk.Entry(window)
last_year_handicap_entry.pack()

# create a label for this year's average score
this_year_avg_label = tk.Label(window, text="This Year's Average Score:")
this_year_avg_label.pack()

# create an entry widget for this year's average score
this_year_avg_entry = tk.Entry(window)
this_year_avg_entry.pack()

# create a button to calculate the handicap
calculate_button = tk.Button(window, text="Calculate Handicap", command=calculate_handicap)
calculate_button.pack()

# create a label to display the handicap
handicap_label = tk.Label(window, text="Handicap:")
handicap_label.pack()

# run the main loop
window.mainloop()
