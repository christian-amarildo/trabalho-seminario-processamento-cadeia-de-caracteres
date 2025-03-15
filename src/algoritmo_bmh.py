# algoritmo_bmh.py
def search_bmh(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m == 0 or n == 0 or m > n:
        return []
    
    # Criação da tabela de deslocamento
    shift_table = {}
    for i in range(m - 1):
        shift_table[pattern[i]] = m - i - 1

    occurrences = []
    i = 0  # Posição atual no texto
    
    while i <= n - m:
        j = m - 1  # Compara do final do padrão
        
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
            
        if j == -1:
            occurrences.append(i)
            i += m  # Desloca o tamanho completo do padrão
        else:
            # Obtém o caractere atual do texto para consulta na tabela
            current_char = text[i + m - 1]
            i += shift_table.get(current_char, m)
    
    return occurrences