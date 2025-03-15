# algoritmo_bmh.py

def construir_tabela_deslocamento(padrão):
    """
    Constrói a tabela de deslocamento (shift table) para o algoritmo Boyer-Moore-Horspool.
    """
    m = len(padrão)
    tabela_deslocamento = {}
    for i in range(m - 1):
        tabela_deslocamento[padrão[i]] = m - i - 1
    return tabela_deslocamento

def buscar(texto, padrão):
    """
    Realiza a busca do padrão no texto utilizando o algoritmo Boyer-Moore-Horspool.
    Retorna o índice da primeira ocorrência ou -1 se não encontrar.
    """
    m = len(padrão)
    n = len(texto)
    tabela_deslocamento = construir_tabela_deslocamento(padrão)
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and texto[i + j] == padrão[j]:
            j -= 1
        if j == -1:
            return i  # Padrão encontrado na posição i
        else:
            deslocamento = tabela_deslocamento.get(texto[i + m - 1], m)
            i += deslocamento
    return -1  # Padrão não encontrado


# gerar_texto.py

import random
import string

def gerar_texto(tamanho):
    """
    Gera um texto aleatório de tamanho especificado.
    """
    texto = ''.join(random.choices(string.ascii_lowercase + ' ', k=tamanho))
    return texto


# interface.py

import sys
from algoritmo_bmh import buscar
from gerar_texto import gerar_texto

def escolher_tamanho_texto():
    """
    Permite ao usuário escolher o tamanho do texto a ser gerado.
    """
    print("Escolha o tamanho do texto:")
    print("1. 500 caracteres")
    print("2. 1000 caracteres")
    print("3. 1500 caracteres")
    print("4. 2000 caracteres")
    print("5. 3000 caracteres")
    
    escolha_tamanho = input("Escolha uma opção (1-5): ")
    
    tamanhos = {
        '1': 500,
        '2': 1000,
        '3': 1500,
        '4': 2000,
        '5': 3000
    }
    
    return tamanhos.get(escolha_tamanho, 500)  # Default to 500 if invalid choice

def escolher_padrao():
    """
    Permite ao usuário inserir o padrão a ser buscado.
    """
    padrao = input("Digite o padrão a ser buscado: ")
    return padrao

def main():
    """
    Função principal que coordena a execução do código.
    """
    tamanho_texto = escolher_tamanho_texto()
    texto = gerar_texto(tamanho_texto)
    
    print("\nTexto gerado:")
    print(texto[:100])  # Exibe os primeiros 100 caracteres do texto
    
    padrao = escolher_padrao()
    
    print(f"\nProcurando o padrão '{padrao}' no texto...")
    resultado = buscar(texto, padrao)
    
    if resultado != -1:
        print(f"Padrão encontrado na posição {resultado}")
    else:
        print("Padrão não encontrado.")

if __name__ == "__main__":
    main()


# test_algoritmos.py

import time
from algoritmo_bmh import buscar
from gerar_texto import gerar_texto

def testar_geracao_texto():
    """
    Testa a geração de texto para garantir que o tamanho está correto.
    """
    tamanho = 500
    texto = gerar_texto(tamanho)
    assert len(texto) == tamanho, f"Esperado tamanho {tamanho}, mas obteve {len(texto)}"

def testar_busca_bmh_encontrado():
    """
    Testa o algoritmo de busca para quando o padrão é encontrado.
    """
    texto = "a quick brown fox jumps over the lazy dog"
    padrao = "fox"
    resultado = buscar(texto, padrao)
    assert resultado == 16, f"Esperado 16, mas obteve {resultado}"

def testar_busca_bmh_nao_encontrado():
    """
    Testa o algoritmo de busca para quando o padrão não é encontrado.
    """
    texto = "a quick brown fox jumps over the lazy dog"
    padrao = "cat"
    resultado = buscar(texto, padrao)
    assert resultado == -1, f"Esperado -1, mas obteve {resultado}"

# test_desempenho.py

from algoritmo_bmh import buscar
from gerar_texto import gerar_texto
import time

def testar_desempenho():
    """
    Testa o desempenho do algoritmo para diferentes tamanhos de texto.
    """
    tamanhos = [500, 1000, 1500, 2000, 3000]
    padrao = "quick"
    
    for tamanho in tamanhos:
        texto = gerar_texto(tamanho)
        inicio = time.time()
        buscar(texto, padrao)
        fim = time.time()
        
        print(f"Tempo para buscar '{padrao}' em texto de {tamanho} caracteres: {fim - inicio:.6f} segundos")

if __name__ == "__main__":
    testar_geracao_texto()
    testar_busca_bmh_encontrado()
    testar_busca_bmh_nao_encontrado()
    print("Todos os testes passaram com sucesso!")
    testar_desempenho()
