import tkinter as tk
import random

# Data from the problem
data = [
    ['h', 't', 'h', 't', 't', 't', 'h'],
    ['t', 't', 'h', 't', 't', 't', 'h'],
    ['t', 'h', 'h', 'h', 't', 'h', 'h'],
    ['t', 'h', 't', 't', 'h', 'h', 't'],
    ['t', 'h', 't', 'h', 'h', 't', 'h'],
    ['h', 'h', 't', 't', 'h', 't', 't'],
    ['h', 't', 'h', 't', 't', 't', 'h'],
    ['t', 't', 'h', 't', 'h', 'h', 't'],
    ['h', 't', 't', 't', 'h', 'h', 'h'],
    ['t', 't', 'h', 't', 'h', 'h', 't'],
    ['t', 'h', 't', 'h', 'h', 't', 't'],
]

# Function to calculate probabilities for a given column
def calculate_probabilities(column_data):
    total = len(column_data)
    heads = column_data.count('h')
    tails = column_data.count('t')
    return {'P(Heads)': heads / total, 'P(Tails)': tails / total}

# Calculate probabilities for each column
columns = ['H1', 'T1', 'H/T', 'H2', 'T2', 'H3', 'T3']
column_data = {col: [row[i] for row in data] for i, col in enumerate(columns)}
probabilities = {col: calculate_probabilities(column_data[col]) for col in columns}

# Simulate coin flip based on probabilities
def simulate_flip():
    selected_column = column_selector.get()
    if not selected_column:
        result_label.config(text="Please select a column!")
        return
    
    probs = probabilities[selected_column]
    outcome = random.choices(
        ['Head', 'Tail'], 
        weights=[probs['P(Heads)'], probs['P(Tails)']]
    )[0]
    result_label.config(text=f"Result: {outcome}")

# Create the GUI
root = tk.Tk()
root.title("Coin Flip Predictor")

# Dropdown for column selection
column_selector = tk.StringVar()
column_selector.set("")  # Default value
tk.Label(root, text="Select a Column:").pack(pady=5)
column_menu = tk.OptionMenu(root, column_selector, *columns)
column_menu.pack(pady=5)

# Button to run the simulation
run_button = tk.Button(root, text="Run", command=simulate_flip)
run_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
