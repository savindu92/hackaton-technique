class Robot:
    def __init__(self, position, battery, max_battery, capacity):
        self.position = position
        self.battery = battery
        self.max_battery = max_battery
        self.capacity = capacity
    
    def move(self, destination):
        # code pour déplacer le robot vers une nouvelle destination
        pass
    
    def charge(self, duration):
        # code pour recharger la batterie du robot
        pass
    
    def unload(self, warehouse):
        # code pour décharger la marchandise dans l'entrepôt
        pass
    
    def load(self, warehouse, item):
        # code pour charger la marchandise dans le robot
        pass
    
    def bid(self, task, price):
        # code pour faire une offre sur une tâche
        pass
    
    def complete_task(self, task):
        # code pour accomplir une tâche
        pass
