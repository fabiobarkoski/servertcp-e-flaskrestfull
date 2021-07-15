from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# conectando ao banco de dados
engine = create_engine('sqlite:///users.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

# criando tabela de usuários


class Users(Base):
    """
    Classe da Tabela Users
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), index=True, unique=True)
    password = Column(String(50))

# função para exibir usuário e senha
    def __repr__(self):
        return f'Usuário: {self.username} Senha: {self.password}'

# função para salvar as alterações no banco de dados
    def commit(self):
        db_session.add(self)
        db_session.commit()

# criando tabela de produtos


class Product(Base):
    """
    Classe da Tabela Product
    """
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True)
    type = Column(String(50))
    amount = Column(Integer)

    def __repr__(self):
        return f'Produto:{self.name} Tipo:{self.type} Quantidade:{self.amount}'

    def commit(self):
        db_session.add(self)
        db_session.commit()
# função para deletar o produto selecionado

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
