from sqlalchemy import Column, Integer, String, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from conexoes import conexao

conexao = conexao.Conexao()
engine = conexao.conectar()

Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(40), nullable=False)
    cpf = Column(VARCHAR(11), nullable=False)

    def __repr__(self):
        return '%s' % (self.nome)


Base.metadata.create_all(engine)
