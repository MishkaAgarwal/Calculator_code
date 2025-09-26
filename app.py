import streamlit as st

def calculate(num1, num2, operation):
    """Performs the selected mathematical operation."""
    if operation == "Add (+)" or operation == "+":
        return num1 + num2
    elif operation == "Subtract (-)" or operation == "-":
        return num1 - num2
    elif operation == "Multiply (*)" or operation == "*":
        return num1 * num2
    elif operation == "Divide (/)" or operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    return "Error: Invalid operation"

# --- Streamlit App Layout ---
st.title("🔢 Simple Streamlit Calculator")
st.markdown("---")

# Input fields for numbers
try:
    number1 = st.number_input("Enter the first number:", value=0.0, step=0.01, format="%.2f", key="num1")
except Exception:
    number1 = 0.0

try:
    number2 = st.number_input("Enter the second number:", value=0.0, step=0.01, format="%.2f", key="num2")
except Exception:
    number2 = 0.0

# Dropdown for operation selection
operation = st.selectbox(
    "Select the operation:",
    ("Add (+)", "Subtract (-)", "Multiply (*)", "Divide (/)")
)

st.markdown("---")

# Button to trigger calculation
if st.button("Calculate Result"):
    # Perform the calculation
    result = calculate(number1, number2, operation)

    # Display the result
    st.subheader("Result:")
    if isinstance(result, str) and "Error" in result:
        st.error(result)
    else:
        st.success(f"The result of {number1} {operation[-3:-2].strip()} {number2} is **{result}**")

# Optional: Add a brief description or instruction
st.markdown(
    """
    <p style='font-size: small; color: gray;'>
    Enter two numbers, select an operation, and click 'Calculate Result'.
    </p>
    """,
    unsafe_allow_html=True
)
