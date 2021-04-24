# Bot Simply Maker

---

**Important : Veuillez ne pas toucher au fichier `code.py` pour éviter tout problème**

---

Serveur suport : [Clique ici](https://discord.gg/)


A savoir :

- Nous ne sommes en aucun cas responsable de vos actes vis a vis de votre robot
- Installer [Python](https://python.org)

---

### Créer votre premier bot c'est simple avec Bot Simply Maker !

#### Voici comment faire : 

> 1 - [Télécharger le dosier](https://github.com/liamgen/botsimplymaker)

> 2 - Créer importer le module : `from code import *`

> 3 - Créations de premieres commandes :

```
from code import *
token = 'VOTRE_TOKEN_ICI'
```

Connecter le bot :

```
login(token)
```

Créer une commande :

```
command('command_name', 'code')
```

### Exemple :

```
from code import *

token = 'VOTRE_TOKEN_ICI'

command('!ping', ':ping_pong: Pong ! Je t'ai répondu en `$ping` millisecondes')
command('!bot-info', 'Mon ping est de `$ping` ms!\nJ'ai $commandCount commandes\nJe suis sur $serversCount serveurs\nUtilisateurs : $usersCount\nVersion discord : $version')

login(token)
```

Voici ce que le bot répondera :
 
<img src="https://skyris.liamgen.repl.co/screen.png">

Vous pouvez aussi définir le status avec `setstatus('!help')`
