# Mini Socket Project: ROT13 Challenge

A small Python project using sockets to create a simple network challenge.

- The **server** sends a string encrypted with **ROT13**.
- The **client** must decrypt it and send the original string back **within 2 seconds**.
- If the response is correct, the server returns a **FLAG**.

This challenge is inspired by an exercise available on **Root-Me**.  
I wanted to **rebuild it on the server side** to better understand how it works internally.

## Files

- `server.py`: server code (listens, encrypts, verifies)
- `client.py`: client code (receives, decrypts, responds)
