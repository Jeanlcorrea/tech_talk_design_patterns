from abc import ABC, abstractmethod
from payment_method import PaymentMethod, CreditCardPayment, PayPalPayment


# CREATOR: INTERFACE DA FÁBRICA

class PaymentFactory(ABC):

    @abstractmethod
    def create_payment_method(self) -> PaymentMethod:
        raise NotImplementedError()


# CONCRETE CREATOR: FÁBRICA PARA PAGAMENTO POR CARTÃO DE CRÉDITO

class CreditCardPaymentFactory(PaymentFactory):
    def create_payment_method(self) -> PaymentMethod:
        return CreditCardPayment()


# CONCRETE CREATOR: FÁBRICA PARA PAGAMENTO POR PAYPAL

class PayPalPaymentFactory(PaymentFactory):

    def create_payment_method(self) -> PaymentMethod:
        return PayPalPayment()
