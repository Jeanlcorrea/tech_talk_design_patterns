from strategy.tax_context import TaxContext
from strategy.tax_strategy import SalesTaxStrategy


def calculate_sales_tax(amount: float) -> float:
    strategy = SalesTaxStrategy()
    context = TaxContext(strategy)
    return context.calculate(amount)
