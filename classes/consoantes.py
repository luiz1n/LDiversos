class Consoantes:

    def __init__(self) -> None:
        pass
    
    def consoantes( self, palavra ):
        palavra_com_consoantes = ""
        p = str(palavra)
        for caractere in palavra:
            if ( caractere == 'b' or (
                caractere == 'c'
                or caractere == 'd'
                or caractere == 'f'
                or caractere == 'g'
                or caractere == 'h'
                or caractere == 'j'
                or caractere == 'k'
                or caractere == 'l'
                or caractere == 'm'
                or caractere == 'n'
                or caractere == 'p'
                or caractere == 'q'
                or caractere == 'r'
                or caractere == 's'
                or caractere == 't'
                or caractere == 'v'
                or caractere == 'w'
                or caractere == 'y'
                or caractere == 'z'
            ) ):
                palavra_com_consoantes += caractere
        return palavra_com_consoantes