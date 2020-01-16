import os

import discord
from dotenv import load_dotenv

#.env
DISCORD_TOKEN={your-bot-token}
DISCORD_GUILD={your-guild-name}

#substituir pelos actual values

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

class CustomClient(discord.Client):
    
    @client.event
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
    
    async def creatListUsers():
        return []

    async def insertUsers(list,user):
        return list+[user]

    async def getUsers():
        return users

    async def setUser(name,index):
        users[index]=name
        print('Operação efetuada com sucesso')

    async def sameList(list1,list2):
        return list1==list2

    async def e_list(x):
        return isinstance(x,list)

    async def empty_list(list):
        return list==[]

    async def sizeList(list):
        return len(list)

    async def showUsers(list):
        if list==[]:
            raise ValueError('No users found')
        else:
            for i in len(list):
                print('Pessoas inscritas:', i)
    
    counter = 0
    async def addPoints(points,member):
        if message.author == client.user:
            counter += point
            print('Score updated. You now have', points, 'points')
client = CustomClient()   
client.run(token)

#pontos=eval(input("Escreva a quantidade de minutos que visualizou:"))
#async def calcula_total():   
 #   total+=pontos #total=total+pontos
 #   print ('O seu total de pontos é:', pontos)

#m.info (exemplo)->tipo m.add (ou seja qual for o nome da funcionalidade) seguido do número de minutos a adicionar
# e depois uma mention do
# 
#  user que pertence a pontuação a adicionar
#Exemplo m.addMin(50)@Ninja
#mee6->adição de pontos (neste caso por mensagem aleatoriamente(random ou rand))
