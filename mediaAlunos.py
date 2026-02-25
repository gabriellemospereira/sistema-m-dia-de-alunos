nome = str(input('Qual o nome do aluno: '))
nota1 = float(input('Digite a nota do {}: '.format(nome)))
nota2 = float(input('Digite a segunda nota do {}: '.format(nome)))
média = (nota1 + nota2) / 2

if média < 5.0:
    print('*' * 50)
    print('A nota do aluno(a) {} foi {:1f}'.format(nome, média))
    print('REPROVADO')
    print('*' * 50)
elif média < 7.0:
    print('*' * 50)
    print('A nota do aluno(a) {} foi {:.1f}'.format(nome, média))
    print('RECUPERAÇÃO')
    print('*' * 50)
else: 
    print('*' * 50)
    print(' A nota do aluno(a) {} foi {:.1f}'.format(nome, média))
    print(' APROVADO!!!')
    print('*' * 50)