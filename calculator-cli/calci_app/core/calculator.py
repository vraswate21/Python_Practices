"""this module has necessasy base classes"""

from abc import abstractmethod, ABC

class BaseCalculator(ABC):


    @abstractmethod
    def calculate(self):
        """ this method will perform calculation and respond with a result"""
        