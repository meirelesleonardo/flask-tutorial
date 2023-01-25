import pyodbc 
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from decouple import config



# cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
#                       "Server=server_name;"
#                       "Database=db_name;"
#                       "Trusted_Connection=yes;")


# cursor = cnxn.cursor()
# cursor.execute('SELECT * FROM Table')

# for row in cursor:
#     print('row = %r' % (row,))

Base = declarative_base()

class User(Base):
    __tablename__='users' # obrigatório

    id = Column(Integer, primary_key=True)
    nome = Column(String)

def conectar_com_banco():
    server = config("HOST_BD_SQLSERVER")
    database = config("DATABASE_BD_SQLSERVER") 
    username = config("USER_BD_SQLSERVER") 
    password = config("PASSWORD_BD_SQLSERVER") 
    
    # cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

    driver = 'ODBC+DRIVER+17+for+SQL+Server'
    engine_stmt = ("mssql+pyodbc://%s:%s@%s/%s?driver=%s" % (username, password, server, database, driver ))
    engine = create_engine(engine_stmt, echo=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    user = User(nome='Meireles')

    session.add(user)
    session.commit()

    query_agentes = session.query(User)
    
    for agente in query_agentes:
        print(agente.nome)
    #engine = create_engine('mssql+pyodbc://' + server + '/' + database + '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')

    # cur=cnxn.cursor()
    # return(cur)

cursor=conectar_com_banco()
# cursor.execute("SELECT @@version;") 
# row = cursor.fetchone() 
# print(row)