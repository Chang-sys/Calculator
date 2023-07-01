import tkinter as tk

# Function to update the display label
def update_display(value):
    current_text = display_label["text"]
    display_label["text"] = current_text + str(value)

# Function to calculate the expression and display the result
def calculate():
    expression = display_label["text"]
    try:
        # Replace the "%" symbol with "/100*" to perform modulo operation
        expression = expression.replace("%", "/100*")
        result = eval(expression)
        display_label["text"] = str(result)
    except:
        display_label["text"] = "Error"

# Function to clear the display
def clear_display():
    display_label["text"] = ""

# Function to toggle positive/negative sign
def toggle_sign():
    expression = display_label["text"]
    if expression.startswith("-"):
        display_label["text"] = expression[1:]
    else:
        display_label["text"] = "-" + expression

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the display label
display_label = tk.Label(window, text="", anchor="e", width=20, font=("Arial", 30), bg="#000000", fg="#ffffff")
display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the buttons
buttons = [
    ("AC", 1, 0, "gray", clear_display),
    ("+/-", 1, 1, "gray", toggle_sign),
    ("% ", 1, 2, "gray", lambda: update_display("%")),
    ("/", 1, 3, "orange", lambda: update_display("/")),
    ("7", 2, 0, "black", lambda: update_display(7)),
    ("8", 2, 1, "black", lambda: update_display(8)),
    ("9", 2, 2, "black", lambda: update_display(9)),
    ("*", 2, 3, "orange", lambda: update_display("*")),
    ("4", 3, 0, "black", lambda: update_display(4)),
    ("5", 3, 1, "black", lambda: update_display(5)),
    ("6", 3, 2, "black", lambda: update_display(6)),
    ("-", 3, 3, "orange", lambda: update_display("-")),
    ("1", 4, 0, "black", lambda: update_display(1)),
    ("2", 4, 1, "black", lambda: update_display(2)),
    ("3", 4, 2, "black", lambda: update_display(3)),
    ("+", 4, 3, "orange", lambda: update_display("+")),
    ("0", 5, 0, "black", lambda: update_display(0)),
    (".", 5, 2, "black", lambda: update_display(".")),
    ("=", 5, 3, "orange", calculate),
]

# Create the buttons and bind them to the appropriate functions
for btn_text, row, col, bg_color, command in buttons:
    # Check if the button is "0" and set columnspan accordingly
    if btn_text == "0":
        btn = tk.Button(window, text=btn_text, width=11, height=2, font=("Arial", 23), bg=bg_color, fg="#fff", command=command)
        btn.grid(row=row, column=col, columnspan=2, padx=5, pady=5, sticky="nsew")
    else:
        btn = tk.Button(window, text=btn_text, width=5, height=2, font=("Arial", 23), bg=bg_color, fg="#fff", command=command)
        btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")


# Configure grid weights to make the buttons expand and fill the window
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(6):
    window.grid_rowconfigure(i, weight=1)

# Run the main loop
window.mainloop()
