import os

ARQUIVO_BLACKLIST = "blacklist.txt"

def carregar_blacklist():
    caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), ARQUIVO_BLACKLIST)
    try:
        with open(caminho, "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def salvar_blacklist(lista_ips):
    caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)),ARQUIVO_BLACKLIST)
    print(f"DEBUG: Tentando salvar em: {caminho}")
    with open(caminho, "w") as f:
        for ip in lista_ips:
            f.write( ip + "\n")

def main():
    tentativas_falhadas = {}
    lista_ips_bloqueados = carregar_blacklist()
    while True:
        ip = input("Digite seu ip: ")

        if ip in lista_ips_bloqueados:
            print(f"ACESSO NEGADO! IP {ip} esta na blacklist.")
            continue
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == "admin" and senha == "123":
            print(f"Login bem-sucedido! Bem-vindo {usuario}.")
            tentativas_falhadas[ip] = 0
            break
        else:
            print("Usuário ou senha incorretos.")

            #conta +1 erro para esse IP
            tentativas_falhadas[ip] = tentativas_falhadas.get(ip, 0) + 1
            print(f"Tentativa {tentativas_falhadas[ip]} de 3 para o IP {ip}")

            if tentativas_falhadas[ip] >= 3:
                print(f"IP {ip} BLOQUEADO por excesso de tentativas!")
                lista_ips_bloqueados.append(ip)
                salvar_blacklist(lista_ips_bloqueados)

if __name__ == "__main__":
    main()

