def categorizar_livro(titulo,  categoria): 
    if categoria == "ficção": 
        return f"{titulo} é um livro de ficção."
    elif categoria == "não ficção": 
        return f"{titulo} é um livro de não ficção."
    elif categoria == "referência": 
        return f"{titulo} é um livro de referência."
    else: 
        return f"{titulo} não é um livro válido."

def calcular_multa(categoria,  dias_atraso): 
    if categoria == "ficção": 
        return dias_atraso * 0.50
    elif categoria == "não ficção": 
        return dias_atraso * 0.60
    else: 
        return 0

titulo = input("Digite o titulo do livro:  ")
categoria = input("Digite a categoria do livro (ficção,  não ficção,  referência):  ")
dias_atraso = int(input("Digite o número de dias em atraso:  "))

print(categorizar_livro(titulo,  categoria))
print(f"A multa é de R$ {calcular_multa(categoria,  dias_atraso): .2f}.")
