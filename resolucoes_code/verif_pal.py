def eh_palindromo(palavra):
    # Remove espaços e transforma em minúsculas para comparação
    palavra = palavra.replace(" ", "").lower()
    # Verifica se a palavra é igual à sua inversa
    return palavra == palavra[::-1]

# Teste
palavra = input("Digite uma palavra para verificar se é um palíndromo: ")
if eh_palindromo(palavra):
    print(f'"{palavra}" é um palíndromo!')
else:
    print(f'"{palavra}" não é um palíndromo.')