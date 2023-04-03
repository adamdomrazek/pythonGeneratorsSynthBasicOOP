'''
    This file contains implementation of various oscilators

    overview jak to działa
    Params:
        freq           frequency of sine wave
        ampl           amplitude
        phase          phase shift in degrees
        sample_rate    number of samples every second
        
    sin( 2*pi*freq * 1/sample_rate )
        
    every second there are #sample_rate number of samples
    sin(2pi*freq*1/512)
    sin(2pi*freq*2/512)
    sin(2pi*freq*3/512)
    ...
    sin(2pi*freq*512/512)
    
    Every second generator generates:
        - #freq number of full cycles
        - #sample_rate number of samples
'''

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile 

from synthHelpers import prettyFigures as pf
from .oscillatorBase import Oscillator

# ============================= Sine oscillator class =============================
class SineOscillator(Oscillator):
    '''
        freq    [hz]
        phase   [degrees]
        ampl    [-]
    '''
    def __init__(self,
                 freq=440,
                 phase=0,
                 ampl=1,
                 sampling_rate=44_100,
                 wave_range=(-1, 1)):
        # call constructr of a base class
        super().__init__(freq, phase, ampl, sampling_rate, wave_range)
        # helper attributes
        self._arg1 = 0
        self._arg2 = 0
        
    def _initialize_osc(self):
        # sin(_arg1 + arg2)
        # arg1 is also increment step size for the generator object
        self._arg2 = self._phase * 2 * math.pi / 360
        self._arg1 = 2 * math.pi * self._freq / self._sampling_rate
        self._i = 0

    def __next__(self):
        val = self._ampl * math.sin(self._i + self._arg2)
        self._i = self._i + self._arg1   # Increment with every generator iteration
        # if self._wave_range is not (-1, 1):
        #     val = self.squish_val(val, *self._wave_range)
        return val
    
    def __iter__(self):
        self._initialize_osc()
        return self
    
# ============================= Square oscillator class =============================
class SquareOscillator(SineOscillator):
    def __init__(self,
                 freq=440,
                 phase=0,
                 ampl=1,
                 sampling_rate=44_100,
                 wave_range=(-1, 1),
                 threshold=0):
        super().__init__(freq, phase, ampl, sampling_rate, wave_range)
        
        self.threshold = threshold
    
    def __next__(self):
        val = self._ampl * math.sin(self._i + self._arg2)
        self._i = self._i + self._arg1
        
        if val < self.threshold:
            val = self._wave_range[0]
        else:
            val = self._wave_range[1]
        return val * self._ampl

# ============================= Sawtooth oscillator class =============================
class SawtoothOscillator(Oscillator):
    # def _post_phase_set(self):
    #     self._p = ((self._p + 90)/ 360) * self._period
    
    def _initialize_osc(self):
        # sin(_arg1 + arg2)
        # arg1 is also increment step size for the generator object
        self._arg2 = self._phase * 2 * math.pi / 360
        self._arg1 = 2 * math.pi * self._freq / self._sampling_rate
        self._i = 0
        
    def _initialize_osc(self):
        self._period = self._sampling_rate / self._freq
        self._i = 0
    
    def __next__(self):
        div = (self._i + self._phase )/self._period
        val = 2 * (div - math.floor(0.5 + div))
        self._i = self._i + 1
        # if self._wave_range is not (-1, 1):
        #     val = self.squish_val(val, *self._wave_range)
        return val * self._ampl
    
    def __iter__(self):
        self._initialize_osc()
        return self

# ============================= Triangle oscillator class =============================
class TriangleOscillator(SawtoothOscillator):
    def __next__(self):
        div = (self._i + self._phase)/self._period
        val = 2 * (div - math.floor(0.5 + div))
        val = (abs(val) - 0.5) * 2
        self._i = self._i + 1
        # if self._wave_range is not (-1, 1):
        #     val = self.squish_val(val, *self._wave_range)
        return val * self._ampl


    
    
    
    
    
    
    
    
    