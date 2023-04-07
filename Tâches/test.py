import tache
from tache import Task, AuctionTask, TaskGenerator
from typing import List

class Robot:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.tasks = []
    
    def add_task(self, task: Task):
        if isinstance(task, AuctionTask):
            return
        
        if task.reward > self.capacity:
            return
        
        self.tasks.append(task)
        self.capacity -= task.reward
    
    def __repr__(self):
        return f"Robot({self.capacity}, {self.tasks})"
        

def allocate_tasks(robots: List[Robot], tasks: List[Task]):
    for task in tasks:
        # trier les robots en fonction de leur capacité restante
        robots.sort(key=lambda x: x.capacity, reverse=True)
        for robot in robots:
            # essayer d'ajouter la tâche au robot courant
            robot.add_task(task)
            if task in robot.tasks:
                # la tâche a été ajoutée avec succès, on passe à la suivante
                break


# Exemple d'utilisation
tasks = TaskGenerator(n_simple_tasks=10, n_auction_tasks=5, deadline=10, auction_deadline=5, max_reward=10).generate()

robots = [Robot(5), Robot(8), Robot(10)]

allocate_tasks(robots, tasks)

for robot in robots:
    print(robot)
