# algoritmo_search_shift_and.py

def search_shift_and(text, pattern):
    m = len(pattern)
    n = len(text)
    
    # Se padrão ou texto forem vazios, ou padrão maior que o texto, nenhuma ocorrência.
    if m == 0 or n == 0 or m > n:
        return []
    
    # Pré-processamento: cria máscara de bits para cada caractere do padrão
    # Para o Shift-And com deslocamento à ESQUERDA,
    # o caractere pattern[i] fica no bit i (LSB=bit0, MSB=bit m-1).
    mask = {}
    for i, char in enumerate(pattern):
        if char not in mask:
            mask[char] = 0
        mask[char] |= 1 << i
    
    # Máscara de aceitação: é o bit que representa o último caractere do padrão
    accept_mask = 1 << (m - 1)
    
    occurrences = []
    state = 0  # estado inicial (nenhum caractere do padrão "casado" ainda)
    
    for pos, char in enumerate(text):
        # 1) Desloca o estado para a esquerda e faz OR com 1  => (state << 1) | 1
        # 2) Aplica bitwise AND com a máscara do caractere atual => & mask.get(char, 0)
        #    (Se o caractere não estiver no dicionário, retorna 0, pois não casa)
        state = ((state << 1) | 1) & mask.get(char, 0)
        
        # Se o bit correspondente ao último caractere estiver setado em state,
        # significa que "m" caracteres consecutivos corresponderam ao padrão
        if state & accept_mask:
            start_pos = pos - m + 1
            occurrences.append(start_pos)
    
    return occurrences


# o que corrigiu o ultimo bug:
# Definição da máscara: antes, o código usava mask[char] |= 1 << (m - 1 - i), o que é adequado se a gente deslocasse o estado para a direita a cada caractere. Mas, como a linha de código faz state = ((state << 1) | 1) & mask.get(char, 0), a gente desloca para a esquerda. Nesse caso, a primeira letra do padrão deve ativar o bit 0, a segunda o bit 1, e assim por diante, deixando o último caractere no bit m-1.