# Can you change the self-parameter inside a class to something else (say “sayanjit”)? Trychanging self to “slf” or “sayanjit” and see the effects.

from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(sayanjit, fro, to):
        print(f"Ticket is booked in train no: {sayanjit.trainNo} from {fro} to {to}") 

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time") 

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(300, 5000)}")  


t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")