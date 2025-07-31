from tkinter import * #you can use asterisks to import everything but still not use the name when calling functions

window = Tk()
window.title("First GUI w/ tkinter")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20) #adds padding for all widgets

#Creating a button
def button_clicked():
    print("I got clicked!")
    new_text = input.get()
    label.config(text=new_text)

#Label
label = Label(text="I am a label", font=("Courier", 24, "bold"))
label.config(text="new text")
# label.pack() #positions in a line on teh side determined
# label.place(x=100,y=100) #places precisely; (0,0) is in the top left corner
label.grid(column=0, row=0) #creates a grid - places objects relatively
label.config(padx=100,pady=100)

#Button
button = Button(text="button", command=button_clicked)
# button.pack()
button.grid(column=1,row=1)

#Entry
input = Entry(width=10) #Add some text to begin with
print(input.get())
input.grid(column=3,row=2) #you cannot use grid and pack together

new_button = Button(text = "new button")
new_button.grid(column=2,row=0)

window.mainloop()