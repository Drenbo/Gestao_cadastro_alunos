import json
import os

def criar_banco():
    if not os.path.exists('banco.json'): 
        modelo = {"dados": []}
        with open('banco.json', 'w') as file:
            json.dump(modelo, file, indent=5)
        print("Banco de dados criado com sucesso!")
    else:
        print("Banco de dados já existe.")

def media_aluno(x, y, z):
    x = int(x)
    y = int(y)
    z = int(z)
    return (x + y + z) / 3

criar_banco()

while True:
    print('O que deseja realizar no sistema:\n 1 - Cadastrar\n 2 - Visualizar Alunos\n 3 - Visualizar Aluno\n 4 - Sair')
    escolha = int(input('Serviço solicitado: '))
    
    if escolha == 1:
        nome = input('Qual o nome do aluno? ')
        idade = input('Qual a idade do aluno? ')
        nota_Mat = input('Qual a nota em Matemática? ')
        nota_Cie = input('Qual a nota em Ciências? ')
        nota_His = input('Qual a nota em História? ')

        alunos = {
            "nome": nome,
            "idade": idade,
            "notas": [nota_Mat, nota_Cie, nota_His],
            "media": media_aluno(nota_Mat, nota_Cie, nota_His)
        }
        
        with open('banco.json', 'r') as file:
            try:
                dicionario = json.load(file) 
            except json.JSONDecodeError:
                dicionario = {"dados": []}

        dicionario['dados'].append(alunos)
        dicionario['dados'] = sorted(dicionario['dados'], key=lambda aluno: aluno['media'], reverse=True)

        with open('banco.json', 'w') as file:
            json.dump(dicionario, file, indent=5)

    elif escolha == 2:
        with open('banco.json', 'r') as file:
            try:
                dicionario = json.load(file)
            except json.JSONDecodeError:
                dicionario = {"dados": []}
        for aluno in dicionario['dados']:
            print(aluno)

    elif escolha == 3:
        escolha_aluno = input('Qual o nome do aluno em questão? ')
        with open('banco.json', 'r') as file:
            try:
                dicionario = json.load(file)
            except json.JSONDecodeError:
                dicionario = {"dados": []}
        encontrado = False
        for aluno in dicionario['dados']:
            if aluno['nome'] == escolha_aluno:
                print(aluno)
                encontrado = True
                break
        if not encontrado:
            print('Aluno não encontrado.')

    elif escolha == 4:
        print('Saindo do programa')
        break

    else:
        print('Opção inválida. Tente novamente.')
