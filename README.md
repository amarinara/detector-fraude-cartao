# 💳 Detector de Fraudes em Cartões de Crédito

Este projeto demonstra a aplicação prática de um algoritmo de **Aprendizado Supervisionado de Classificação** para identificar transações financeiras fraudulentas.

O objetivo principal é simular um cenário real onde o banco precisa de avaliar se uma transação é legítima ou se deve ser bloqueada preventivamente como fraude.

## 🧠 Como Funciona a Lógica?

Em vez de criarmos regras rígidas escritas à mão pelo programador, o modelo analisa características (variáveis) de transações passadas:
* **Valor da Transação:** Compras com valores muito fora do padrão.
* **Hora do Dia:** Transações suspeitas realizadas de madrugada.
* **Distância:** Compras feitas muito longe do endereço de residência do utilizador.

O algoritmo utilizado foi o **Random Forest Classifier** (Floresta Aleatória), que cria múltiplos caminhos de decisão para classificar as transações em:
* `0` (Transação Legítima)
* `1` (Transação Fraudulenta)

## 📁 Estrutura do Projeto

* `main.py`: O código em Python que simula os dados, treina o modelo de Inteligência Artificial e exibe os resultados.
* `requirements.txt`: Lista de dependências necessárias para executar o projeto.

## 🛠️ Como Executar este Projeto

1. Certifica-te de que tens o Python instalado no teu computador.
2. Clona este repositório ou descarrega os ficheiros.
3. No terminal, instala as dependências necessárias executando:
   ```bash
   pip install -r requirements.txt
