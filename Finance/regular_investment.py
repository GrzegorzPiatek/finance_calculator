class RegularInvestment:
    def __init__(self, initial_investment, interest_per_year, number_of_years, capitalizations_per_year, pmt, periods_per_year):
        self.initial_investment = initial_investment
        self.interest_per_year = interest_per_year
        self.number_of_years = number_of_years
        self.capitalizations_per_year = capitalizations_per_year
        self.pmt = pmt
        self.periods_per_year = periods_per_year
        self.results = []  # To store results after calculation
        self.future_value = None
        self.total_payments = 0  # Initialize total payments made

    def calculate_investment(self):
        """
        Calculate the future value of regular investments with periodic payments and total payments made.
        """
        rate_per_period = self.interest_per_year / 100 / self.capitalizations_per_year
        payment_periodicity = self.capitalizations_per_year // self.periods_per_year
        self.results.append((0, 0, self.initial_investment))  # Include the initial investment
        amount = self.initial_investment
        
        for year in range(1, self.number_of_years + 1):
            for period in range(1, self.capitalizations_per_year + 1):
                amount *= (1 + rate_per_period)
                if period % payment_periodicity == 0:
                    amount += self.pmt
                    self.total_payments += self.pmt
                if period == self.capitalizations_per_year:
                    self.results.append((year, period, amount))

        self.future_value = amount

    def get_results(self):
        """ Return the stored results. """
        return self.results

    def get_future_value(self):
        """ Return the calculated future value. """
        return self.future_value

    def get_total_payments(self):
        """ Return the total payments made (without compounding). """
        return self.total_payments + self.initial_investment
