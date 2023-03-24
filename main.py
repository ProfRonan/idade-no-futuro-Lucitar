ano_atual = input()
idade = input()
ano_futuro = input()

idade_nova = (int(ano_futuro) - int(ano_atual)) + int(idade)

print("Fulano, no ano de " + ano_futuro + " você terá " + str(idade_nova) + " anos")