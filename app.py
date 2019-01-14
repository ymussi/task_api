from flask import Flask

import tratacpf
from conexoes import conexao
from repositorios import cliente_repositorio

conexao = conexao.Conexao()
sessao = conexao.criar_sessao()

app = Flask('projeto')


@app.route("/api/consultar/<cpf>")
def consultar_cpf(cpf):
    cpfint = cpf
    repositorio = cliente_repositorio.ClienteRepositorio()
    nome_return = repositorio.buscar_nome_cpf(cpfint, sessao)
    return tratacpf.trata_consulta(nome_return, cpfint)


app.run(use_reloader=True)
