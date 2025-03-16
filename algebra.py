import tkinter as tk
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def solve_polynomial(root, clear_screen):
    clear_screen()

    title = tk.Label(root, text="Solve a Polynomial Equation", font=("Helvetica", 24))
    title.pack(pady=10)

    entry_label = tk.Label(root, text="Enter the polynomial equation (e.g., x**2 - 4*x + 4 = 0):", font=("Helvetica", 16))
    entry_label.pack(pady=5)

    entry = tk.Entry(root, font=("Helvetica", 16), width=40)
    entry.pack(pady=5)

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

    def compute_solution():
        equation = entry.get()
        try:
            x = sp.symbols('x')
            parsed_eq = sp.sympify(equation.replace("=", "-(") + ")")
            solutions = sp.solve(parsed_eq, x)
            
            if not solutions:
                display_latex_expression("No real solutions")
            else:
                display_latex_expression(solutions)
        except Exception as e:
            with open("error_log.txt", "a") as log_file:
                log_file.write(f"Error: {str(e)}\n")
            display_latex_expression("Something went wrong. Check your equation.")

    solve_button = tk.Button(root, text="Solve", font=("Helvetica", 16), bg="blue", fg="white", command=compute_solution)
    solve_button.pack(pady=10)

def solve_system(root, clear_screen):
    clear_screen()

    title = tk.Label(root, text="Solve a System of Equations", font=("Helvetica", 24))
    title.pack(pady=10)

    num_eq_label = tk.Label(root, text="Enter the number of equations:", font=("Helvetica", 16))
    num_eq_label.pack(pady=5)

    num_eq_entry = tk.Entry(root, font=("Helvetica", 16), width=5)
    num_eq_entry.pack(pady=5)

    equation_entries = []
    equation_frame = tk.Frame(root)
    equation_frame.pack(pady=10)

    def generate_entries():
        for widget in equation_frame.winfo_children():
            widget.destroy()
        
        try:
            num_eq = int(num_eq_entry.get())
            equation_entries.clear()
            for i in range(num_eq):
                label = tk.Label(equation_frame, text=f"Equation {i+1}:", font=("Helvetica", 14))
                label.pack()
                entry = tk.Entry(equation_frame, font=("Helvetica", 14), width=40)
                entry.pack()
                equation_entries.append(entry)
        except ValueError:
            with open("error_log.txt", "a") as log_file:
                log_file.write("Invalid number of equations entered.\n")
            return

    generate_button = tk.Button(root, text="Generate Fields", font=("Helvetica", 14), bg="green", fg="white", command=generate_entries)
    generate_button.pack(pady=5)

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

    def compute_solution():
        try:
            equations = [sp.sympify(entry.get().replace("=", "-(") + ")") for entry in equation_entries]
            symbols = list(equations[0].free_symbols)
            solutions = sp.solve(equations, symbols)
            
            if not solutions:
                display_latex_expression("No real solutions")
            else:
                display_latex_expression(solutions)
        except Exception as e:
            with open("error_log.txt", "a") as log_file:
                log_file.write(f"Error: {str(e)}\n")
            display_latex_expression("Something went wrong. Check your equations.")

    solve_button = tk.Button(root, text="Solve", font=("Helvetica", 16), bg="blue", fg="white", command=compute_solution)
    solve_button.pack(pady=10)

def factorise(root, clear_screen):
    clear_screen()

    title = tk.Label(root, text="Factorise a Polynomial", font=("Helvetica", 24))
    title.pack(pady=10)

    entry_label = tk.Label(root, text="Enter the polynomial expression (e.g., x^2 - 4):", font=("Helvetica", 16))
    entry_label.pack(pady=5)

    entry = tk.Entry(root, font=("Helvetica", 16), width=40)
    entry.pack(pady=5)

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

    def compute_factorisation():
        equation = entry.get()
        try:
            x = sp.symbols('x')
            parsed_expr = sp.sympify(equation)
            factored_expr = sp.factor(parsed_expr)

            display_latex_expression(factored_expr)
        except Exception as e:
            with open("error_log.txt", "a") as log_file:
                log_file.write(f"Error: {str(e)}\n")
            display_latex_expression("Something went wrong. Check your input.")

    factorise_button = tk.Button(root, text="Factorise", font=("Helvetica", 16), bg="blue", fg="white", command=compute_factorisation)
    factorise_button.pack(pady=10)

def expand_simplify(root, clear_screen):
    clear_screen()

    title = tk.Label(root, text="Expand & Simplify Expression", font=("Helvetica", 24))
    title.pack(pady=10)

    entry_label = tk.Label(root, text="Enter an expression to expand and simplify:", font=("Helvetica", 16))
    entry_label.pack(pady=5)

    entry = tk.Entry(root, font=("Helvetica", 16), width=40)
    entry.pack(pady=5)

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

    def compute_expansion():
        expression = entry.get()
        try:
            x, y, z = sp.symbols('x y z')  
            parsed_expr = sp.sympify(expression)
            expanded_expr = sp.expand(parsed_expr)
            simplified_expr = sp.simplify(expanded_expr)
            display_latex_expression(simplified_expr)
        except Exception as e:
            with open("error_log.txt", "a") as log_file:
                log_file.write(f"Error: {str(e)}\n")
            display_latex_expression("Invalid Expression")

    expand_button = tk.Button(root, text="Expand & Simplify", font=("Helvetica", 16), bg="blue", fg="white", command=compute_expansion)
    expand_button.pack(pady=10)

def solve_inequality(root, clear_screen):
    clear_screen()

    title = tk.Label(root, text="Solve an Inequality", font=("Helvetica", 24))
    title.pack(pady=10)

    entry_label = tk.Label(root, text="Enter the inequality (e.g., x**2 - 4 > 0):", font=("Helvetica", 16))
    entry_label.pack(pady=5)

    entry = tk.Entry(root, font=("Helvetica", 16), width=40)
    entry.pack(pady=5)

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

    def compute_solution():
        inequality = entry.get()
        try:
            x = sp.symbols('x')
            parsed_ineq = sp.sympify(inequality)
            solution = sp.solve_univariate_inequality(parsed_ineq, x)

            display_latex_expression(solution)
        except Exception as e:
            with open("error_log.txt", "a") as log_file:
                log_file.write(f"Error: {str(e)}\n")
            display_latex_expression("Something went wrong. Check your inequality.")

    solve_button = tk.Button(root, text="Solve", font=("Helvetica", 16), bg="blue", fg="white", command=compute_solution)
    solve_button.pack(pady=10)

def graph_functions(root, clear_screen):
    clear_screen()

def solve_symbolic_equation(root, clear_screen):
    clear_screen()

def simulate_projectile_motion(root, clear_screen):
    clear_screen()