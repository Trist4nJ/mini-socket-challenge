# Mini-Projet Socket : Challenge ROT13

Un petit projet Python basé sur les sockets pour créer un challenge réseau.

- Le **serveur** envoie une chaîne chiffrée avec **ROT13**.
- Le **client** doit la déchiffrer et renvoyer la réponse en **moins de 2 secondes**.
- Si la réponse est correcte, le serveur renvoie un **FLAG**.

Ce challenge est inspiré d’un exercice disponible sur **Root-Me**.  
J’ai voulu le **reproduire côté serveur** pour mieux comprendre comment il fonctionne en interne.

## Fichiers

- `server.py` : code du serveur (écoute, chiffre, vérifie)
- `client.py` : code du client (reçoit, déchiffre, répond)
