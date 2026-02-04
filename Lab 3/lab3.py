#agent sketch
class Environment:
    pass
class Agent:
    pass
def run_agent(Environment, Agent):
    pass
  #_____________________________
#basic agent
class Environment:
    def __init__(self, state):
        self.state=state
    def get_percept(self):
        return self.state
class Agent:
    def act(sekf, percept):
        return "clean the room" if percept == "dirty" else "do nothing"
def run_agent(Environment, Agent):
    percept=Environment.get_percept()
    action=Agent.act(percept)
    print(f"percept id {percept}and action is {action}")

env1= Environment("clean")
a1= Agent()
run_agent(env1, a1)
#_________________________________
class Environment:
    def __init__(self, state):
        self.state=state
    def get_percept(self):
        return self.state
    def clean_room(self):
        self.state='clean'
class Agent:
    def act(self, percept):
        return "clean the room" if percept == "dirty" else "do nothing"
def run_agent(Environment, Agent, steps):
    for i in range(steps):
        percept=Environment.get_percept()
        action=Agent.act(percept)
        print(f"step is {i+1}, percept is {percept} and action is {action}")
        if percept == 'dirty':
            Environment.clean_room()

env1= Environment("dirty")
a1= Agent()
run_agent(env1, a1, 5)
#_____________________________________

