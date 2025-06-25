import json
import os
class Memory:
    def __init__(self):
        self.memory = []
    def save(self, talk: dict) -> dict:
        self.memory.append(talk ) if type(talk) is dict else print("Can't save in memory") 
    def lastTalk(self):
        return self.memory[:-2:-1]
    def delete(self):
        if len(self.memory) > 100:
            self.memory = []
    def writeInFile(self, cmd: str, res: str):
        with open("memory.txt", "a") as remember:
            content = f"You: {cmd}\nBot: {res}\n"
            remember.write(content) 
    def __str__(self):
        return "\n".join(str([i for i in self.memory]))
    