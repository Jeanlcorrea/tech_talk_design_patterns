# Padrão Factory Method

## O que é o Padrão Factory Method?

O padrão Factory Method é um padrão de design criacional que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses decidam qual classe instanciar. Esse padrão permite que uma classe delegue a responsabilidade de criação de objetos a suas subclasses, promovendo uma maior flexibilidade e desacoplamento.

## Quando Usar

O padrão Factory Method é útil quando:

- Você não sabe com antecedência quais classes devem ser instanciadas.
- Você deseja fornecer uma interface de criação de objetos que pode ser estendida por subclasses.
- Você deseja evitar a dependência direta de classes concretas em seu código.

## Estrutura do Padrão

A estrutura básica do padrão Factory Method inclui:

- **Produto:** Uma interface ou classe abstrata que define o objeto a ser criado.
- **ConcreteProduct:** Classes que implementam a interface do Produto.
- **Creator:** Uma classe abstrata que declara o método de fábrica (factory method).
- **ConcreteCreator:** Classes que implementam o método de fábrica e retornam instâncias do ConcreteProduct.

## Exemplo Prático

### Cenário

Considere um sistema de notificação que pode enviar diferentes tipos de mensagens (como email, SMS e push notifications). Em vez de instanciar diretamente as classes de notificação, você pode usar o padrão Factory Method para criar objetos de notificação.

### Implementação

1. **Produto:** Interface de Notificação que define o método `send()`.
2. **Classes Concretas:** Implementações específicas de Notificação (EmailNotification, SMSNotification, etc.).
3. **Creator:** Uma classe abstrata que declara o método `create_notification()`.
4. **ConcreteCreator:** Implementações específicas que criam e retornam instâncias de notificações.

### Vantagens do Padrão Factory Method

- **Desacoplamento:** Reduz a dependência entre o código do cliente e as classes concretas, facilitando a manutenção e extensão do código.
- **Flexibilidade:** Permite que o código seja modificado para suportar novos tipos de produtos sem a necessidade de alterar o código existente.
- **Organização:** Melhora a organização do código, centralizando a lógica de criação de objetos.

## Conclusão

O padrão Factory Method é uma ferramenta poderosa para lidar com a criação de objetos de forma flexível e extensível. Ele promove um design limpo e desacoplado, facilitando a manutenção e a evolução do código ao longo do tempo.
