from payment_factory import PaymentFactory


# CONSUMO DA RESOLUÇÃO ATRAVÉS DO CÓDIGO DO CLIENTE

def client_code(factory: PaymentFactory, amount: float):
    payment_method = factory.create_payment_method()
    print(payment_method.pay(amount))
