from sqlalchemy import *
from sqlalchemy.orm import *

Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    
    #atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    
    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"
    
class Address(Base):
    __tablename__ = "address"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(30), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    
    user = relationship("User", back_populates="address")

    def __repr__(self):
         return f"Address(id={self.id}, email_address={self.email_address})"
     

print(User.__tablename__)
print(Address.__tablename__)


#conexao com o banco de dados
engine = create_engine("sqlite://")

#agora que eu defini a engine (a conexão com o banco), eu preciso efetuar as modificações, pegar os 
# objetos, as classes que eu criei, mepear e persistir elas no banco de dados

#criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# Agora eu preciso definir um 'inspetor', que é o cara que vai buscar dentro da minha engine as informações
# que eu preciso

#Investiga o esquema do banco de dados
insp = inspect(engine)
print(insp.has_table("user_account"))
print(insp.get_table_names())


# Agora eu quero criar dados e persistí-los dentro do SQlITE
with Session(engine) as session:
    nathan = User(
        name='Nathan',
        fullname='Nathan Fonseca da Silva',
        address=[Address(email_address='email@email.com')]
    )
    
    sandy = User(
        name='sandy',
        fullname='Sandy cardoso',
        address=[Address(email_address='sandy@email.org'),
                 Address(email_address='sandycardoso@sandy.com'),]
    )
    
    patrick = User(name='patrick', fullname='Patrick Cardoso')
    
    
    #Enviando para o BD (persistência de dados)
    session.add_all([nathan, sandy, patrick])
    
    session.commit()


# FAZENDO CONSULTAS
statement = select(User).where(User.name.in_(['Nathan', 'sandy']))
# print(statement)
for user in session.scalars(statement):
    print(user)
    

statement_address = select(Address).where(Address.user_id.in_([2]))
for address in session.scalars(statement_address):
    print(address)
    
    
# FUNÇÕES ORDER BY, JOIN E COUNT
order = select(User).order_by(User.fullname.desc())
print(order)

for result in session.scalars(order):
    print(result)
    
    
# JOIN
join = select(User.fullname, Address.email_address).join_from(Address, User)
# for result in session.scalars(join):
#     print(result)
    
connection = engine.connect()
results = connection.execute(join).fetchall()
print("Executando statement a partir da connection")
for result in results:
    print(result)
    
    
#COUNT
count = select(func.count('*')).select_from(User)
print(count)
for result in session.scalars(count):
    print(result)