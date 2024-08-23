def operaçao (operação,conjunto1,conjunto2):
    if operaçao == 'U':
        resultado = sorted(set(conjunto1)) | set(conjunto2)
    elif operaçao == 'I':
        resultado = sorted(set(conjunto1) & set(conjunto2))
    elif operaçao == 'D': 
        resultado = sorted(set(conjunto1) - set(conjunto2))
    elif operaçao == 'C': 
        resultado = [(a, b) for a in conjunto1 for b in conjunto2]
    return resultado

def lerLinhas(linhas):
    i=0
    while i < len(linhas):
        operaçao = linhas[i].strip()
        conjunto1 = list(map(int, linhas[i+1].strip().split(',')))
        conjunto2 = list(map(int, linhas[i+2].strip().split(',')))

        resultado = operaçao(operaçao, conjunto1, conjunto2)
        print(f"{operaçao}:Conjunto 1 {conjunto1}, Conjunto 2 {conjunto2}. Resultado : {resultado}\n")

        i+=3

def main():
    nomeArquivo = str(input("Digite o nome do arquivo de entrada (incluindo .txt): "))

    try:
        with open(nomeArquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

    except FileNotFoundError:
        print(f"Arquivo '{nomeArquivo}' não encontrado.")

main()