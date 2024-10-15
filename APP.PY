import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import symbols

# Title of the app
st.title("Scientific Graphical Calculator")

# Define a function for evaluating mathematical expressions
def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

# Define a function for graphing a mathematical function
def graph_function(function_str, x_range=(-10, 10)):
    x = symbols('x')  # Define x as a symbol
    try:
        # Parse the input function string into a sympy expression
        function = sp.sympify(function_str)
        
        # Generate data points for the graph
        x_vals = np.linspace(x_range[0], x_range[1], 400)
        y_vals = [float(function.subs(x, val)) for val in x_vals]

        # Plot the graph using matplotlib
        plt.figure(figsize=(6, 4))
        plt.plot(x_vals, y_vals, label=function_str)
        plt.title(f"Graph of {function_str}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.legend()
        st.pyplot(plt)
    except Exception as e:
        st.error(f"Error in graphing: {e}")

# Sidebar for input selection
st.sidebar.header("Calculator Options")
mode = st.sidebar.selectbox("Choose Mode", ['Calculation', 'Graph'])

# Calculation Mode
if mode == 'Calculation':
    st.header("Scientific Calculator")
    expression = st.text_input("Enter your expression (e.g., 2 + 3 * sin(pi/2))")
    
    if st.button("Calculate"):
        result = calculate_expression(expression)
        st.write(f"Result: {result}")

# Graphing Mode
elif mode == 'Graph':
    st.header("Graph Plotter")
    function_str = st.text_input("Enter a function of x (e.g., sin(x), exp(x), x**2)")
    x_min = st.number_input("X-axis minimum", value=-10)
    x_max = st.number_input("X-axis maximum", value=10)
    
    if st.button("Plot Graph"):
        graph_function(function_str, x_range=(x_min, x_max))

