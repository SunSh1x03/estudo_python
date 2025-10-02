"""Utilitários para praticar operadores relacionais e condicionais.

O arquivo original tinha apenas um pequeno exemplo de comparação de números
no contexto do jogo de adivinhação. Agora o conteúdo foi organizado em
funções reutilizáveis e pequenos testes interativos.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ResultadoChute:
    """Representa o resultado da avaliação de um chute."""

    mensagem: str
    acertou: bool
    maior: bool
    menor: bool


def avaliar_chute(numero_secreto: int, chute: int) -> ResultadoChute:
    """Compara ``chute`` com ``numero_secreto`` e retorna um resumo.

    Parameters
    ----------
    numero_secreto: int
        Valor considerado correto.
    chute: int
        Valor informado pelo usuário.
    """

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        mensagem = "Você acertou!"
    elif maior:
        mensagem = "Você errou! O seu chute foi maior que o número secreto!"
    else:
        mensagem = "Você errou! O seu chute foi menor que o número secreto!"

    return ResultadoChute(mensagem=mensagem, acertou=acertou, maior=maior, menor=menor)


def demonstrar_avaliacao(numero_secreto: int) -> None:
    """Exibe uma pequena demonstração em linha de comando."""

    print("***********************************")
    print(" Demonstração de avaliação de chute ")
    print("***********************************\n")

    while True:
        entrada = input("Digite um número (ou 'sair' para encerrar): ").strip().lower()
        if entrada == "sair":
            break

        try:
            chute = int(entrada)
        except ValueError:
            print("Valor inválido! Digite um número inteiro ou 'sair'.\n")
            continue

        resultado = avaliar_chute(numero_secreto, chute)
        print(resultado.mensagem + "\n")

    print("Fim da demonstração!\n")


if __name__ == "__main__":
    demonstrar_avaliacao(numero_secreto=42)
