"""
# Traffic
### Author: Daniel Herrera
### Date: Nov 17, 2020
### Purpose: 
        Socket connection statistical graphing.
"""
from . import projcommon as common
import multiprocessing as mp

class Car(mp.Process):
    def __init__(self, threadID: int, threadName: str, counter: int):
        mp.Process.__init__(self)
        self.__threadID = threadID
        self.__threadName = threadName
        self.__counter = counter

    @property
    def threadID(self):
        return self.__counter

    @property
    def threadName(self):
        return self.__counter

    @property
    def counter(self):
        return self.__counter

    def run(self):
        print(self)

def test_module():
    print(f"{common.Fore.GREEN}\t working... {common.Style.RESET_ALL}\n\n")