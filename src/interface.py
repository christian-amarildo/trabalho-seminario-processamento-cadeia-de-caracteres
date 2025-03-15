# interface.py
import time
from algoritmo_bmh import search_bmh
from gerar_texto import generate_text

def select_text_size():
    print("\nOpções de tamanho de texto:")
    sizes = [500, 1000, 1500, 2000, 3000]
    for idx, size in enumerate(sizes, 1):
        print(f"{idx}. {size} caracteres")
        
    while True:
        try:
            choice = int(input("\nEscolha o tamanho (1-5): "))
            if 1 <= choice <= 5:
                return sizes[choice - 1]
            print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def select_pattern():
    return input("\nDigite o padrão a buscar: ").strip()

def main():
    print("="*50)
    print("Buscador BMH - Boyer-Moore-Horspool")
    print("="*50)
    
    size = select_text_size()
    pattern = select_pattern()
    
    # Gerar texto
    print(f"\nGerando texto com {size} caracteres...")
    text = generate_text(size)
    
    # Executar busca
    print(f"Buscando padrão '{pattern}'...")
    start_time = time.time()
    occurrences = search_bmh(text, pattern)
    elapsed = time.time() - start_time
    
    # Resultados
    print("\n" + "="*50)
    if occurrences:
        print(f"Padrão encontrado {len(occurrences)} vezes nas posições:")
        print(occurrences[:10], "..." if len(occurrences) > 10 else "")
    else:
        print("Padrão não encontrado.")
    
    print(f"\nTempo de busca: {elapsed:.6f} segundos")
    print("="*50)

if __name__ == "__main__":
    main()