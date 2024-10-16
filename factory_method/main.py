from payment_factory import CreditCardPaymentFactory, PayPalPaymentFactory
from client import client_code


if __name__ == "__main__":
    amount_to_pay = 100.0

    # USANDO A FÁBRICA DE CARTÃO DE CRÉDITO

    credit_card_factory = CreditCardPaymentFactory()
    client_code(credit_card_factory, amount_to_pay)

    # USANDO A FÁBRICA DE PAYPAL

    paypal_factory = PayPalPaymentFactory()
    client_code(paypal_factory, amount_to_pay)
