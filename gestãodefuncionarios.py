print("crie um login")

usuario = input('digite um usuário: ')
senha = input('digite uma senha: ')

while True:
    print('ENTRE NA SUA CONTA: ')
    usuario1 = input('DIGITE O SEU USUÁRIO: ') 
    senha1 = input ("DIGITE SUA SENHA: ")
    if (usuario1 == usuario) and (senha1 == senha) :
        print(f"LOGIN FEITO COM SUCESSO, SEJA BEM VINDO {usuario}!!")
        break
    else:
        print("SENHA OU USUARIO INCORRETO, TENTE NOVAMENTE")