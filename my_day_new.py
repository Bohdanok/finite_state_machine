"""My day"""
import random
import copy
import matplotlib.pyplot as plt
class Bohdan:
    """The representation of me"""
    def __init__(self, health, success_rate, energy, hunger,mental_health, allowance) -> None:
        self.hunger = hunger
        self.health = health
        self.success_rate = success_rate
        self.energy = energy
        self.allowance = allowance
        self.mental_health = mental_health


    def __repr__(self) -> str:
        return f"Bohdan:\nHealth: {self.health}\nEnergy: {self.energy}\nHunger: {self.hunger}\nSuccess rate: {self.success_rate}\nMental health: {self.mental_health}\nAllowance: {self.allowance}\n"

def yielder(function):
    def wrapper(*args, **kwargs):
        data = function(*args, **kwargs)
        data.send(None)
        return data
    return wrapper

class FSM:
    """Finite state machine"""
    def __init__(self, bohdan:Bohdan) -> None:
        self.start = self.start_day_cycle()
        self.current_state = self.start

        self.bohdan = bohdan
        self.cache_bohdan = copy.deepcopy(bohdan)

        self.sleep = self.sleep_state()
        self.oversleep = self.oversleep_state()
        self.mental_breakdown = self.mental_breakdown_state()
        self.bulking = self.bulking_state()
        self.eating = self.eating_state()
        self.working = self.working_state()
        self.super_work = self.super_work_state()
        self.rest = self.rest_state()

        self.start.send(None)
        self.sleep.send(None)
        self.oversleep.send(None)
        self.mental_breakdown.send(None)
        self.bulking.send(None)
        self.eating.send(None)
        self.working.send(None)
        self.super_work.send(None)
        self.rest.send(None)


        print("Hi")
        print("Hi")

        self.alive = True
        # self.current_state = self.start
        self.end = False
    def send(self, data):
        """Starting send"""
        if self.bohdan.health < 1:
            self.alive = False

        try:
            self.current_state.send(data)
        except StopIteration:
            print(data)
            # self.end = True
    # @yielder
    def start_day_cycle(self):
        while True:
            data = yield
            if self.bohdan == self.cache_bohdan:
                print('It is the start of the cycle!!')
            else:
                print(f"The change in Bohdan's characteristics:\nHealth: {self.cache_bohdan.health} -> {self.bohdan.health}\nHunger: {self.cache_bohdan.hunger} -> {self.bohdan.hunger}\nEnergy: {self.cache_bohdan.energy} -> {self.bohdan.energy}\nMental health: {self.cache_bohdan.mental_health} -> {self.bohdan.mental_health}\nSuccess rate: {self.cache_bohdan.success_rate} -> {self.bohdan.success_rate}\nAllowance {self.cache_bohdan.allowance} -> {self.bohdan.allowance}")
            self.bohdan.health = min(self.bohdan.health + 8, 100)
            self.bohdan.energy = min(self.bohdan.energy + 9, 100)
            self.bohdan.hunger = max(self.bohdan.hunger - 3, 0)
            self.bohdan.mental_health = min(self.bohdan.mental_health + 2, 100)
            if random.random() < 0.08:
                self.bohdan.allowance += 2000
            self.current_state = self.sleep

    # @yielder
    def sleep_state(self):
        """The sleeping state"""
        # add_energy, add_health
        while True:
            data = yield
            print(f"Current state: {self.current_state}   Hour = {data}.\n{self.bohdan}")
            self.bohdan.health = min(self.bohdan.health + 5, 100)
            self.bohdan.energy = min(self.bohdan.energy + 9, 100)
            self.bohdan.hunger = max(self.bohdan.hunger - 3, 0)
            self.bohdan.mental_health = min(self.bohdan.mental_health + 2, 100)
            if data == 8 and random.random() > 0.2:
                self.bohdan.health = min(self.bohdan.health, 100)
                self.bohdan.energy = min(self.bohdan.energy, 100)
                self.bohdan.hunger = max(self.bohdan.hunger, 0)
                if random.random() < 0.3:
                    self.current_state = self.bulking
                else: self.current_state = self.eating
            elif data == 8:
                self.bohdan.health = min(self.bohdan.health, 100)
                self.bohdan.energy = min(self.bohdan.energy, 100)
                self.bohdan.hunger = max(self.bohdan.hunger, 0)
                self.current_state = self.oversleep

    # @yielder
    def oversleep_state(self):
        while True:
            data = yield
            print(f"Current state: {self.current_state}   Hour = {data}.\n{self.bohdan}")
            
            self.bohdan.energy += 9
            self.bohdan.health += 5
            self.bohdan.hunger -= 3
            if data == 11:
                self.bohdan.health = min(self.bohdan.health, 100)
                self.bohdan.energy = min(self.bohdan.energy, 100)
                self.bohdan.hunger = max(self.bohdan.hunger, 0)
                self.bohdan.mental_health -= 10
                self.bohdan.success_rate -= 30
                if random.random() < 0.3:
                    self.current_state = self.bulking
                else: self.current_state = self.eating
            if random.random() > 0.5:
                self.bohdan.health = min(self.bohdan.health, 100)
                self.bohdan.energy = min(self.bohdan.energy, 100)
                self.bohdan.hunger = max(self.bohdan.hunger, 0)
                self.bohdan.mental_health -= 2
                self.bohdan.success_rate -= 20
                if random.random() < 0.3:
                    self.current_state = self.bulking
                else: self.current_state = self.eating

    # @yielder
    def eating_state(self):
        """Eat something"""
        while True:
            data = yield
            print(f"Current state: {self.current_state}   Hour = {data}.\n{self.bohdan}")
            self.bohdan.energy = min(self.bohdan.energy + 10, 100)
            self.bohdan.health = min(self.bohdan.health + 2, 100)
            self.bohdan.hunger = min(self.bohdan.hunger + 30, 100)
            self.bohdan.allowance -= random.randint(55, 75)
            self.current_state = self.working

    # @yielder
    def bulking_state(self):
        """The BUlking meal"""
        while True:
            data = yield
            print(f"Current state: {self.current_state}   Hour = {data}.\n{self.bohdan}")
            self.bohdan.allowance -= random.randint(80, 100)
            self.bohdan.energy = min(self.bohdan.energy + 15, 100)
            self.bohdan.health = min(self.bohdan.health + 2, 100)
            self.bohdan.hunger = min(self.bohdan.hunger + 40, 100)
            self.bohdan.mental_health += 3
            self.current_state = self.super_work

    # @yielder
    def super_work_state(self):
        while True:
            data = yield
            print(f"Current state: {self.current_state}   Hour = {data}.\n{self.bohdan}")
            self.bohdan.energy = max(self.bohdan.energy - 10, 0)
            self.bohdan.health = max(self.bohdan.health - 5, 0)
            self.bohdan.hunger = max(self.bohdan.hunger - 6, 0)
            self.bohdan.mental_health = max(self.bohdan.mental_health - 1, 0)
            self.bohdan.success_rate += 10
            if data == 14 or data == 19:
                if random.random() < 0.3:
                    self.current_state = self.bulking
                else: self.current_state = self.eating
            if data == 22:
                self.current_state = self.rest

    # @yielder
    def working_state(self):
        """WOrk work work"""
        while True:
            data = yield
            print(f"Current state: {self.current_state}   Hour = {data}.\n{self.bohdan}")
            self.bohdan.energy = max(self.bohdan.energy - 10, 0)
            self.bohdan.health = max(self.bohdan.health - 5, 0)
            self.bohdan.hunger = max(self.bohdan.hunger - 6, 0)
            self.bohdan.mental_health = max(self.bohdan.mental_health - 3, 0)
            self.bohdan.success_rate += 5
            if data == 14 or data == 19:
                if random.random() < 0.3:
                    self.current_state = self.bulking
                else:
                    self.current_state = self.eating
            elif data == 22:
                if random.random() < 0.2:
                    self.current_state = self.mental_breakdown
                else: self.current_state = self.rest

    # @yielder
    def rest_state(self):
        while True:
            data = yield
            print(f"Current state: {self.current_state}   Hour = {data}.\n{self.bohdan}")
            self.bohdan.energy = max(self.bohdan.energy - 10, 0)
            self.bohdan.health = min(self.bohdan.health + 1, 100)
            self.bohdan.hunger = max(self.bohdan.hunger - 5, 0)
            if data == 23:
                self.current_state = self.start

    # @yielder
    def mental_breakdown_state(self):
        """Mental breakdown"""
        while True:
            data = yield
            print(f"Current state: {self.current_state}   Hour = {data}.\n{self.bohdan}")
            if data == 23:
                self.current_state = self.start
            self.bohdan.success_rate -= 20
            self.bohdan.energy = max(self.bohdan.energy - 15, 0)
            self.bohdan.health = max(self.bohdan.health - 10, 0)
            self.bohdan.hunger = max(self.bohdan.hunger - 10, 0)
            self.bohdan.mental_health = max(self.bohdan.mental_health - 4, 0)

