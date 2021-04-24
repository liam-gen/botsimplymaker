## /!\ NE PAS TOUCHER NI SUPPRIMER CE FICHIER /!\ ##

import discord
from replit import db
client = discord.Client()

commands = {}



@client.event
async def on_message(message, *member: discord.User):
    if message.content.split(" ")[0] in commands.keys():
        code = commands[message.content.split(" ")[0]]
        
        latency = client.latency * 1000
        executecode = code.replace('$channelID', str(message.channel.id))
        pingreplace = executecode.replace('$ping', str(round(latency)))
        serverreplace = pingreplace.replace('$serversCount', str(len(client.guilds)))
        authorreplace = serverreplace.replace('$authorID', str(message.author.id))
        usernamereplace = authorreplace.replace('$username', str(message.author))
        commandreplace = usernamereplace.replace('$commandCount', str(len(commands)))
        usersreplace = commandreplace.replace('$usersCount', str(len(client.users)))
        versionreplace = usersreplace.replace('$version', str(discord.__version__))
        await message.channel.send(versionreplace)
def command(name, code):
    commands[name] = code

def setstatus(name):
    db['status'] = name


@client.event
async def on_ready():
    status = db['status']
    print(f"Connexion au bot {client.user.name}")
    print('----------')
    print(f'Changement du status pour : Joue a {status}')
    print('----------')
    await client.change_presence(activity=discord.Game(name=status))

def login(token):
    client.run(token)
