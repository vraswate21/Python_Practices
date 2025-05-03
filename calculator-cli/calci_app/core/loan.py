"""this module contains the class for different types of loan calculators"""



from calci_app.core.calculator import BaseCalculator



class LoanEmiCalculator(BaseCalculator):
    """this class implements the loan EMI Calculator"""

    def __init__(self, principal, monthly_intrest_rate, tenure_in_months):
        self._principal = principal
        self._monthly_intrest_rate = monthly_intrest_rate
        self._tenure_in_months = tenure_in_months

    def calculate(self):
        """this method calculates the loan emi and return the monthly emi value"""

        pass


class TotalAmountofLoanCalculator(BaseCalculator):
    """ this calculator will respond with a total amount you will be paying"""

    """if the take the loan (principal + intrest)"""

    def __init__(self, principal, monthly_intrest_rate, tenure_in_months):
        self._principal = principal
        self._monthly_intrest_rate = monthly_intrest_rate
        self._tenure_in_months = tenure_in_months

    def calculate(self):
        """this method calculate the loan emi and return the monthly emi value"""


        pass