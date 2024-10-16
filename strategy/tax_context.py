from tax_strategy import TaxStrategy


class TaxContext:

    def __init__(self, strategy: TaxStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: TaxStrategy):
        self.strategy = strategy

    def calculate(self, amount: float) -> float:
        return self.strategy.calculate_tax(amount)
