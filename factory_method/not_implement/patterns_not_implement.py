class PaymentProcessor:

    def process_payment(self, method: str, amount: float):
        # VERIFICA O MÉTODO DE PAGAMENTO

        if method == "credit_card":
            self._pay_with_credit_card(amount)
        elif method == "paypal":
            self._pay_with_paypal(amount)
        elif method == "bank_transfer":
            self._pay_with_bank_transfer(amount)
        else:
            print("MÉTODO DE PAGAMENTO INVÁLIDO!")

    def _pay_with_credit_card(self, amount: float):
        if amount > 0:
            print(f"Pagando ${amount:.2f} com Cartão de Crédito. (VERIFICAÇÃO DE CRÉDITO EM ANDAMENTO...)")
        else:
            print("VALOR INVÁLIDO PARA PAGAMENTO COM CARTÃO.")

    def _pay_with_paypal(self, amount: float):
        if amount > 0:
            print(f"Pagando ${amount:.2f} com PayPal. (CONECTANDO AO PAYPAL...)")
        else:
            print("VALOR INVÁLIDO PARA PAGAMENTO COM PAYPAL.")

    def _pay_with_bank_transfer(self, amount: float):
        if amount > 0:
            print(f"Pagando ${amount:.2f} por Transferência Bancária. (CONFIRMANDO TRANSFERÊNCIA...)")
        else:
            print("VALOR INVÁLIDO PARA TRANSFERÊNCIA BANCÁRIA.")


# CÓDIGO DO CLIENTE

if __name__ == "__main__":
    processor = PaymentProcessor()

    # PAGAMENTOS COM DIFERENTES MÉTODOS... QUANTO MAIS INSTÂNCIAS, MAIS MEMÓRIA!

    processor.process_payment("credit_card", 100.0)
    processor.process_payment("paypal", 50.0)
    processor.process_payment("bank_transfer", 75.0)
    processor.process_payment("unknown_method", 30.0)
