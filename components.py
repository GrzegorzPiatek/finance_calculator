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
    st.header("Compound Interest Calculator")
    present_value = st.number_input("Present value ($)", min_value=0.0, value=1000.0)
    interest_per_year = st.number_input("Interest per year (%)", min_value=0.0, value=5.0, step=0.1)
    number_of_years = st.number_input("Number of years", min_value=1, value=10)
    capitalizations_per_year = st.number_input("Number of capitalizations per year", min_value=1, value=12)

    ci = CompoundInterest(present_value, interest_per_year, number_of_years, capitalizations_per_year)

    if st.button("Calculate"):
        ci.calculate_interest()
        results = ci.get_results()
        df_results = pd.DataFrame(results, columns=['Year', 'Period', 'Amount'])

        future_value = ci.get_future_value()
        earn = ci.get_earnings()

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