from tkinter import *
import csv

root = Tk()
root.title('Person')
root.geometry('850x250')
root.resizable(False, False)

# top level window
top = Toplevel(root)
top.title('Info')
top.geometry('200x100')
Label(top, text="You can see people's info here", bg='red').pack(fill="both", expand=True)

# Labels
Label(root, text='Name:').grid(row=0, column=0, padx=5, pady=5)
Label(root, text='Family:').grid(row=0, column=2, padx=5, pady=5)
Label(root, text='Weigh:').grid(row=0, column=4, padx=5, pady=5)
Label(root, text='Marrie:').grid(row=1, column=0, padx=5, pady=5)
Label(root, text='Height:').grid(row=1, column=4, padx=5, pady=5)
Label(root, text='Experience:').grid(row=1, column=2, padx=5, pady=5)
Label(root, text='Degree:').grid(row=2, column=0, padx=5, pady=5)
Label(root, text='Wishes:').grid(row=4, column=0, padx=5, pady=5)
l=Label(root)
l.grid(row=5, column=1,columnspan=4 , padx=5, pady=5)

# Function to save data
def save_data(vazn=None, tahol=None, qad=None, tajrobe=None, arezoo=None):
    name = name_entry.get()
    family = family_entry.get()
    weigh = weigh_spinbox.get()  # Use the Spinbox variable
    marry = t.get()  # Use the IntVar for Checkbutton
    height = qad_scale.get()  # Use the Scale variable
    experience = mode_choice.get()
    wish = text_area.get("1.0", END)

    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, family, vazn, tahol, qad, tajrobe, arezoo])

    # Clear the entries after saving
    name_entry.delete(0, END)
    family_entry.delete(0, END)
    text_area.delete("1.0", END)

# menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label='quit', command=root.quit)
filemenu.add_command(label='save', command=save_data)
root.config(menu=menubar)

# Entry fields
name_entry = Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)
family_entry = Entry(root)
family_entry.grid(row=0, column=3, padx=5, pady=5)

# Spinbox and Scale
weigh_spinbox = Spinbox(root, from_=20, to=150)  # Named Spinbox
weigh_spinbox.grid(row=0, column=5, padx=5, pady=5)

qad_scale = Scale(root, from_=100, to=200, orient=HORIZONTAL)  # Named Scale
qad_scale.grid(row=1, column=5, padx=5)

# Checkbuttons
t = IntVar()
Checkbutton(root, text="Married", variable=t).grid(row=1, column=1, padx=5, pady=5)

Degree = IntVar()
Checkbutton(root, text="junior", variable=Degree).grid(row=1, column=3, padx=5, pady=5)

# Radiobuttons
modes = [("Academic", "Academic"), ("Experimental", "Experimental"), ("Public class", "Public class"),
         ("Private class", "Private class"), ("you tube", "you tube")]
mode_choice = StringVar()
mode_choice.set("Academic")  # Default value
for index, (text, value) in enumerate(modes):
    Radiobutton(root, text=text, variable=mode_choice, value=value).grid(row=2, column=index + 1, padx=5, pady=5)

# Text widget
text_area = Text(root, width=10, height=4)  # Adjusted width for better visibility
text_area.grid(row=4, column=1, padx=5, pady=5)

# Canvas
canvas1 = Canvas(root, width=200, height=50)
canvas1.grid(row=4, column=4)
canvas1.create_text(90, 15, fill="red", font="times 20 italic bold", text="estekhdamian")

canvas2 = Canvas(root, width=200, height=50)
canvas2.grid(row=4, column=5)
canvas2.create_text(80, 15, fill="red", font="times 20 italic bold", text="group")

#button
def give():
    name = name_entry.get()
    family = family_entry.get()
    weigh = weigh_spinbox.get()  # Use the Spinbox variable
    marry = t.get()  # Use the IntVar for Checkbutton
    height = qad_scale.get()  # Use the Scale variable
    experience = mode_choice.get()
    wish = text_area.get("1.0", END)
    if marry==1 :
        p=f"{name} {family} is {height} cm tall and {weigh} kg with {experience} experiences which is married wishes {wish}"
    else :
        p= f"{name} {family} is {height} cm tall and {weigh} kg with {experience} experiences which is not married wishes {wish}"
    l.config(text=p,bg='light grey')
Button(root,text="give information",command=give).grid(row=4,column=2)

root.mainloop()
