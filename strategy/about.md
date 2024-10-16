# Padrão Strategy

## O que é o Padrão Strategy?

O padrão Strategy é um padrão de design comportamental que permite que um algoritmo seja selecionado em tempo de execução. Ele encapsula algoritmos em classes separadas e permite que os objetos variem o comportamento de acordo com a estratégia escolhida. Isso promove a flexibilidade e a reutilização do código.

## Quando Usar

O padrão Strategy é útil quando:

- Você tem várias maneiras de realizar uma tarefa, mas deseja evitar a complexidade de condicionais.
- O algoritmo pode variar independentemente dos clientes que o utilizam.
- Você deseja encapsular um conjunto de algoritmos e torná-los intercambiáveis.

## Estrutura do Padrão

A estrutura básica do padrão Strategy inclui:

- **Contexto:** A classe que usa uma estratégia.
- **Estratégia:** Uma interface comum que define um método para a estratégia.
- **Implementações de Estratégia:** Classes concretas que implementam a interface da estratégia.

## Exemplo Prático

### Cenário

Considere um sistema de cálculo de impostos onde diferentes tipos de impostos podem ser aplicados a uma transação. Em vez de usar condicionais para determinar qual imposto calcular, você pode usar o padrão Strategy.

### Implementação

1. **Interface da Estratégia:** Define um método para calcular o imposto.
2. **Classes Concretas:** Implementam diferentes tipos de estratégias de cálculo de impostos (por exemplo, imposto sobre vendas, serviços, importações, etc.).
3. **Contexto:** Utiliza a estratégia escolhida para calcular o imposto.

### Vantagens do Padrão Strategy

- **Redução de Condicionais:** Elimina a necessidade de múltiplas instruções `if` ou `switch`, tornando o código mais limpo e fácil de manter.
- **Facilidade de Extensão:** Novas estratégias podem ser adicionadas sem modificar o código existente, apenas criando novas classes que implementam a interface da estratégia.
- **Desacoplamento:** O código do cliente não precisa conhecer a implementação específica da estratégia.

## Conclusão

O padrão Strategy é uma poderosa ferramenta para melhorar a flexibilidade e a manutenção do código. Ele permite que você encapsule comportamentos e altere a lógica em tempo de execução, promovendo um design mais limpo e modular.
