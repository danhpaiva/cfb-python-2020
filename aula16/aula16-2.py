import os
os.system("cls")

print("Cadastro de Turmas")

turma = [
    [1, ["Aluno", "Aluno2"]],
    [2, ["Aluno", "Alunos2"]]
]

controlador = "0"
controlador2 = 0
i = 0
j = 0
k = 0
aluno = 1
codturma = 1

while controlador != "1":

    # Controle para cadastrar a segunda
    if i == 1:
        j = 0
        k = 0

    print("Informe o codigo da " + str(codturma) + "ª turma: ")
    turma[i][j] = int(input())

    while controlador2 <= 1:
        j = 1
        turma[i][j][k] = input("Informe o nome do " +
                               str(aluno) + "º" + " aluno: ")
        aluno += 1
        controlador2 += 1
        k += 1

    if codturma == 2:
        break
    else:
        controlador = input("[0] Continuar | [1] Sair ")
        controlador2 = 0
        aluno = 1
        codturma += 1
        i += 1

print("\n\tTurmas Cadastradas: \n")

for linha, coluna in turma:
    print("Turma: " + str(linha) + " Alunos: " + str(coluna))
