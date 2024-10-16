from strategy.tax_context import TaxContext
from strategy.tax_strategy import ServiceTaxStrategy


def calculate_service_tax(amount: float) -> float:
    strategy = ServiceTaxStrategy()
    context = TaxContext(strategy)
    return context.calculate(amount)
