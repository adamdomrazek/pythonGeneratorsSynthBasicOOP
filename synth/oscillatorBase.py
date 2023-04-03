'''
    Oscillator base class
'''

import numpy as np
from abc import ABC, abstractmethod


# ============================= Oscillator class =============================
class Oscillator(ABC):
    '''
        This class contains basic attributes of every oscilator,
        those include:
            _f frequency
            _a amplitude
            _p phase shift
        
        Properites for setting and getting these attributes:
            freq
            ampl
            phase
    '''
    def __init__(self,
                 freq=440,
                 phase=0,
                 ampl=1,
                 sampling_rate=44_100,
                 wave_range=(-1, 1)):
        
        self._sampling_rate = sampling_rate
        self._wave_range = wave_range
        
        # Properties can be changed
        self._freq = freq
        self._ampl = ampl
        self._phase = phase
        
    # Properties for private variables _f, _a, _p -> getters & setters
    # will manage operations like: objectName.freq = 10 without setters
    @property
    def freq(self):
        return self._freq
    @freq.setter
    def freq(self, value):
        self._freq = value
    @property
    def ampl(self):
        return self._ampl
    @ampl.setter
    def ampl(self, value):
        self._ampl = value
    @property
    def phase(self):
        return self._phase
    @phase.setter
    def phase(self, value):
        self._phase = value
    @property
    def samplingRate(self):
        return self._sampling_rate
    
    # może do wywalenia
    @staticmethod
    def squish_val(val, min_val=0, max_val=1):
        return (((val + 1) / 2 ) * (max_val - min_val)) + min_val
    
    # Implementation will depend on the type of an oscillator
    @abstractmethod
    def _initialize_osc(self):
        pass
            
    @abstractmethod
    def __next__(self):
        return None
    
    @abstractmethod
    def __iter__(self):
        return self
    
    # Public methods
    def getValues(self, simTime):
        ''' Will have to think about this one - don't know if it is a good practice '''
        self.__iter__()
        sig = np.array([self.__next__() for i in range(self._sampling_rate * simTime)])
        return sig  
    