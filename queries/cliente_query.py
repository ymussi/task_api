from dominios.db import Cliente


class CpfQuery():

    def listar_cliente_cpf(self, cpf_Cliente, sessao):
        clientes = sessao.query(Cliente).filter(Cliente.cpf == cpf_Cliente).all()
        return clientes

