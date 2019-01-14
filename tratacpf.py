def trata_cpf(cpf, sessao):
    if len(str(cpf)) == 11:
        print('CPF Válido.')
        return True
    else:
        print('CPF Inválido.')
        return False


def trata_consulta(nome_return, cpfint):
    try:
        return f"Consulta Realizada!<br>Seu nome é : {nome_return[0]}\
                <br>Seu CPF é : {cpfint}"
    except:
        return 'CPF Inválido.'
