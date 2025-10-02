"""Jogo de adivinhação com diferentes níveis de dificuldade.

Este módulo nasceu como um pequeno exercício, mas agora possui
tratamento de erros, seleção de nível e contagem de pontos.
"""

from __future__ import annotations

import random
from typing import Tuple


def solicitar_dificuldade() -> Tuple[str, int]:
    """Pergunta ao jogador qual nível deseja jogar.

    Returns
    -------
    tuple[str, int]
        Nome da dificuldade escolhida e o número máximo de tentativas.
    """

    dificuldades = [
        ("1", "Fácil", 10),
        ("2", "Médio", 6),
        ("3", "Difícil", 3),
    ]

    print("Escolha o nível de dificuldade:")
    for codigo, nome, tentativas in dificuldades:
        print(f"{codigo} - {nome} ({tentativas} tentativas)")

    codigos_validos = {codigo: (nome, tentativas) for codigo, nome, tentativas in dificuldades}

    while True:
        escolha = input("Digite o número da dificuldade desejada: ").strip()
        if escolha in codigos_validos:
            return codigos_validos[escolha]
        print("Opção inválida. Tente novamente usando 1, 2 ou 3.\n")


def obter_chute(minimo: int = 1, maximo: int = 100) -> int:
    """Solicita um chute válido ao usuário.

    Parameters
    ----------
    minimo, maximo
        Limites aceitos para o número digitado.
    """

    while True:
        entrada = input(f"Digite um número entre {minimo} e {maximo}: ").strip()
        try:
            chute = int(entrada)
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.\n")
            continue

        if minimo <= chute <= maximo:
            return chute

        print(f"Número fora do intervalo permitido ({minimo}-{maximo}). Tente novamente.\n")


def jogar_adivinhacao() -> None:
    """Executa o jogo completo de adivinhação."""

    print("***********************************")
    print("Bem-vindo ao jogo de Adivinhação!")
    print("***********************************")

    nome_dificuldade, tentativas_disponiveis = solicitar_dificuldade()
    numero_secreto = random.randint(1, 100)
    pontos = 1000

    print(f"\nVocê escolheu o nível {nome_dificuldade}. Vamos começar!\n")

    for rodada in range(1, tentativas_disponiveis + 1):
        print(f"Tentativa {rodada} de {tentativas_disponiveis}")
        chute = obter_chute()

        acertou = chute == numero_secreto
        maior = chute > numero_secreto

        if acertou:
            print(f"Parabéns! Você acertou o número secreto e fez {pontos} pontos!\n")
            break

        diferenca = abs(numero_secreto - chute)
        pontos_perdidos = diferenca * 10
        pontos = max(pontos - pontos_perdidos, 0)

        if maior:
            print("Você errou! O seu chute foi maior que o número secreto.\n")
        else:
            print("Você errou! O seu chute foi menor que o número secreto.\n")
    else:
        print(f"Suas tentativas acabaram! O número secreto era {numero_secreto}.\n")

    print(f"Fim do jogo! Sua pontuação final foi de {pontos} ponto(s).\n")


if __name__ == "__main__":
    jogar_adivinhacao()