from code import *

token = 'VOTRE_TOKEN_ICI'

## Exemple commande ping :
command('!ping', ":ping_pong: Pong ! Je t'ai répondu en `$ping` millisecondes")

## Exemple commandes infos
command('!bot-info', "Le ping du bot est de `$ping` ms !\nJ'ai $commandCount commandes\nJe suis sur $serversCount serveurs\nUtilisateurs : $usersCount\nVersion discord : $version")
command('!user-info', "Ton nom est $username, ton id est $authorID")

## Change le status :
setstatus('!help')

## Connexion au bot
login(token)
