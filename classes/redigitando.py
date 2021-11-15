class Redigitando:
    def __init__(self) -> None:
        pass

    def redigitar(self, palavra):
        palavra = str(palavra)
        if palavra.__contains__('a'):
            palavra = palavra.replace('a', '4')
        if palavra.__contains__('e'):
            palavra = palavra.replace('e', '3')
        if palavra.__contains__('i'):
            palavra = palavra.replace('i', '1')
        if palavra.__contains__('o'):
            palavra = palavra.replace('o', '0')
        return palavra