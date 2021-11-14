from g_python.gextension import Extension
from g_python.hdirection import Direction
from g_python.hpacket import HPacket
from g_python.hparsers import HEntity, HEntityType

from classes.vogais import Vogais
import json

vogais = Vogais()


def pegar( chave ):
    carregar = json.loads(open('configuracao.json', 'r').read())
    valor = carregar[str(chave).upper()]
    return valor

HEADERS_CUSTOMIZAVEIS = pegar('headers_customizaveis')
HEADERS_CUSTOMIZAVEIS = True if HEADERS_CUSTOMIZAVEIS.lower() == "sim" else False
AUTHOR = "Luiz1n"
PREFIXO = ":"

USERS = {}
INICIADO = False

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

def enviar_mensagem (mensagem):
    extension.send_to_server(HPacket(pegar_header("RoomUserTalk", True), mensagem, 1, 0))

def pegar_usuarios( message ):
    packet = message.packet
    for user in HEntity.parse(packet):
        if user.name not in USERS:
            USERS[user.name] = user.index

def interceptar_fala( message ):
    packet = message.packet
    (index, message_, _, bubble, _, _,) = packet.read('isiiii')
    message.is_blocked = True
    message_ = str(message_).lower()

    if not message_.startswith(PREFIXO):
        message.is_blocked = False
        return
    
    if message_.startswith(PREFIXO):
        comando = message_.replace(PREFIXO, "")

        if comando == "iniciar":
            enviar_aviso("Informe um evento. Use :lista para obter a lista de eventos.")
            return

        if comando.startswith('iniciar '):
            evento = comando.replace('iniciar ', '')        
            if evento == "vogais":
                vogais.vogais()


extension.intercept( Direction.TO_CLIENT, pegar_usuarios, pegar_header('RoomUsers') )
extension.intercept( Direction.TO_CLIENT, interceptar_fala, pegar_header('RoomUserTalk') )