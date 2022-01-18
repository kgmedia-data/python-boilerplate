from scripts.libs.my_libs import MyLibs
from config.env import ENV_VARS_1

ml = MyLibs()

class Job:

    def __init__(self):
        pass

    def run(self):
        print("Job is doing something!")
        ml.do_something()