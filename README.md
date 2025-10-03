# estudo_python

Coleção de pequenos programas escritos em Python para praticar conceitos
fundamentais da linguagem. Cada script é independente e pode ser executado
isoladamente a partir do terminal para explorar diferentes tópicos, como
estruturas condicionais, manipulação de entrada de usuário e persistência de
dados em arquivos.

## Conteúdo do repositório

| Arquivo | Descrição |
| --- | --- |
| `adivinhacao.py` | Jogo completo de adivinhação com escolha de nível (fácil, médio, difícil), validação de entrada e sistema de pontuação que considera a proximidade do chute em relação ao número secreto. |
| `administracao1_2.py` | Conjunto de utilitários reutilizáveis para comparar um chute com um número secreto, além de uma pequena demonstração interativa para estudar operadores relacionais. |
| `pentest.py` | Aplicativo de linha de comando para gerenciar um portfólio de pentests. Permite cadastrar, listar, buscar, atualizar métricas e remover registros, persistindo os dados em um arquivo JSON. |

## Requisitos

- Python 3.8 ou superior.

## Como executar

1. Clone este repositório ou baixe os arquivos para o seu computador.
2. Abra um terminal no diretório onde os scripts estão localizados.
3. Execute o programa desejado com o Python:

   ```bash
   python adivinhacao.py
   python administracao1_2.py
   python pentest.py
   ```

Cada script fornece instruções interativas diretamente no terminal, não sendo
necessário instalar dependências adicionais além da biblioteca padrão do
Python.

## Dicas adicionais

- O script `pentest.py` armazena os dados no arquivo `pentest_data.json`, criado
automaticamente no mesmo diretório quando o programa é executado pela primeira
vez.
- Para redefinir o portfólio de pentests, basta apagar o arquivo
  `pentest_data.json` antes de iniciar uma nova sessão.

Bom estudo! 🎯
