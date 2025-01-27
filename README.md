# Controle de Estoque de Medicamentos

Este é um sistema simples de controle de estoque de medicamentos desenvolvido em Python utilizando as bibliotecas **Tkinter** para a interface gráfica e **SQLite** para o banco de dados.

## 🎯 Objetivo

O programa permite gerenciar o estoque de medicamentos, registrando informações como:
- Nome do medicamento.
- Quantidade de comprimidos disponíveis.
- Quantidade de vezes que o medicamento precisa ser tomado por dia.

Com base nesses dados, o programa calcula e exibe a **data de reposição**, indicando quando será necessário reabastecer o estoque. Além disso, o programa agora inclui funcionalidades para editar e excluir medicamentos.

---

## 🚀 Funcionalidades

- **Adicionar Medicamento**: Salva um novo medicamento no banco de dados.
- **Listar Medicamentos**: Mostra os medicamentos cadastrados com informações detalhadas.
- **Editar Medicamento**: Permite atualizar as informações de um medicamento selecionado.
- **Excluir Medicamento**: Remove um medicamento selecionado do banco de dados.
- **Cálculo Automático**: Calcula a data em que será necessário repor o medicamento com base na frequência diária de uso.
- **Armazenamento Permanente**: Os dados são salvos em um banco SQLite e permanecem disponíveis mesmo após o fechamento do programa.

---

## 🛠️ Tecnologias Utilizadas

- **Python** (versão 3.12.5)
- **Tkinter**: Biblioteca padrão para criar interfaces gráficas.
- **SQLite**: Banco de dados leve integrado ao Python.

---

## 🖥️ Requisitos para Execução

1. **Python 3.x instalado** no seu computador.
2. **Tkinter instalado** (geralmente já vem com o Python). Caso precise instalar:
   - No Linux (Ubuntu/Debian): `sudo apt-get install python3-tk`
   - No MacOS: `brew install python-tk`
3. Biblioteca SQLite (vem integrada no Python por padrão).

---

## 📦 Como Executar o Projeto

1. Clone ou baixe este repositório:
   ```bash
   https://github.com/jonathanalves522/controlhe_de_medicamentos

## 🧮 Lógica do Cálculo da Data de Reposição
A data de reposição é calculada utilizando a fórmula:

dias = quantidade de comprimidos disponíveis ÷ vezes ao dia
data de reposição = data atual + dias

## 🆕 Funcionalidades de Edição e Exclusão
##  Editar Medicamento
1. Selecione o medicamento na lista.
2. Clique no botão "Carregar para Editar".
3. Os dados do medicamento serão carregados nos campos de entrada.
4. Faça as alterações desejadas e clique em "Atualizar Medicamento".

## Excluir Medicamento
1. Selecione o medicamento na lista.
2. Clique no botão "Excluir Medicamento".
3. Confirme a exclusão. O medicamento será removido do banco de dados.


## 📝 Licença
Este projeto está licenciado sob a MIT License. Você pode usá-lo e modificá-lo livremente.



