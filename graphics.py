import tkinter as tk
import algebra
import calculus
import linAlgebra
import number
import stats
import tkinter as tk

def clear_screen(remove_back=False, remove_title=False):
    for widget in root.winfo_children():
        if not remove_title and isinstance(widget, tk.Label) and widget.cget("text") == "Math Solver":
            continue
        if not remove_back and isinstance(widget, tk.Button) and widget.cget("text") == "Back":
            continue
        widget.destroy()

def display_main_menu():
    clear_screen(remove_back=True, remove_title=True)

    title = tk.Label(root, text="Math Solver", font=("Helvetica", 30))
    title.pack()

    algebra_button = tk.Button(root, text="Algebra", width=20, height=5, bg="blue", fg="white", font=("Helvetica", 16), command=lambda: display_features("Algebra"))
    calculus_button = tk.Button(root, text="Calculus", width=20, height=5, bg="blue", fg="white", font=("Helvetica", 16), command=lambda: display_features("Calculus"))
    linear_algebra_button = tk.Button(root, text="Linear Algebra", width=20, height=5, bg="blue", fg="white", font=("Helvetica", 16), command=lambda: display_features("Linear Algebra"))
    number_button = tk.Button(root, text="Number Theory", width=20, height=5, bg="blue", fg="white", font=("Helvetica", 16), command=lambda: display_features("Numbers"))
    statistics_button = tk.Button(root, text="Statistics", width=20, height=5, bg="blue", fg="white", font=("Helvetica", 16), command=lambda: display_features("Statistics"))

    algebra_button.place(relx=0.2, rely=0.3, anchor="center")
    calculus_button.place(relx=0.5, rely=0.3, anchor="center")
    linear_algebra_button.place(relx=0.8, rely=0.3, anchor="center")
    number_button.place(relx=0.35, rely=0.6, anchor="center")
    statistics_button.place(relx=0.65, rely=0.6, anchor="center")

feature_functions = {
    "Solve a polynomial equation": algebra.solve_polynomial,
    "Solve a system of equations": algebra.solve_system,
    "Factorise an expression": algebra.factorise,
    "Expand and/or simplify an algebraic expression": algebra.expand_simplify,
    "Solve an inequality": algebra.solve_inequality,
    "2D graphing of functions": algebra.graph_functions,
    "Solve a symbolic equation": algebra.solve_symbolic_equation,
    "Simulate projectile motion": algebra.simulate_projectile_motion,

    "Compute a derivative": calculus.derivative,
    "Compute a definite integral": calculus.integral,
    "Find limits": calculus.limits,
    "Symbolic differentiation": calculus.symbolic_differentiation,
    "Symbolic integration": calculus.symbolic_integration,

    "Matrix addition": linAlgebra.matrix_addition,
    "Matrix subtraction": linAlgebra.matrix_subtraction,
    "Matrix multiplication": linAlgebra.matrix_multiplication,

    "Prime factorisation": number.prime_factorisation,
    "Greatest Common Divisor (GCD)": number.gcd,
    "Least Common Multiple (LCM)": number.lcm,

    "Basic statistics (mean, median, mode, variance, standard deviation)": stats.basic,
    "Binomial probability distribution": stats.binomial,
    "Geometric probability distribution": stats.geometric,
    "Poisson probability distribution": stats.poisson,
    "Normal probability distribution": stats.normal
}

features = {
        "Algebra": [
            "Solve a polynomial equation",
            "Solve a system of equations",
            "Factorise an expression",
            "Expand and/or simplify an algebraic expression",
            "Solve an inequality",
            "2D graphing of functions",
            "Solve a symbolic equation",
            "Simulate projectile motion"
        ],
        "Calculus": [
            "Compute a derivative",
            "Compute a definite integral",
            "Find limits",
            "Symbolic differentiation",
            "Symbolic integration"
        ],
        "Linear Algebra": [
            "Matrix addition",
            "Matrix subtraction",
            "Matrix multiplication",
        ],
        "Numbers": [
            "Prime factorisation",
            "Greatest Common Divisor (GCD)",
            "Least Common Multiple (LCM)"
        ],
        "Statistics": [
            "Basic statistics (mean, median, mode, variance, standard deviation)",
            "Binomial probability distribution",
            "Geometric probability distribution",
            "Poisson probability distribution",
            "Normal probability distribution"
        ]
    }

def display_features(topic):
    clear_screen()

    for i, feature in enumerate(features.get(topic, [])):
        func = feature_functions.get(feature, lambda r, c: print(f"No function for {feature}"))

        btn = tk.Button(root, text=feature, wraplength=300, width=30, height=2, 
                        bg="green", fg="white", font=("Helvetica", 14), 
                        command=lambda f=func: f(root, clear_screen))
        btn.pack(pady=5)

    back_button = tk.Button(root, text="Back", width=20, height=2, bg="red", fg="white", 
                            font=("Helvetica", 16), command=display_main_menu)
    back_button.pack(pady=20)

root = tk.Tk()
root.title("Math Solver")
root.geometry("1200x1000")
root.resizable(False, False)

display_main_menu()