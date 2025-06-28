import socket
import random
import codecs

# Challenge sur ROT13

# Création du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))  # écoute sur toutes les interfaces, port 12345
server_socket.listen(1)  # 1 client maximum en attente

print("Serveur en écoute sur le port 12345...")

conn, addr = server_socket.accept()
conn.settimeout(2)

chaine = ""
for _ in range(15):
    n = random.randint(65, 120)
    chaine += chr(n)

encrypted_message = codecs.encode(chaine, 'rot_13')

message = f"Renvoyez en moins de 2 secondes le texte en clair : {encrypted_message}"

conn.sendall(message.encode())
while True:
    try:
        data = conn.recv(1024)

        if not data:
            print("[Serveur] Client déconnecté.")
            break

        message = data.decode().strip()

        if message == chaine:
            conn.sendall("FLAG{s0ck3tPyTh0n}".encode())
            break
        else:
            conn.sendall("Mauvaise réponse.".encode())

    except socket.timeout:
        try:
            conn.sendall("Trop lent ! Déconnexion...".encode())
        except BrokenPipeError:
            print("[Serveur] Le client a déjà fermé la connexion.")
        break

    except ConnectionResetError:
        print("[Serveur] Connexion réinitialisée par le client.")
        break

    except Exception as e:
        print(f"[Erreur inattendue] {e}")
        break

conn.close()
print("[Serveur] Connexion fermée.")