def start_the_day1(number_of_days:int):
    """Simulate defined number of days"""
    random.seed(1)
    boh = Bohdan(100, 0, 100, 100, 100, 2000)
    execution = FSM(boh)
    hours = (i for i in range(0, 23) for j in range(number_of_days))
    while hours:
        try:
            execution.send(next(hours))
        except StopIteration:
            return

def plot_characteristics_by_days(number_of_days: int):
    """
    Simulate defined number of days
    This is just some plotting
    """
    random.seed(1)
    boh = Bohdan(100, 0, 100, 100, 100, 2000)
    execution = FSM(boh)

    # Lists to store parameter values by days
    health_values = []
    success_rate_values = []
    energy_values = []
    hunger_values = []
    mental_health_values = []
    allowance_values = []

    for day in range(number_of_days):
        # Lists to store parameter values for the current day
        day_health = []
        day_success_rate = []
        day_energy = []
        day_hunger = []
        day_mental_health = []
        day_allowance = []

        for time in range(0, 24):
            execution.send(time)

            # Append current parameter values to lists for the day
            day_health.append(boh.health)
            day_success_rate.append(boh.success_rate)
            day_energy.append(boh.energy)
            day_hunger.append(boh.hunger)
            day_mental_health.append(boh.mental_health)
            day_allowance.append(boh.allowance)

        # Append the average parameter values for the day to the main lists
        health_values.append(sum(day_health) / len(day_health))
        success_rate_values.append(sum(day_success_rate) / len(day_success_rate))
        energy_values.append(sum(day_energy) / len(day_energy))
        hunger_values.append(sum(day_hunger) / len(day_hunger))
        mental_health_values.append(sum(day_mental_health) / len(day_mental_health))
        allowance_values.append(sum(day_allowance) / len(day_allowance))

    # Plotting
    plt.figure(figsize=(12, 8))

    plt.subplot(3, 2, 1)
    plt.plot(range(1, number_of_days + 1), health_values)
    plt.title('Health')
    plt.xlabel('Days')
    plt.ylabel('Value')

    plt.subplot(3, 2, 2)
    plt.plot(range(1, number_of_days + 1), success_rate_values)
    plt.title('Success Rate')
    plt.xlabel('Days')
    plt.ylabel('Value')

    plt.subplot(3, 2, 3)
    plt.plot(range(1, number_of_days + 1), energy_values)
    plt.title('Energy')
    plt.xlabel('Days')
    plt.ylabel('Value')

    plt.subplot(3, 2, 4)
    plt.plot(range(1, number_of_days + 1), hunger_values)
    plt.title('Hunger')
    plt.xlabel('Days')
    plt.ylabel('Value')

    plt.subplot(3, 2, 5)
    plt.plot(range(1, number_of_days + 1), mental_health_values)
    plt.title('Mental Health')
    plt.xlabel('Days')
    plt.ylabel('Value')

    plt.subplot(3, 2, 6)
    plt.plot(range(1, number_of_days + 1), allowance_values)
    plt.title('Allowance')
    plt.xlabel('Days')
    plt.ylabel('Value')

    plt.tight_layout()
    plt.show()

plot_characteristics_by_days(100)
# start_the_day1(1)