# Importação para limpar a tela
import os

# Exibe menu
def exibe_menu():
    print('\n')
    print('1 - Ler dados')
    print('2 - Gravar dados de ferramenta nova')
    print('0 - Encerrar programa')

# Função para gravar novo dado no arquivo
def gravar_arquivo(ferramenta, usuario, adicionais, dados):
    novo_dado = f'\n\n{"-"*30}\nNome: {usuario}\nFerramenta: {ferramenta}\nAdicional: {adicionais}'
    with open('arquivo.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(novo_dado)

# Função para ler dados do arquivo
def ler_arquivos():
    try:
        with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
            dados = arquivo.read()
            return dados
    except FileNotFoundError:
        return None

# Programa principal
if __name__ == '__main__':
    while True:
        dados = ler_arquivos() or ''
        print(dados)
        exibe_menu()
        opcao = input('Opção desejada: ')
        os.system('cls')  # Limpa a tela (funciona no Windows)
        
        if opcao == '1':
            print(f'\n{dados}\n')
        elif opcao == '2':
            print('CADASTRAR NOVO MATERIAL\n')
            novo_usuario = input('Informe o nome do novo usuário: ')
            nova_ferramenta = input('Informe a nova ferramenta: ')
            novo_adicional = input('Informe se há alguma observação ou dados adicionais: ')
            gravar_arquivo(nova_ferramenta, novo_usuario, novo_adicional, dados)
        elif opcao == '0':
            print('Programa encerrado com sucesso!')
            break
        else:
            print('Opção inválida!')

            