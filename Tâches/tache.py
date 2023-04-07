from typing import List, Tuple
import random

class Task:
    def __init__(self, task_id: int, reward: int, deadline: int):
        self.task_id = task_id
        self.reward = reward
        self.deadline = deadline
    
    def __repr__(self):
        return f"Task({self.task_id}, {self.reward}, {self.deadline})"
        
class SimpleTask(Task):
    def __init__(self, task_id: int, reward: int, deadline: int):
        super().__init__(task_id, reward, deadline)
        
class AuctionTask(Task):
    def __init__(self, task_id: int, deadline: int, auction_deadline: int):
        self.auction_deadline = auction_deadline
        super().__init__(task_id, 0, deadline)

class TaskGenerator:
    def __init__(self, n_simple_tasks: int, n_auction_tasks: int, deadline: int, auction_deadline: int, max_reward: int):
        self.n_simple_tasks = n_simple_tasks
        self.n_auction_tasks = n_auction_tasks
        self.deadline = deadline
        self.auction_deadline = auction_deadline
        self.max_reward = max_reward
        self.task_id = 0
    
    def generate(self) -> List[Task]:
        tasks = []
        for i in range(self.n_simple_tasks):
            task = SimpleTask(self.task_id, random.randint(1, self.max_reward), self.deadline)
            tasks.append(task)
            self.task_id += 1
            
        for i in range(self.n_auction_tasks):
            task = AuctionTask(self.task_id, self.deadline, self.auction_deadline)
            tasks.append(task)
            self.task_id += 1
            
        return tasks
