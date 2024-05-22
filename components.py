from matplotlib import pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import pandas as pd
import streamlit as st

from Finance.compound_interest import CompoundInterest
from Finance.regular_investment import RegularInvestment

calculators = {
    'COMPOUND_INTEREST': 'Procent składany',
    'REGULAR_INVESTMENT': 'Regularne inwestycje'
}


def sidebar():
    """
    Create a sidebar for selecting calculator types.

    Returns:
        str: The key of the selected calculator.
    """
    st.sidebar.title("Wybór kalkulatora")
    calculator_type = st.sidebar.selectbox(
        "Wybierz kalkulator",
        options=list(calculators.keys()),
        format_func=lambda x: calculators[x],
        index=0
    )
    return calculator_type

def title():
    """
    Display the main title on the Streamlit app.
    """
    st.title("Kalkulator finansowy")

def compound_interest():
    st.header("Procent składany")
    present_value = st.number_input("[PV] Wartość początkowa (zł)", min_value=0.0, value=1000.0, step=1000.0)
    interest_per_year = st.number_input("[I/Y] Oprocentowanie w skali roku (%)", min_value=0.0, value=5.0, step=0.1)
    number_of_years = st.number_input("[N] Czas trwania inwestycji w latach", min_value=1, value=10)
    capitalizations_per_year = st.number_input("[C/Y] Liczba kapitalizacji w roku", min_value=1, value=12)

    ci = CompoundInterest(present_value, interest_per_year, number_of_years, capitalizations_per_year)
    
    if st.button("Przelicz"):
        ci.calculate_interest()
        results = ci.get_results()
        df_results = pd.DataFrame(results, columns=['Year', 'Period', 'Amount'])
        future_value = ci.get_future_value()
        earn = ci.get_earnings()
        display_results(df_results, future_value, f"Zysk: {earn:,.2f} zł")

def regular_investment():
    st.header("Regularne inwestycje")
    present_value = st.number_input("[PV] Wartość początkowa (zł)", min_value=0.0, value=0.0, step=1000.0)
    interest_per_year = st.number_input("[I/Y] Oprocentowanie w skali roku (%)", min_value=0.0, value=5.0, step=0.1)
    number_of_years = st.number_input("[N] Czas trwania inwestycji w latach]", min_value=1, value=10, step=1)
    capitalizations_per_year = st.number_input("[C/Y] Liczba kapitalizacji w roku", min_value=1, value=12)
    pmt = st.number_input("[PMT] Kwota regularnej inwestycji (zł)", min_value=0.0, value=100.0, step=100.0)
    periods_per_year = st.number_input("[P/YR] Liczba wpłat w ciągu roku", min_value=1, max_value=52, step=1)

    ri = RegularInvestment(present_value, interest_per_year, number_of_years, capitalizations_per_year, pmt, periods_per_year)
    
    if st.button("Przelicz "):
        ri.calculate_investment()
        results = ri.get_results()
        df_results = pd.DataFrame(results, columns=['Year', 'Period', 'Amount'])
        future_value = ri.get_future_value()
        total_payments = ri.get_total_payments()
        display_results(df_results, future_value, f"Całkowita wartość wpłat: {total_payments:,.2f} zł")

def plot_results(df_results, title, y_label, present_value):
    """
    Plot the investment results over time.

    Args:
    df_results (DataFrame): Data containing 'Year' and 'Amount' for plotting.
    title (str): Title of the plot.
    y_label (str): Label for the Y-axis.
    present_value (float): The initial investment value for setting Y-axis limits.
    """
    fig, ax = plt.subplots()
    ax.plot(df_results['Year'], df_results['Amount'])
    ax.set_title(title)
    ax.set_xlabel("Rok")
    ax.set_ylabel(y_label)
    ax.ticklabel_format(style='plain', axis='y')
    ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
    ax.set_ylim(bottom=min(df_results['Amount'].min(), present_value))
    return fig

def display_results(df_results, future_value, additional_info):
    """
    Display results in the Streamlit app.

    Args:
    df_results (DataFrame): Data containing detailed investment results.
    future_value (float): The final computed future value.
    additional_info (str): Additional formatted information to display, like total payments.
    """
    st.subheader("Szczegółowe wyniki:")
    st.write(f"[FV] Wartość końcowa: {future_value:,.2f} zł")
    st.write(additional_info)
    st.pyplot(plot_results(df_results, "Wzrost wartości w czasie", "Wartość (zł)", df_results['Amount'].iloc[0]))
    st.write("Szczegółowe dane:")
    st.dataframe(df_results.style.format({"Amount": "{:,.2f} zł"}))  # Formatting the Amount column as currency


def footer():
    # Add a footer
    st.markdown("""
        <style>
        .reportview-container .main .block-container{
            padding-bottom: 100px;
        }
        footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: white;
            color: black;
            text-align: center;
            padding: 0px;
        }
        </style>
        <footer>
            Autor: Grzegorz Piątek © 2024 | Kontakt: grzegorzadampiatek@gmail.com | Wersja: 0.2
        </footer>
        """, unsafe_allow_html=True)