import os
os.system("cls")

print("Cadastro de Turmas\n")

turma = [
    [0, ["#####", "#####"]],
    [0, ["#####", "#####"]]
]

controlador = "0"
controlador2 = 0
i = 0
j = 0
k = 0
aluno = 1
codturma = 1

while controlador != "1":

    # Controle para cadastrar a segunda turma
    if i == 1:
        j = 0
        k = 0

    print("Informe o codigo da " + str(codturma) + "ª turma: ")
    turma[i][j] = int(input())

    # Controle para cadastrar os alunos
    while controlador2 <= 1:
        j = 1
        turma[i][j][k] = input("Informe o nome do " +
                               str(aluno) + "º" + " aluno: ")

        # Condição para limitar o quadrasto de apenas 2 estudantes
        if aluno >= 2:
            break
        else:
            controlador2 = int(
                input("Gostaria de cadastrar mais um aluno? [1] Sim | [2] Não"))
            if controlador2 == 1:
                aluno += 1
                k += 1
            else:
                codturma = 2
                break
    
    print("\tCadastro Concluído!")

    # Controle para sair do programa caso as duas turmas já estejam cadastradas
    if codturma == 2:
        break
    else:
        controlador = input(
            "\tDigite: [0] Continuar no programa | [1] Sair do programa")
        controlador2 = 0
        aluno = 1
        codturma += 1
        i += 1

os.system("cls")
print("\n\tTurmas Cadastradas: \n")

for linha, coluna in turma:
    print("Turma: " + str(linha) + "\nAlunos: " + str(coluna) + "\n")
