from socket import *
import threading
import json
import random

def handleClient(clientSocket):
    while True:
        try:
            #  JSON fra client
            requestJson = clientSocket.recv(1024).decode() #giver lidt problemer ved "no" i Do you want to keep going? (yes/no):
            request = json.loads(requestJson)

            # Håndtering af kommandoer og tal
            command = request.get("command")
            number1 = request.get("number1")
            number2 = request.get("number2")

            # Håndterer kommandoer og tal og sender svar tilbage som JSON!
            if command == "Random":
                result = random.randint(number1, number2)
            elif command == "Add":
                result = number1 + number2
            elif command == "Subtract":
                result = number1 - number2
            else:
                result = "Unknown command"

            response = json.dumps({"result": result})
            clientSocket.send(response.encode())

        except (json.JSONDecodeError, ValueError):

            # Håndterer fejl 
            response = json.dumps({"error": "Invalid request use: 'command;number1;number2'"})
            clientSocket.send(response.encode())

# Opsætning af serverens socket og port
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The Server is ready...!')

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket,)).start()
