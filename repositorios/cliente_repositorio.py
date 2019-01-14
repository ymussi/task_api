from queries import cliente_query


class ClienteRepositorio():

    def buscar_nome_cpf(self, cpf_cliente, sessao):
        query_cliente = cliente_query.CpfQuery()
        clientes = query_cliente.listar_cliente_cpf(cpf_cliente, sessao)
        return clientes

