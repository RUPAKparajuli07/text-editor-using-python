import tkinter as tk
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Notpad - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Notpad - {filepath}")

window = tk.Tk()
window.title("")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Set the default font style, size, and family for the Text widget
text_font = tkFont.Font(family="Helvetica", size=12, weight="normal")
txt_edit = tk.Text(window, font=text_font)

# Create a tag for bold text
bold_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
txt_edit.tag_configure("bold", font=bold_font)

# Create a tag for italic text
italic_font = tkFont.Font(family="Helvetica", size=12, slant="italic")
txt_edit.tag_configure("italic", font=italic_font)

# Create a tag for colored text
txt_edit.tag_configure("red", foreground="red")
txt_edit.tag_configure("blue", foreground="blue")
txt_edit.tag_configure("green", foreground="green")

# Create a tag for highlighted text
txt_edit.tag_configure("highlight", background="yellow")

fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# Add buttons to apply font styles, sizes, and colors
bold_btn = tk.Button(fr_buttons, text="Bold", command=lambda: txt_edit.tag_add("bold", tk.SEL_FIRST, tk.SEL_LAST))
italic_btn = tk.Button(fr_buttons, text="Italic", command=lambda: txt_edit.tag_add("italic", tk.SEL_FIRST, tk.SEL_LAST))
red_btn = tk.Button(fr_buttons, text="Red", command=lambda: txt_edit.tag_add("red", tk.SEL_FIRST, tk.SEL_LAST))
blue_btn = tk.Button(fr_buttons, text="Blue", command=lambda: txt_edit.tag_add("blue", tk.SEL_FIRST, tk.SEL_LAST))
green_btn = tk.Button(fr_buttons, text="Green", command=lambda: txt_edit.tag_add("green", tk.SEL_FIRST, tk.SEL_LAST))
highlight_btn = tk.Button(fr_buttons, text="Highlight", command=lambda: txt_edit.tag_add("highlight", tk.SEL_FIRST, tk.SEL_LAST))

bold_btn.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
italic_btn.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
red_btn.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
blue_btn.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
green_btn.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
highlight_btn.grid(row=7, column=0, sticky="ew", padx=5, pady=5)

window.mainloop()
 
