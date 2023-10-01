

from socket import *
import json

serverIp = '127.0.0.1'  # localhost
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIp, serverPort))

print("Connected to the server: " + serverIp)

while True:
    command = input("Command (Generate 'Random' Number, 'Add' func or 'Subtract' func): ")
    number1 = input("Number 1: ")
    number2 = input("Number 2: ")

    # Oprettelse af JSON 
    request = json.dumps({"command": command, "number1": int(number1), "number2": int(number2)})
    clientSocket.send(request.encode())
    print ("Sent to server: ", request)
    # Modtag serverens svar
    responseJson = clientSocket.recv(1024).decode()
    response = json.loads(responseJson)
    print("Server", serverIp,": " ,response.get("result"))

    another = input("Do you want to keep going? (yes/no): ")
    if another.lower() != 'yes':
        break

clientSocket.close()
