import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import symbols
from math import *

# Title of the app
st.title("Scientific Graphical Calculator")

# Sidebar for input selection
st.sidebar.header("Calculator Options")
mode = st.sidebar.selectbox("Choose Mode", ['Calculation', 'Graph'])

# Define a function for evaluating mathematical expressions
def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

# Define a function for graphing a mathematical function
def graph_function(function_str, x_range=(-10, 10)):
    x = symbols

    

