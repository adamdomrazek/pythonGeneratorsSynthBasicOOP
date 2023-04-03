'''
    This module contains classes/functions that will be used to manipulate waveforms
'''
import numpy as np
from .oscillatorBase import Oscillator

class WaveAdder:
    '''
        Sampling rate of both of the oscillators has to be the same
    '''
    def __init__(self, *oscillators: Oscillator):
        self.oscillators = oscillators
        self.n = len(oscillators)
        self.samplingRate = self.oscillators[0].samplingRate
        
    def __iter__(self):
        [iter(osc) for osc in self.oscillators]
        return self
        
    def __next__(self):
        return sum( next(osc) for osc in self.oscillators )
    
    def getValues(self, simTime):
        self.__iter__()
        # divide signal by the number of oscillators -> to bound amplitude
        sig = np.array([self.__next__() for i in range(self.samplingRate * simTime)]) / self.n
        return sig  
    
    