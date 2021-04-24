from code import *

token = input('token : ')
## Commande ping
command('!ping', ":ping_pong: Pong ! Je t'ai répondu en `$ping` millisecondes")
## Commandes infos
command('!bot-info', "Le ping du bot est de `$ping` ms !\nJ'ai $commandCount commandes\nJe suis sur $serversCount serveurs\nUtilisateurs : $usersCount\nVersion discord : $version")
command('!user-info', "Ton nom est $username, ton id est $authorID")
command('!test', "$mentioned")
setstatus('!help')
login(token)
