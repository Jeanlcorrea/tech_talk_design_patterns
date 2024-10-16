from strategy.use_cases.calculate_sales_tax_use_case import calculate_sales_tax
from strategy.use_cases.calculate_service_tax_use_case import calculate_service_tax


if __name__ == "__main__":
    amount = 100.0

    # CÁLCULO DE IMPOSTO SOBRE VENDAS

    sales_tax = calculate_sales_tax(amount)
    print(f"Imposto sobre vendas: ${sales_tax:.2f}")


    # CÁLCULO DE IMPOSTO SOBRE SERVIÇOS

    service_tax = calculate_service_tax(amount)
    print(f"Imposto sobre serviços: ${service_tax:.2f}")
