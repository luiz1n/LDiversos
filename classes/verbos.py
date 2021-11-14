import random

class Verbos:
    def __init__(self) -> None:

        self.a_verbos = ['amar', 'alar', 'agir', 'abafar', 'abandonar', 'abalar', 'abaixar', 'acender', 'abordar']
        self.b_verbos = ['bater', 'babar', 'burlar', 'balir', 'baldear', 'banir', 'banhar']
        self.c_verbos = ['cair', 'colar', 'cafelar', 'cafifar', 'caçar', 'caçoar', 'calar']
        self.d_verbos = ['dançar', 'doar', 'dadivar', 'declinar', 'declarar', 'daltonizar', 'dandinar']
        self.e_verbos = ['errar', 'ecoar', 'encravar', 'editar', 'eleger', 'elidir', 'eliminar']
        self.f_verbos = ['fabricar', 'falar', 'ferver', 'florar', 'farpar', 'fruir', 'fugir', 'facilitar']
        self.g_verbos = ['gabar', 'galar', 'guiar', 'garrochar', 'guinar', 'guinchar', 'gerar', 'galantear']
        self.h_verbos = ['herdar', 'honrar', 'habilitar', 'habitar', 'hackear', 'haver']
        self.i_verbos = ['ir', 'irritar', 'içar', 'imitar', 'ilhar']
        self.j_verbos = ['jogar', 'jantar', 'jejuar', 'jardar', 'janelar']
        self.k_verbos = ['kickar']
        self.l_verbos = ['lanchar', 'ler', 'lacrar', 'laçar', 'lançar', 'lanhar', 'ligar', 'livrar']
        self.m_verbos = ['matar', 'morrer', 'mascar', 'malear', 'madeixar', 'malhar']
        self.n_verbos = ['nadar', 'ninhar', 'nacionalizar']
        self.o_verbos = ['orar', 'olhar', 'orçar', 'odiar']
        self.p_verbos = ['parar', 'pular', 'por']
        self.q_verbos = ['querer', 'quadrar', 'quinar', 'quicar', 'quitar']
        self.r_verbos = ['rir', 'roer', 'rolar', 'roubar']
        self.s_verbos = ['sair', 'soar', 'surtar']
        self.t_verbos = ['ter', 'transpor', 'trombar',' trombejar', 'topar', 'traduzir']
        self.u_verbos = ['urrar', 'uivar', 'usar', 'usitar', 'ustir', 'usurar', 'usufrir']
        self.v_verbos = ['ver', 'voar', 'vandalizar', 'viuvar', 'viver', 'vedar']
        self.z_verbos = ['zerar', 'zangar', 'zingar', 'zipar', 'zuir', 'zular', 'zelar']

    def sort_verbos(self, letra):
        if letra == 'a':
            return random.choice(self.a_verbos)
        elif letra == 'b':
            return random.choice(self.b_verbos)
        elif letra == 'c':
            return random.choice(self.c_verbos)
        elif letra == 'd':
            return random.choice(self.d_verbos)
        elif letra == 'e':
            return random.choice(self.e_verbos)
        elif letra == 'f':
            return random.choice(self.f_verbos)
        elif letra == 'g':
            return random.choice(self.g_verbos)
        elif letra == 'h':
            return random.choice(self.h_verbos)
        elif letra == 'i':
            return random.choice(self.i_verbos)
        elif letra == 'j':
            return random.choice(self.j_verbos)
        elif letra == 'k':
            return random.choice(self.k_verbos)
        elif letra == 'l':
            return random.choice(self.l_verbos)
        elif letra == 'm':
            return random.choice(self.m_verbos)
        elif letra == 'n':
            return random.choice(self.n_verbos)
        elif letra == 'o':
            return random.choice(self.o_verbos)
        elif letra == 'p':
            return random.choice(self.p_verbos)
        elif letra == 'q':
            return random.choice(self.q_verbos)
        elif letra == 'r':
            return random.choice(self.r_verbos)
        elif letra == 's':
            return random.choice(self.s_verbos)
        elif letra == 't':
            return random.choice(self.t_verbos)
        elif letra == 'u':
            return random.choice(self.u_verbos)
        elif letra == 'v':
            return random.choice(self.v_verbos)
        elif letra == 'z':
            return random.choice(self.z_verbos)
    def verbos(self, letra):
        letra = str(letra)
        if letra.__contains__(' '):
            verbos_ = ''
            p = letra.split(' ')
            for l in p:
                verbos_ += f'{self.sort_verbos(l)} '
            return verbos_
        else:
            return self.sort_verbos(letra)