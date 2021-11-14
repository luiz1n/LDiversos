from g_python.gextension import Extension
from g_python.hdirection import Direction
from g_python.hpacket import HPacket

from classes.vogais import Vogais
from classes.consoantes import Consoantes
from classes.gerundios import Gerundios
from classes.verbos import Verbos

import json

vogais = Vogais()
consoantes = Consoantes()
gerundios = Gerundios()
verbos = Verbos()

def pegar( chave ):
    carregar = json.loads(open('configuracao.json', 'r').read())
    valor = carregar[str(chave).upper()]
    return valor

HEADERS_CUSTOMIZAVEIS = pegar('headers_customizaveis')
HEADERS_CUSTOMIZAVEIS = True if HEADERS_CUSTOMIZAVEIS.lower() == "sim" else False
AUTHOR = "Luiz1n"
PREFIXO = ":"

INICIADO = False
EVENTO = "?"

extension_info  = {
    "title": "LDiversos",
    "description": "Scripts para diversos",
    "author": AUTHOR,
    "version": "1.0"
}

extension = Extension(extension_info, args=['-p', '9092'], silent=True)
extension.start()

print(f'''Script Iniciado ~ Coded by {AUTHOR}''')

headers = {
    "standard": {
        "Outgoing": {
            "RoomUserTalk": "Chat"
        },
        "Incoming": {
            "RoomUserTalk": "Chat",
            "RoomUsers": "Users"
        }
    },

    "custom": {
        "Outgoing": {
            "RoomUserTalk": 1314
        },
        "Incoming": {
            "RoomUserTalk": 1446,
            "RoomUsers": 374
        }
    }
}

def pegar_header( name, outgoing = False ):
    return headers['custom' if HEADERS_CUSTOMIZAVEIS else 'standard']['Outgoing' if outgoing else 'Incoming'][name]

def enviar_aviso (aviso):
    extension.send_to_client(HPacket(pegar_header("RoomUserTalk"), 0, f'LDiversos ~ {aviso}', 0, 34, 0, -1))

def enviar_mensagem (mensagem, bubble):
    extension.send_to_server(HPacket(pegar_header("RoomUserTalk", True), mensagem, bubble, 0))

def parar():
    global INICIADO
    if INICIADO:
        INICIADO = False

def interceptar_fala( message ):

    global INICIADO, EVENTO

    packet = message.packet
    (message_, bubble, _,) = packet.read('sii')
    message.is_blocked = True
    message_ = str(message_).lower()

    if not message_.startswith(PREFIXO):
        message.is_blocked = False
        
        if INICIADO:
            message.is_blocked = True
            if EVENTO == 'Vogais':
                v = vogais.vogais(message_)
                enviar_mensagem(v, bubble)

            elif EVENTO == 'Consoantes':
                c = consoantes.consoantes(message_)
                enviar_mensagem(c, bubble)

            elif EVENTO == 'Gerundios':
                g = gerundios.gerundios(message_)
                enviar_mensagem(g, bubble)
            
            elif EVENTO == "Verbos":
                v = verbos.verbos(message_)
                enviar_mensagem(v, bubble)


    if message_.startswith(PREFIXO):
        comando = message_.replace(PREFIXO, "")

        if comando == "iniciar":
            parar()
            enviar_aviso("Informe um evento. Use :lista para obter a lista de eventos.")
            return

        if comando == "parar":
            if INICIADO:
                parar()
            else:
                enviar_aviso("O Script já está parado.")
            return

        if comando.startswith('iniciar '):
            evento = comando.replace('iniciar ', '')     

            if evento == "vogais":
                EVENTO = "Vogais"
                INICIADO = True

            elif evento == "consoantes":
                EVENTO = "Consoantes"
                INICIADO = True

            elif evento == "gerundios":
                EVENTO = "Gerundios"
                INICIADO = True
            
            elif evento == "verbos":
                EVENTO = "Verbos"
                INICIADO = True
            
            else:
                enviar_aviso("Evento não reconhecido. Use :lista para ter a lista de eventos disponíveis.")
                return

            enviar_aviso(f"Script iniciado com o evento: {EVENTO}")


extension.intercept( Direction.TO_SERVER, interceptar_fala, pegar_header('RoomUserTalk', True))