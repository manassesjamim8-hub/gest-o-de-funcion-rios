# "banco de dados" temporario usando dicionario 
funcionarios = {
     "admin":"123"
}
# funcao com def para cadastrar um funcionario
def cadastrar_funcinario():
    print("\n--- CADASTRO DE NOVO FUNCIONÁRIO ---")
    novo_usuario = input('escolha um nome de usuario: ')

    #verifica se esse usuario ja esta cadastrado no sistema
    if novo_usuario in funcionarios:
        print("Erro: Este usuário já está cadastrado!")
    else:
        nova_senha = input('Crie uma nova senha')

        funcionarios[novo_usuario] = nova_senha
        print('PARABENS: cadastro do novo funcionario criado com sucesso')

cadastrar_funcinario()
print(f'sistema atualizado com sucesso {funcionarios}')