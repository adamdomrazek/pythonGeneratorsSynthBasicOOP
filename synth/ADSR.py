'''
    Instead of keeping track of the current sample number:
    time=1sec   -> n=44_100
    time=10sec  -> n=440_100 
    this class implements a generator that uses 3 different generators (itertools.count)
    for attack time, decay time, release time
    
    At the start of iteration __iter__ sets self.val=0
    and sets current stepper to get_ads_stepper()
        self.stepper = get_ads_stepper() 
        
    ================================================================================================================
    powiniennem to pisać od końca zaczzynając od implementacji __iter__ i __next__
    potem zdefiniować co poszczególne metody robią dokładnie
    
    
    1. 
        def __next__(self):
            self._val = next(self._stepper)
            return None
            
        def __iter__(self):
            self._val = 0
            self._stepper = get_ads_stepper
            self._ended = 0
            return self
            
    2. 
        def get_ads_stepper(self):
            # rules for setting up self.stepper 
    ================================================================================================================
'''
import itertools
import numpy as np

class ADSR_Envelope():
    def __init__(self,
                 sampling_rate,
                 attack_duration=0.05,
                 decay_duration=0.2,
                 release_duration=0.3,
                 sustain_level=0.7
                 ):
        self._attack_duration = attack_duration
        self._decay_duration = decay_duration
        self._release_duration = release_duration
        self._sustain_level = sustain_level
        self._sampling_rate = sampling_rate
            
    def _get_ads_stepper(self):
        '''
            main generator for attack, decay and sustain phase
            
            Takes care of attack, decay and sustain phase
            Attack and decay phase have their own steppers (generators/itertools.cout)
            switching between phases is determined by self.val 
        '''
        # =================== attack & decay steppers init code =================== 
        steppers = []
        # attack stepper
        if self._attack_duration > 0:
            steppers.append(itertools.count(start=0,
                                            step= 1 / (self._attack_duration * self._sampling_rate)))
        # decay stepper
        if self._decay_duration > 0:
            steppers.append(itertools.count(start=1,
                                            step=-(1 - self._sustain_level) / (self._decay_duration  * self._sampling_rate)))
        
        # =================== main generator loop =================== 
        while True:                                         # infinite generator
            l = len(steppers)                               # number of steppers determines the functinality
            if l>0:                                           # check if steppers list is not empty
                val = next(steppers[0])
                if l == 2 and val > 1:                      # 2 steppers and val>1
                    steppers.pop(0)                         # remove attack stepper
                    val = next(steppers[0])
                elif l == 1 and val < self._sustain_level:  # one stepper case and sample val below sustain level
                    steppers.pop(0)
                    val = self._sustain_level
            else:   
                val = self._sustain_level                   # steppers list empty = apmplitude is constant
            
            yield val                                       # generator yield
    
    def _get_release_stepper(self):
        '''
            Takes care of release phase
        '''
        # =================== release phase init code =================== 
        val = self._sustain_level    # before was set to 1
        if self._release_duration > 0:
            release_step = - self._val / (self._release_duration * self._sampling_rate)
            stepper = itertools.count(self._val, step=release_step)     # count from current sustain value to zero
        else:
            val = -1  
        
        # =================== main generator loop =================== 
        while True:                     # infinite generator
            if val <= 0:                # if the value of current sample is below zero stop generator
                self._ended = True      # and set next sample value to zero
                val = 0
            else:
                val = next(stepper)     # increment release stepper until it reaches negative value
            yield val

    def __iter__(self):
        self._val = 0
        self._ended = False
        self._stepper = self._get_ads_stepper()
        return self
    
    def __next__(self):
        self._val = next(self._stepper)
        return self._val
    
    # change self.stepper for relase phase
    def trigger_release(self):
        self._stepper = self._get_release_stepper()
        
    def getValues(self, simTime):
        self.__iter__()
        sig = np.array([self.__next__() for i in range(self._sampling_rate * simTime)])
        return sig 









