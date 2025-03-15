# algoritmo_shiftand.py
def search_shift_and(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m == 0 or n == 0 or m > n:
        return []
    
    # Pré-processamento: cria máscaras de caracteres
    mask = {}
    for i in range(m):
        char = pattern[i]
        if char not in mask:
            mask[char] = 0
        mask[char] |= 1 << (m - 1 - i)
    
    # Máscara de estado e máscara de aceitação
    state = 0
    accept_mask = 1 << (m - 1)
    occurrences = []
    
    for pos in range(n):
        char = text[pos]
        # Atualiza o estado
        state = ((state << 1) | 1) & mask.get(char, 0)
        
        # Verifica se encontrou uma ocorrência
        if (state & accept_mask) != 0:
            start_pos = pos - m + 1
            occurrences.append(start_pos)
    
    return occurrences