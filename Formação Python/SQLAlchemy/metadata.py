from sqlalchemy import *
from sqlalchemy.orm import *

engine = create_engine('sqlite://')

# Objeto associado aos metadados do meu bd
metadata_obj = MetaData()
user = Table(
    #Nome da tabela
    'user', 
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('email_address', String(60)),
    Column('nickname', String(50), nullable=False)
)

user_prefs = Table(
    'user_prefs', metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100))
)

# Exibir nome das tabelas para verificar se elas foram incluídas no bd
for tab in metadata_obj.sorted_tables:
    print(tab)
    
# Criando as tabelas no banco de dados
metadata_obj.create_all(engine)

metadata_bd_obj = MetaData()
financial_info = Table(
    'financial_info', metadata_bd_obj,
    Column('id', Integer, primary_key=True),
    Column('value', String(100), nullable=False)
)


#Ver informações das tabelas
#Ver quem é a PK
print(financial_info.primary_key)


#Executando statement
with engine.connect() as conn:
    print('Executando um statement no Banco')
    sqlInsert = text('insert into user (user_id, email_address, nickname) values (1, "email@email", "tien")')
    conn.execute(sqlInsert)
    sql = text('select * from user')
    result = conn.execute(sql)
    
    #printando resultado
    for row in result:
        print(row)
