import tkinter.ttk
from tkinter import *
from tkinter import messagebox

import googletrans
import textblob


# functions
# translate button function
def translate():
    # resets the output box
    output_text.delete(1.0, END)

    try:
        # takes the key value for selected language in the input dropdown menu
        for key, value in languages.items():
            if value == input_lang.get():
                from_lang_key = key

        # takes the key value for selected language in the output dropdown menu
        for key, value in languages.items():
            if value == output_lang.get():
                to_lang_key = key

        # stores the input text into a variable to be processed
        words = textblob.TextBlob(input_text.get(1.0, END))

        # translates the input stored in the variable words
        words = words.translate(from_lang=from_lang_key, to=to_lang_key)

        # gives final output in the output text box
        output_text.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("TRANSLATOR", str(e))


root = Tk()
root.title("Translator 1.0")
root.geometry("700x300")

# icon
icon_image = PhotoImage(file="images/icon.png")
root.iconphoto(False, icon_image)

# Storing all language
languages = googletrans.LANGUAGES
language_list = list(languages.values())

# Preparing the input area
input_lang = tkinter.ttk.Combobox(root, values=language_list, font="Roboto 10", state="r")
input_lang.place(x=90, y=50)
input_lang.set("english")

f_input = Frame(root, bg="ghost white", bd=5)
f_input.place(x=44, y=105, width=280, height=160)
input_text = Text(f_input, font="Roboto 15", relief=RIDGE, wrap=WORD)
input_text.place(x=0, y=0, width=250, height=150)

input_scroll = Scrollbar(f_input)
input_scroll.pack(side="right", fill="y")

input_scroll.configure(command=input_text.yview)
input_text.configure(yscrollcommand=input_scroll.set)

# Output area
output_lang = tkinter.ttk.Combobox(root, values=language_list, font="Roboto 10", state="r")
output_lang.place(x=422, y=50)
output_lang.set("SELECT LANGUAGE")

f_output = Frame(root, bg="ghost white", bd=5)
f_output.place(x=376, y=105, width=280, height=160)
output_text = Text(f_output, font="Roboto 15", relief=RIDGE, wrap=WORD)
output_text.place(x=0, y=0, width=250, height=150)

output_scroll = Scrollbar(f_output)
output_scroll.pack(side="right", fill="y")

output_scroll.configure(command=output_text.yview)
output_text.configure(yscrollcommand=output_scroll.set)

# Translate Button
translate_button = tkinter.Button(
    root,
    text="TRANSLATE",
    command=translate,  # Function to call when the button is clicked
    font=("Roboto", 7, "bold"),  # Font and font size
    fg="black",  # Text color
    bg="grey",  # Background color
    activeforeground="white",  # Text color when the button is under the cursor
    activebackground="black",  # Background color when the button is under the cursor
    height=2,  # Button height
    width=10,  # Button width
    relief="raised",  # Button relief
    bd=1,  # Border size
)
translate_button.place(x="310", y="50")

root.configure(bg="white")
root.mainloop()
