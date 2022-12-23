import email

nome = input(
    'Digite seu nome:'
)

sobrenm = input(
    'Digite seu sobrenome:'
)

idade = input(
    'Digite sua idade:'
)

email = email(input(
    'Digite seu e-mail:'
))

senha = input(
    'Digite sua senha:'
)

confr = input(
    'Confirme sua senha:'
)

print(
    f'Olá {nome} {sobrenm}, Bem vindo ao nosso sistema! mandaremos um código no endereço de e-mail: {email}'
)