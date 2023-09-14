class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def start(self):
        print("Starting the car")
        
class threeseries(BMW):
    def __init__(self,cruisecontrolenabled,make, model, year):
        BMW.__init__(self,make, model, year) 
        self.cruisecontrolenabled=cruisecontrolenabled
    
    def display(self):
        print(self.cruisecontrolenabled)
        
    #Overriding is done here
    def start(self):
        print("Button start")
        

class fiveseries(BMW):
    def __init__(self,parkassistenabled, make, model, year):
        BMW.__init__(self,make, model, year)
        self.parkassistenabled=parkassistenabled
        
threeseriesobj=threeseries(True,"BMW","328i",2019)
print(threeseriesobj.cruisecontrolenabled)
print(threeseriesobj.make)
print(threeseriesobj.model)
print(threeseriesobj.year)

threeseriesobj.start()
threeseriesobj.display()
