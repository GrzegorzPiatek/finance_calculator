from matplotlib import pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import pandas as pd
import streamlit as st

from Finance.compound_interest import CompoundInterest

calculators = {
    'COMPOUND_INTEREST': 'Compound Interest',
    'CREDIT_CALCULATOR': 'Credit calculator'
}


def sidebar():
    """
    Create a sidebar for selecting calculator types.

    Returns:
        str: The key of the selected calculator.
    """
    st.sidebar.title("Calculator Selection")
    calculator_type = st.sidebar.selectbox(
        "Choose a calculator",
        options=list(calculators.keys()),
        format_func=lambda x: calculators[x],
        index=0
    )
    return calculator_type

def title():
    """
    Display the main title on the Streamlit app.
    """
    st.title("Finance Calculator")

def compound_interest():
    """
    Gather user inputs for the compound interest calculator.
    """
    st.header("Compound Interest Calculator")
    present_value = st.number_input("Present value ($)", min_value=0.0, value=1000.0)
    interest_per_year = st.number_input("Interest per year (%)", min_value=0.0, value=5.0, step=0.1)
    number_of_years = st.number_input("Number of years", min_value=1, value=10)
    capitalizations_per_year = st.number_input("Number of capitalizations per year", min_value=1, value=12)

    # Button to perform calculation
    if st.button("Calculate"):
        ci = CompoundInterest(present_value, interest_per_year, number_of_years, capitalizations_per_year)
        results = ci.calculate_interest()

        # Create a DataFrame including the initial state (year 0)
        initial_data = [(0, 0, present_value)]  # Year 0, Period 0, Initial Amount
        results_data = [(r[0], r[1], r[2]) for r in results if r[1] == capitalizations_per_year]
        df_results = pd.DataFrame(initial_data + results_data, columns=['Year', 'Period', 'Amount'])

        # Future Value and Earn calculation
        future_value = df_results['Amount'].iloc[-1]  # The last amount is the future value
        earn = future_value - present_value

        st.subheader("Results of Compound Interest Calculation:")
        st.write(f"Future Value: ${future_value:,.2f}")
        st.write(f"Earn: ${earn:,.2f}")

        # Plotting using matplotlib for better control
        fig, ax = plt.subplots()
        ax.plot(df_results['Year'], df_results['Amount'])
        ax.set_title("Compound Interest Growth Over Time")
        ax.set_xlabel("Year")
        ax.set_ylabel("Amount ($)")
        ax.ticklabel_format(style='plain', axis='y')  # Disables scientific notation
        ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))  # Format with comma as thousands separator

        ax.set_ylim(bottom=min(df_results['Amount'].min(), present_value))  # Ensure the Y-axis includes the initial value
        st.pyplot(fig)

        # Displaying the dataframe after the chart
        st.write("Detailed Compound Interest Values by Year:")
        st.dataframe(df_results.style.format({"Amount": "${:,.2f}"}))  # Formatting the Amount column as currency

def credit_calculator():
    """
    Gather user inputs for the credit calculator.
    """
    st.header("Credit Calculator")
    loan_amount = st.number_input("Loan Amount ($)", min_value=0.0, value=10000.0)
    interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, value=7.5)
    loan_term = st.number_input("Loan Term (years)", min_value=1, value=5)
    return loan_amount, interest_rate, loan_term