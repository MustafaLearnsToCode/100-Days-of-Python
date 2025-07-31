from tkinter import * #you can use asterisks to import everything but still not use the name when calling functions

window = Tk()
window.title("First GUI w/ tkinter")
window.minsize(width=500, height=300)

#Creating a label
label = Label(text="I am a label", font=("Courier", 24, "bold"))
label.pack()

label["text"] = "new text"
label.config(text="new text")

#Creating a button
def button_clicked():
    # label["text"] = "Button Got Clicked"
    new_text = entry.get()
    label.config(text=new_text)

button = Button(text="Click me", command=button_clicked)
button.pack()

#Entriesfrom tkinter import * #you can use asterisks to import everything but still not use the name when calling functions

window = Tk()
window.title("First GUI w/ tkinter")
window.minsize(width=500, height=300)

#Creating a label
label = Label(text="I am a label", font=("Courier", 24, "bold"))
label.pack()

label["text"] = "new text"
label.config(text="new text")

#Creating a button
def button_clicked():
    # label["text"] = "Button Got Clicked"
    new_text = entry.get()
    label.config(text=new_text)

button = Button(text="Click me", command=button_clicked)
button.pack()

#Entries
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with.") #Add some text to begin with
print(entry.get()) #Gets text in entry
entry.pack()

#Text
text = Text(height=5, width=30)
text.focus() #Puts cursor in textbox.
text.insert(END, "Example of multi-line text entry.") #Adds some text to begin with.
print(text.get("1.0", END)) #Gets current value in textbox at line 1, character 0
text.pack()

#Spinbox
def spinbox_used():
    print(spinbox.get()) #gets the current value in spinbox.
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    print(checked_state.get()) #Prints 1 if On button checked, otherwise 0.
checked_state = IntVar() #variable to hold on to checked state, 0 is off, 1 is on.
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
radio_state = IntVar() #Variable to hold on to which radio button value is checked.
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection())) # Gets current selection from listbox

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()











window.mainloop() #has to be at the end


entry = Entry(width=30)
entry.insert(END, string="Some text to begin with.") #Add some text to begin with
print(entry.get()) #Gets text in entry
entry.pack()

#Text
text = Text(height=5, width=30)
text.focus() #Puts cursor in textbox.
text.insert(END, "Example of multi-line text entry.") #Adds some text to begin with.
print(text.get("1.0", END)) #Gets current value in textbox at line 1, character 0
text.pack()

#Spinbox
def spinbox_used():
    print(spinbox.get()) #gets the current value in spinbox.
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    print(checked_state.get()) #Prints 1 if On button checked, otherwise 0.
checked_state = IntVar() #variable to hold on to checked state, 0 is off, 1 is on.
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
radio_state = IntVar() #Variable to hold on to which radio button value is checked.
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection())) # Gets current selection from listbox

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()











window.mainloop() #has to be at the end

