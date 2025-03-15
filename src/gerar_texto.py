# gerar_texto.py
def generate_text(size):
    base_lorem = (
        "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor "
        "incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis "
        "nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat "
        "duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore "
        "eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt "
        "in culpa qui officia deserunt mollit anim id est laborum"
    )
    
    # Calcula quantas repetições são necessárias
    repeat = (size // len(base_lorem)) + 1
    text = (base_lorem * repeat)[:size]
    
    # Completa com espaços se necessário
    if len(text) < size:
        text += ' ' * (size - len(text))
    
    return text