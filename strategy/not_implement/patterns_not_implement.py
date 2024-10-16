class TaxCalculator:
    def __init__(self):
        self.sales_tax_rate = 0.1
        self.service_tax_rate = 0.15

    def calculate_sales_tax(self, amount):
        return amount * self.sales_tax_rate

    def calculate_service_tax(self, amount):
        return amount * self.service_tax_rate

    def display_taxes(self, amount, tax_type):
        if tax_type == "sales":
            sales_tax = self.calculate_sales_tax(amount)
            print(f"Imposto sobre vendas: ${sales_tax:.2f}")
        elif tax_type == "service":
            service_tax = self.calculate_service_tax(amount)
            print(f"Imposto sobre serviços: ${service_tax:.2f}")
        else:
            print("Tipo de imposto inválido.")

        # A QUANTIDADE DE IFS AQUI PODE CRESCER E MUITO...

if __name__ == "__main__":
    amount = 100.0

    tax_calculator = TaxCalculator()

    tax_calculator.display_taxes(amount, "sales")

    tax_calculator.display_taxes(amount, "service")

    tax_calculator.display_taxes(amount, "unknown")
