import time
from random import randint
import functools
import getpass


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        FUNC = (func.__name__).replace('_', ' ')
        FUNC = FUNC.capitalize()
        usr_func = f"({getpass.getuser()})Running:\t{FUNC}"
        start_time = time.perf_counter()
        ret = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        usr_func = (usr_func + f"\t[exec-time = {run_time:.7f} secs]\n")
        f = open("machine.log", 'a')
        f.write(usr_func)
        f.close()
        return (ret)
    return wrapper


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
