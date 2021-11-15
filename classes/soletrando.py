class Soletrando:
    def __init__(self) -> None:
        pass

    def soletrar(self, palavra):
        palavra = str(palavra)
        soletr = ""
        for c in palavra:
            soletr += f'{c} '
        return soletr