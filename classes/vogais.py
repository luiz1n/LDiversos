class Vogais:

    def __init__(self) -> None:
        pass

    def vogais( self, palavra ):
        palavra_com_vogal = ""
        for caractere in palavra:
            if caractere == 'a' or caractere == 'e' or caractere == 'i' or caractere == 'o' or caractere == 'u':
                palavra_com_vogal += caractere
        return palavra_com_vogal