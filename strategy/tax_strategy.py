from abc import ABC, abstractmethod


# INTERFACE DE ESTRATÉGIA

class TaxStrategy(ABC):

    @abstractmethod
    def calculate_tax(self, amount: float) -> float:
        raise NotImplementedError()


# ESTRATÉGIA PARA VENDAS

class SalesTaxStrategy(TaxStrategy):

    def calculate_tax(self, amount: float) -> float:
        return amount * 0.1  # 10% de imposto sobre vendas


# ESTRATÉGIA PARA SERVIÇOS

class ServiceTaxStrategy(TaxStrategy):

    def calculate_tax(self, amount: float) -> float:
        return amount * 0.15  # 15% de imposto sobre serviços
