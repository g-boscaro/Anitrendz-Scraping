import sqlalchemy as db
import PyMySQL

#Criando o motor que faz a conexão com o BD
engine = db.create_engine('mysql+pymysql://root:1234@localhost:3306/test', echo=True)

#Criando a sessão que se conecta à engine
Session = db.orm.sessionmaker(bind=engine)
session = Session()


Base = db.ext.declarative.declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    password = db.Column(db.String)

    def __repr__(self):
        return f'User {self.name}'

Base.metadata.create_all(engine)

user = User(name="um Fido", password="1234")
session.add(user)

print(user.id)