class CompoundInterest:
    def __init__(self, present_value, interest_per_year, number_of_years, capitalizations_per_year):
        self.present_value = present_value
        self.interest_per_year = interest_per_year
        self.number_of_years = number_of_years
        self.capitalizations_per_year = capitalizations_per_year
    
    def calculate_interest(self):
        """
        Calculate the compound interest for each capitalization period and return a list of values.

        Returns:
            list of tuple: Each tuple contains the year, period within that year, and the calculated value.
        """
        results = []
        amount = self.present_value
        rate_per_period = self.interest_per_year / 100 / self.capitalizations_per_year

        for year in range(1, self.number_of_years + 1):
            for period in range(1, self.capitalizations_per_year + 1):
                amount *= (1 + rate_per_period)
                results.append((year, period, amount))

        return results
