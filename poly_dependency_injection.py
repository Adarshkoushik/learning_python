class Flight:
    def __init__(self,engine):
        self.engine=engine
    
    def startEngine(self):
        self.engine.start()

class AirBus:
    def start(self):
        print("Airbus Engine Started")

class Boing:
    def start(self):
        print("BoingEngine started")

ae=AirBus()
f1=Flight(ae)
f1.startEngine()

be=Boing()
f2=Flight(be)
f2.startEngine()