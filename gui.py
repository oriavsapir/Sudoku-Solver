import tkinter as tk
import solver

def solve_board():
    input_board = [[int(entry.get()) for entry in row] for row in entries]
    print("---- Original Board ----")
    solver.print_board(input_board)

    solver.solve_sudoku(input_board)

    print("---- Solved Board ----")
    solver.print_board(input_board)
    window.destroy()

def validate_input(value):
    if value.isdigit() and int(value) in range(10):
        return True
    elif value == "":
        return True
    else:
        return False

# Create the main window
window = tk.Tk()
window.title("Sudoku Solver")

# Create a 9x9 grid of entry widgets
entries = []
for i in range(9):
    row_entries = []
    for j in range(9):
        entry_var = tk.StringVar()
        validate_func = window.register(validate_input)
        entry = tk.Entry(window, width=2, font=("Arial", 12), textvariable=entry_var, validate="key", validatecommand=(validate_func, "%P"))
        entry.grid(row=i, column=j)
        entry_var.set("0")  # Set initial value to 0
        row_entries.append(entry_var)
    entries.append(row_entries)

# Create a Solve button
solve_button = tk.Button(window, text="Solve", command=solve_board)
solve_button.grid(row=9, columnspan=9)

# Start the main event loop
window.mainloop()

