from abc import ABC, abstractmethod


# PRODUTO: INTERFACE PARA MÉTODOS DE PAGAMENTO

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount: float):
        raise NotImplementedError()


# PRODUTO CONCRETO: PAGAMENTO POR CARTÃO DE CRÉDITO

class CreditCardPayment(PaymentMethod):

    def pay(self, amount: float):
        return f"Pagando ${amount:.2f} com Cartão de Crédito."


# PRODUTO CONCRETO: PAGAMENTO POR PAYPAL

class PayPalPayment(PaymentMethod):

    def pay(self, amount: float):
        return f"Pagando ${amount:.2f} com PayPal."
