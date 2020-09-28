from bitstring import BitArray

FILE = "Chaves de Criptografia.txt"

def monobit(chaves: list):
    saida = []
    for chave in chaves:
        cont = 0
        for character in chave:
            if character:
                cont += 1

        if 9654 < cont < 10346:
            saida.append("Aprovado")
        else:
            saida.append("Reprovado")
    
    print("\n")
    print("Resultado da validacao Monobit Test:")
    print(saida)
    print("\n")


def chunks(lst: list, n: int):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def poker(chaves: list):
    saida = []
    for chave in chaves:
        ocorr = dict()
        pokerList = chunks(chave, 4)
        for chunk in pokerList:
            if chunk.bin in ocorr.keys():
                ocorr[chunk.bin] += 1
            else:
                ocorr[chunk.bin] = 1

        f = [ocorr ** 2 for ocorr in ocorr.values()]
        x = (16 / 5000) * sum(f) - 5000
        if 1.03 < x < 57.4:
            saida.append("Aprovado")
        else:
            saida.append("Reprovado")

    print("Resultado da validacao Poker Test:")
    print(saida)
    print("\n")

def runsGet(chave: list):
    runs = dict()
    runNumber = 1
    bitAnterior = None
    for idx, bit in enumerate(chave):
        if bitAnterior is None:
            runs[runNumber] = {'inicio': idx}

        elif bitAnterior != bit:
            fim = {'fim': idx - 1}
            runs[runNumber].update(fim)

            runNumber += 1
            runs[runNumber] = {'inicio': idx}

        if idx == len(chave) - 1:
            fim = {'fim': idx}
            runs[runNumber].update(fim)

        bitAnterior = bit
            
    return runs
    

def runs(chaves: list):
    tabelaRun = {
        1: (2267, 2733),
        2: (1079, 1421),
        3: (502, 748),
        4: (223, 402),
        5: (90, 223),
        6: (90, 233),
    }
    
    saida = []
    for chave in chaves:
        runs = runsGet(chave)
        
        ehValido = "Aprovado"
        for run in runs:
            inicio = runs[run]['inicio']
            fim = runs[run]['fim']
            
            tamanho = fim - inicio + 1
            tamanho = 6 if tamanho > 6 else tamanho
            
            inicioEsperado, fimEsperado = tabelaRun[tamanho]
            
            if not (inicioEsperado <= inicio <= fim <= fimEsperado):
                ehValido = "Reprovado"
        
        saida.append(ehValido)
                
    print(f"Resultado da validacao Runs Test:")
    print(saida)
    print("\n")

    
def long_run(chaves: list):
    saida = []
    for chave in chaves:
        runs = runsGet(chave)
        
        ehValido = "Aprovado"
        for run in runs:
            inicio = runs[run]['inicio']
            fim = runs[run]['fim']
            
            tamanho = fim - inicio + 1
            
            if tamanho >= 34:
                ehValido = "Reprovado"
                break
        
        saida.append(ehValido)
            
    print("Resultado da validacao Long Run Test:")
    print(saida)
    print("\n")

def lerChaves():
    with open(FILE, "r") as f:
        tempChave = [line for line in f.readlines()]

    chaves = []
    for chave in tempChave:
        hexString = chave.rstrip("\n")[1:-1]
        bits = BitArray(hex=hexString)
        chaves.append(bits)

    return chaves[:-1]

if __name__ == "__main__":
    chaves = lerChaves()
    
    monobit(chaves)
    poker(chaves)
    runs(chaves)
    long_run(chaves)
