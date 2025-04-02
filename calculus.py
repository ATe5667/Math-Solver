import tkinter as tk
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def derivative(root, clear_screen):
    clear_screen()

    title = tk.Label(root, text="Compute a Derivative", font=("Helvetica", 24))
    title.pack(pady=10)

    entry_label = tk.Label(root, text="Enter the equation of the curve (e.g., x**2 - 4*x + 4 = 0):", font=("Helvetica", 16))
    entry_label.pack(pady=5)

    entry = tk.Entry(root, font=("Helvetica", 16), width=40)
    entry.pack(pady=5)

    var_label = tk.Label(root, text="Enter the x-coordinate: ", font=("Helvetica", 16))
    var_label.pack(pady=5)

    var_entry = tk.Entry(root, font=("Helvetica", 16), width=10)
    var_entry.pack(pady=5)

    solution_frame = tk.Frame(root)
    solution_frame.pack(pady=10)

    def display_latex_expression(expression):
        for widget in solution_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(10, 1))
        ax.text(0.5, 0.5, f"${sp.latex(expression)}$", fontsize=16, ha='center', va='center')
        ax.axis("off")

        canvas = FigureCanvasTkAgg(fig, master=solution_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()
        canvas.draw()

    def compute_derivative():
        try:
            x = sp.symbols('x')
            expr = sp.sympify(entry.get())
            x_value = float(var_entry.get())
            
            derivative_expr = sp.diff(expr, x)
            derivative_value = derivative_expr.subs(x, x_value)
            
            result = f"Derivative: {sp.latex(derivative_expr)}, Evaluated at x={x_value}: {derivative_value}" 
            display_latex_expression(result)
        except Exception as e:
            with open("error_log.txt", "a") as log_file:
                log_file.write(f"Error: {str(e)}\n")
            display_latex_expression("Invalid input. Check your equation and x-coordinate.")

    solve_button = tk.Button(root, text="Solve", font=("Helvetica", 16), bg="blue", fg="white", command=compute_derivative)
    solve_button.pack(pady=10)

def integral(root, clear_screen):
    clear_screen()

def limits(root, clear_screen):
    clear_screen()

def symbolic_differentiation(root, clear_screen):
    clear_screen()

def symbolic_integration(root, clear_screen):
    clear_screen()