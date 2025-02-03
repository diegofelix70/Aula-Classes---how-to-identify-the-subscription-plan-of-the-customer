## Descrição do Código

Este código implementa uma classe chamada `Cliente` em Python, que simula um sistema simples de gerenciamento de planos de assinatura para visualização de filmes. A classe possui os seguintes recursos:

### Atributos
- **`nome`**: Nome do cliente.
- **`email`**: Email do cliente.
- **`plano`**: Plano de assinatura do cliente (pode ser "basic" ou "premium").
- **`planos`**: Lista de planos disponíveis.

### Métodos
- **`__init__`**: Inicializa o cliente com nome, email e plano. Valida se o plano é válido.
- **`mudar_plano`**: Permite ao cliente mudar de plano, desde que o novo plano seja válido.
- **`ver_filme`**: Verifica se o cliente pode assistir a um filme com base no seu plano e no plano necessário para o filme.

### Lógica de Negócio
- Um cliente com plano **"premium"** pode assistir a qualquer filme.
- Um cliente com plano **"basic"** só pode assistir a filmes que também sejam **"basic"**. Se o filme for **"premium"**, ele é solicitado a fazer um upgrade.

### Exemplo de Uso
1. Um cliente é criado com o plano **"basic"**.
2. Tenta assistir a um filme que requer plano **"premium"** e recebe uma mensagem para fazer upgrade.
3. O cliente muda para o plano **"premium"** e consegue assistir ao filme.

### Pontos Fortes do Código
- **Validação de Plano**: Garante que apenas planos válidos ("basic" ou "premium") sejam aceitos.
- **Flexibilidade**: Permite ao cliente mudar de plano.
- **Lógica Clara**: A função `ver_filme` tem uma lógica simples e eficiente para determinar se o cliente pode assistir a um filme.

---

### Saída do Código
```plaintext
basic
Faça upgrade para premium para ver esse filme
premium
Ver filme Harry Potter
