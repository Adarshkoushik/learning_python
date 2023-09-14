class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def start(self):
        print("Starting the car")
    
    def stop(self):
        print("Stopping the car")

class threeseries(BMW):
    def __init__(self,cruisecontrolenabled,make, model, year):
        BMW.__init__(self,make, model, year) 
        self.cruisecontrolenabled=cruisecontrolenabled
    
    def display(self):
        print(self.cruisecontrolenabled)

class fiveseries(BMW):
    def __init__(self,parkassistenabled, make, model, year):
        BMW.__init__(self,make, model, year)
        self.parkassistenabled=parkassistenabled

    def display(self):
        print(self.parkassistenabled)

threeseriesobj=threeseries(True,"BMW","328i",2019)
print(threeseriesobj.cruisecontrolenabled)
print(threeseriesobj.make)
print(threeseriesobj.model)
print(threeseriesobj.year)

threeseriesobj.start()
threeseriesobj.stop()
threeseriesobj.display()

fiveseriesobj=fiveseries(True,"BMW","535d",2021)
fiveseriesobj.display()
