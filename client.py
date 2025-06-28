import socket
import codecs

HOST = 'localhost'
PORT = 12345

# Connexion au serveur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

message = client_socket.recv(1024).decode()
print("[Serveur] :", message)


try:
    encrypted_text = message.split(":")[1].strip()
except IndexError:
    print("Format de message inattendu.")
    client_socket.close()
    exit()

decrypted = codecs.decode(encrypted_text, 'rot_13')
print("[Client] Chaîne déchiffrée :", decrypted)

client_socket.sendall(decrypted.encode())

try:
    response = client_socket.recv(1024)
    print("[Serveur] :", response.decode())
except socket.timeout:
    print("[Erreur] Timeout : pas de réponse du serveur.")

