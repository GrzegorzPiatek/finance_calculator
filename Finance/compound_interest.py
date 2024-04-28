class CompoundInterest:
    def __init__(self, present_value, interest_per_year, number_of_years, capitalizations_per_year):
        self.present_value = present_value
        self.interest_per_year = interest_per_year
        self.number_of_years = number_of_years
        self.capitalizations_per_year = capitalizations_per_year
        self.results = []  # To store results after calculation
        self.future_value = None
        self.earn = None

    def calculate_interest(self):
        """
        Calculate the compound interest for each capitalization period and store results.
        """
        amount = self.present_value
        rate_per_period = self.interest_per_year / 100 / self.capitalizations_per_year
        self.results.append((0, 0, self.present_value))  # Include the initial investment
        
        for year in range(1, self.number_of_years + 1):
            for period in range(1, self.capitalizations_per_year + 1):
                amount *= (1 + rate_per_period)
                if period == self.capitalizations_per_year:
                    self.results.append((year, period, amount))

        self.future_value = amount
        self.earn = amount - self.present_value

    def get_results(self):
        """ Return the stored results. """
        return self.results

    def get_future_value(self):
        """ Return the calculated future value. """
        return self.future_value

    def get_earnings(self):
        """ Return the calculated earnings. """
        return self.earn
