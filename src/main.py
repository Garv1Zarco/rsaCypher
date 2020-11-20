from modules import rsaEntity
from modules import UserEntity


rsa = rsaEntity.Rsa()
rsa.key_gen()
sender = UserEntity.User()
reciever = UserEntity.User()
m = "hola"
c = sender.cypher(rsa, m)
m = reciever.decypher(rsa, c)
print(m)