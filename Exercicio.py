alunos_notas = {'Pedro': 8.0, 'Maria': 7.3, 'Jose': 10.0, 'Ana': 10.0}

with open ('./Notas.txt', 'w') as texto:
    for aluno, nota in alunos_notas.items():
        texto.write(f'{aluno}: {nota}\n')