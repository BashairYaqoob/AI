#agent sketch
class Environment:
    pass
class Agent:
    pass
def run_agent(Environment, Agent):
    pass
  #_____________________________
#basic agent => SIMPLE REFLEXIVE
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
#for 2d environment
class Environment:
    def __init__(self):
        self.grid = [
            ['dirty','clean','dirty'],
            ['dirty','clean','clean'],
            ['clean','clean','dirty']
        ]
    
    def get_percept(self, row, col):
        return self.grid[row][col]
    
    def clean(self, row, col):
        self.grid[row][col] = 'clean'

    def display(self, ar, ac):
        print("Grid:")
        for i in range(3):
            row = []
            for j in range(3):
                if i == ar and j == ac:
                    row.append('_')  # agent
                else:
                    row.append(self.grid[i][j])
            print(" | ".join(row))
        print()
    

class Agent:
    def act(self, percept):
        if percept == 'dirty':
            return 'clean'
        else:
            return 'move'


def run_agent(environment, agent, steps):
    row, col = 0, 0

    for i in range(steps):
        percept = environment.get_percept(row, col)
        action = agent.act(percept)

        print(f"Step {i+1}: Percept = {percept}, "
              f"Position = ({row},{col}), Action = {action}")

        if action == 'clean':
            environment.clean(row, col)
        else:
            col += 1
            if col == 3:
                row += 1
                col = 0
            if row == 3:
                break

        environment.display(row, col)


environment = Environment()
agent = Agent()
run_agent(environment, agent, 9)
#_________________________________________
#1d -> 2d => Environment class change
#agent -> agent change=> Agent class change
class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'
class ModelBasedAgent:
    def __init__(self):
        self.model = {} #current : dirty / clean

    def update_model(self, percept):
        self.model['current'] = percept
        print(self.model)

    def predict_action(self):
        if self.model['current'] == 'Dirty':
            return 'Clean the room'
        else:
            return 'do nothing'

    def act(self, percept):
        self.update_model(percept)
        return self.predict_action()
    
def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)
        print(f"Step {step + 1}: Percept - {percept}, Action - {action}")
        if percept == 'Dirty':
            environment.clean_room()


# Create instances of agent and environment
agent = ModelBasedAgent()
environment = Environment()

# Run the agent in the environment for 5 steps
run_agent(agent, environment, 5)
#_______________________________________
class GoalBasedAgent:
    def __init__(self):
        self.goal = 'Clean'

    def formulate_goal(self, percept):
        if percept == 'Dirty':
            self.goal = 'Clean'
        else:
            self.goal = 'No action needed'

    def act(self, percept):
        self.formulate_goal(percept)
        if self.goal == 'Clean':
            return 'Clean the room'
        else:
            return 'Room is clean'


class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'


def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)
        print(f"Step {step + 1}: Percept - {percept}, Action - {action}")
        if percept == 'Dirty':
            environment.clean_room()


# Create instances of agent and environment
agent = GoalBasedAgent()
environment = Environment()

# Run the agent in the environment for 5 steps
run_agent(agent, environment, 5)
#____________________________________
class UtilityBasedAgent:
    def __init__(self):
        self.utility = {'Dirty': -10, 'Clean': 10}

    def calculate_utility(self, percept):
        return self.utility[percept]

    def select_action(self, percept):
        if percept == 'Dirty':
            return 'Clean the room'
        else:
            return 'No action needed'

    def act(self, percept):
        action = self.select_action(percept)
        return action


class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'


def run_agent(agent, environment, steps):
    total_utility = 0
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)
        utility = agent.calculate_utility(percept)
        print(f"Step {step + 1}: Percept - {percept}, Action - {action}, Utility - {utility}")
        total_utility += utility
        if percept == 'Dirty':
            environment.clean_room()
    print("Total Utility:", total_utility)


# Create instances of agent and environment
agent = UtilityBasedAgent()
environment = Environment()

# Run the agent in the environment for 5 steps
run_agent(agent, environment, 5)
#________________________________________
import random

class LearningBasedAgent:
    def __init__(self, actions):
        self.Q = {}
        self.actions = actions
        self.alpha = 0.1  # Learning rate (intelligence)
        self.gamma = 0.9  # Discount factor (accuracy/ authenticity)
        self.epsilon = 0.1  # Exploration rate (probability)

    def get_Q_value(self, state, action):
        return self.Q.get((state, action), 0.0)

    def select_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.actions)
        else:
            return max(self.actions, key=lambda a: self.get_Q_value(state, a))

    def learn(self, state, action, reward, next_state):
        old_Q = self.get_Q_value(state, action)
        best_future_Q = max([self.get_Q_value(next_state, a) for a in self.actions])
        self.Q[(state, action)] = old_Q + self.alpha * (reward + self.gamma * best_future_Q - old_Q)

    def act(self, state):
        action = self.select_action(state)
        return action

class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'
        return 10

    def no_action_reward(self):
        return 0

def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)
        if percept == 'Dirty':
            reward = environment.clean_room()
            print(f"Step {step + 1}: Percept - {percept}, Action - {action}, Reward - {reward}")
        else:
            reward = environment.no_action_reward()
            print(f"Step {step + 1}: Percept - {percept}, Action - {action}, Reward - {reward}")
        next_percept = environment.get_percept()
        agent.learn(percept, action, reward, next_percept)


# Create instances of agent and environment
agent = LearningBasedAgent(['Clean the room', 'No action needed'])
environment = Environment()

# Run the agent in the environment for 5 steps
run_agent(agent, environment, 5)
