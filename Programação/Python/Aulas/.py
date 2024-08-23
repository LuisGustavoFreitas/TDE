def realizar_operacao(operacao, conjunto1, conjunto2):
    if operacao == 'U':  # União
        resultado = sorted(set(conjunto1) | set(conjunto2))
    elif operacao == 'I':  # Interseção
        resultado = sorted(set(conjunto1) & set(conjunto2))
    elif operacao == 'D':  # Diferença
        resultado = sorted(set(conjunto1) - set(conjunto2))
    elif operacao == 'C':  # Produto Cartesiano
        resultado = [(a, b) for a in conjunto1 for b in conjunto2]
    else:
        raise ValueError(f"Operação desconhecida: {operacao}")
    return resultado

def processar_linhas(linhas):
    i = 0
    while i < len(linhas):
        operacao = linhas[i].strip()
        conjunto1 = list(map(int, linhas[i+1].strip().split(',')))
        conjunto2 = list(map(int, linhas[i+2].strip().split(',')))

        resultado = realizar_operacao(operacao, conjunto1, conjunto2)
        print(f"{operacao}: Conjunto 1 {conjunto1}, Conjunto 2 {conjunto2}. Resultado: {resultado}\n")

        i += 3

def main():
    nome_arquivo = "entrada.txt"  # Nome do arquivo de entrada

    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

        processar_linhas(linhas)
    
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()