class Computer:
    def __init__(self, ram, memory, processor):
        self.ram = ram
        self.memory = memory
        self.processor = processor

    def getspecs(self):
        print('Please enter the details')
        self.ram = input('Enter Ram Size')
        self.memory = input('Memory size')
        self.processor = input('Enter processor')

    def displayspecs(self):
        print('Here are the specs of the computer')
        print(' Ram size is: ' + self.ram + ' Memory size is: ' + self.memory + ' processor is: ' + self.processor)


class Desktop(Computer):
    def __init__(self, casecolor):
        self.casecolor = casecolor

    def get_case_details(self):
        self.casecolor = input('Enter case color')

    def put_case_details(self):
        print('case color is: ' + self.casecolor)


class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight

    def getweight(self):
        self.weight = input('Enter weight')

    def displayweight(self):
        print('weight is: ' + self.weight)


comp = Laptop('');
comp.getspecs()
comp.getweight()
comp.displayspecs()
comp.displayweight()
