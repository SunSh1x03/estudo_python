"""Aplicativo simples de gerenciamento de pentes.

Este script fornece um menu em linha de comando para administrar um
pequeno estoque de pentes, permitindo cadastrar, listar, buscar,
atualizar estoque e remover itens. Os dados são persistidos em um
arquivo JSON localizado no mesmo diretório do script.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict

ARQUIVO_DADOS = Path(__file__).with_name("pentes_data.json")


@dataclass
class Pente:
    """Representa um pente no estoque."""

    codigo: str
    modelo: str
    material: str
    preco: float
    estoque: int


def carregar_pentes() -> Dict[str, Pente]:
    """Carrega os pentes do arquivo JSON, se existir."""

    if not ARQUIVO_DADOS.exists():
        return {}

    try:
        conteudo = json.loads(ARQUIVO_DADOS.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("Arquivo de dados corrompido. Iniciando com estoque vazio.")
        return {}

    pentes: Dict[str, Pente] = {}
    for item in conteudo:
        try:
            pente = Pente(
                codigo=item["codigo"],
                modelo=item["modelo"],
                material=item["material"],
                preco=float(item["preco"]),
                estoque=int(item["estoque"]),
            )
        except (KeyError, TypeError, ValueError):
            print(f"Registro inválido encontrado e ignorado: {item}")
            continue
        pentes[pente.codigo] = pente
    return pentes


def salvar_pentes(pentes: Dict[str, Pente]) -> None:
    """Salva os pentes no arquivo JSON."""

    dados = [asdict(pente) for pente in pentes.values()]
    ARQUIVO_DADOS.write_text(
        json.dumps(dados, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def solicitar_float(mensagem: str) -> float:
    """Solicita um número decimal ao usuário."""

    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Valor inválido. Tente novamente usando apenas números.")


def solicitar_int(mensagem: str) -> int:
    """Solicita um número inteiro ao usuário."""

    while True:
        entrada = input(mensagem).strip()
        try:
            return int(entrada)
        except ValueError:
            print("Valor inválido. Tente novamente com um número inteiro.")


def cadastrar_pente(pentes: Dict[str, Pente]) -> None:
    """Adiciona um novo pente ao estoque."""

    codigo = input("Código do pente: ").strip()
    if not codigo:
        print("O código não pode ficar vazio.")
        return

    if codigo in pentes:
        print("Já existe um pente com esse código.")
        return

    modelo = input("Modelo: ").strip()
    material = input("Material: ").strip()
    preco = solicitar_float("Preço (R$): ")
    estoque = solicitar_int("Quantidade em estoque: ")

    pentes[codigo] = Pente(codigo, modelo, material, preco, estoque)
    salvar_pentes(pentes)
    print("Pente cadastrado com sucesso!")


def listar_pentes(pentes: Dict[str, Pente]) -> None:
    """Lista todos os pentes cadastrados."""

    if not pentes:
        print("Nenhum pente cadastrado.")
        return

    print("\nEstoque de Pentes:")
    print("-" * 60)
    for pente in pentes.values():
        print(
            f"Código: {pente.codigo}\n"
            f"  Modelo: {pente.modelo}\n"
            f"  Material: {pente.material}\n"
            f"  Preço: R$ {pente.preco:.2f}\n"
            f"  Quantidade: {pente.estoque}\n"
        )
    print("-" * 60)


def buscar_pente(pentes: Dict[str, Pente]) -> None:
    """Busca um pente pelo código."""

    codigo = input("Informe o código a buscar: ").strip()
    pente = pentes.get(codigo)
    if pente is None:
        print("Pente não encontrado.")
        return

    print(
        f"Código: {pente.codigo}\n"
        f"Modelo: {pente.modelo}\n"
        f"Material: {pente.material}\n"
        f"Preço: R$ {pente.preco:.2f}\n"
        f"Quantidade: {pente.estoque}"
    )


def atualizar_estoque(pentes: Dict[str, Pente]) -> None:
    """Atualiza a quantidade em estoque de um pente."""

    codigo = input("Código do pente: ").strip()
    pente = pentes.get(codigo)
    if pente is None:
        print("Pente não encontrado.")
        return

    quantidade = solicitar_int("Nova quantidade: ")
    pente.estoque = quantidade
    salvar_pentes(pentes)
    print("Estoque atualizado com sucesso!")


def remover_pente(pentes: Dict[str, Pente]) -> None:
    """Remove um pente do estoque."""

    codigo = input("Código do pente a remover: ").strip()
    if codigo not in pentes:
        print("Pente não encontrado.")
        return

    del pentes[codigo]
    salvar_pentes(pentes)
    print("Pente removido com sucesso!")


def exibir_menu() -> None:
    """Mostra o menu principal."""

    print(
        "\n=== Sistema de Estoque de Pentes ===\n"
        "1. Cadastrar pente\n"
        "2. Listar pentes\n"
        "3. Buscar pente\n"
        "4. Atualizar estoque\n"
        "5. Remover pente\n"
        "0. Sair"
    )


def executar() -> None:
    """Loop principal do programa."""

    pentes = carregar_pentes()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_pente(pentes)
        elif opcao == "2":
            listar_pentes(pentes)
        elif opcao == "3":
            buscar_pente(pentes)
        elif opcao == "4":
            atualizar_estoque(pentes)
        elif opcao == "5":
            remover_pente(pentes)
        elif opcao == "0":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    executar()
