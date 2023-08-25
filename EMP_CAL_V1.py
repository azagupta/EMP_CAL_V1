import streamlit as st

# Function to calculate EMI
def calculate_emi(p, n, r):
    r = r / 100 / 12  # Convert annual rate to monthly rate
    emi = p * r * (1 + r)**n / ((1 + r)**n - 1)
    return emi

# Streamlit App
def main():
    st.title("EMI Calculator")

    # Sliders for inputs
    principal = st.slider("Principal Loan Amount", min_value=1000, max_value=100000, step=1000)
    tenure = st.slider("Loan Tenure (in years)", min_value=1, max_value=30)
    roi = st.slider("Rate of Interest (%)", min_value=1.0, max_value=20.0, step=0.1)

    # Calculate EMI
    if st.button("Calculate EMI"):
        n = tenure * 12  # Convert tenure to months
        emi = calculate_emi(principal, n, roi)
        st.write(f"EMI: {emi:.3f}")

if __name__ == "__main__":
    main()
