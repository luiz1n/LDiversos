class Gerundios:
    def __init__(self) -> None:
        pass

    def gerundios(self, palavra):
        grnd = ""
        palavra = str(palavra)
        if palavra.__contains__(' '):
            fds = palavra.split(' ')
            for verbo in fds:
                if verbo.endswith('r'):
                    grnd += f'{verbo[:-1:]}ndo '
            return grnd
        else:
            if palavra.endswith('r'):
                grnd += f'{palavra[:-1:]}ndo'
                return grnd