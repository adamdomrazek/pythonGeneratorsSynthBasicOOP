'''
    oscylatory i modulatory to generatory
    takie jak ADSR
'''

class ModulatedOscillator:
    def __init__(self, oscillator, *modulators, amp_mod=None, freq_mod=None, phase_mod=None):
        self.oscillator = oscillator                # source oscillator
        self.modulators = modulators                # list of modulator generators (eg. ADSR - generates values of modulating samples)
        self.amp_mod = amp_mod                      # []_mod are functions that actually apply modulations     
        self.freq_mod = freq_mod                    #
        self.phase_mod = phase_mod                  #
        self._modulators_count = len(modulators)    
    
    def __iter__(self):
        iter(self.oscillator)                                   # start generators (source oscillator and modulators)
        [iter(modulator) for modulator in self.modulators]      # 
        return self
    
    def __next__(self):
        mod_vals = [next(modulator) for modulator in self.modulators]       # get next sample of each modulator to mod_vals list
        self._modulate(mod_vals)                                            # use values from modulators to modulate oscillator parameters
        return next(self.oscillator)                                        # returns next sample of modulated source oscillator
    
    def _modulate(self, mod_vals):
        '''
            Function that applies modulating values (mod_vals) to oscillator parameters
        '''
        if self.amp_mod is not None:
            new_amp = self.amp_mod(self.oscillator.init_amp, mod_vals[0])
            self.oscillator.amp = new_amp

    def trigger_release(self):
        '''
            Function used to stop modulators generators and source oscillator generator
            stop generators = obj.trigger_release()
        '''
        tr = "trigger_release"
        for modulator in self.modulators:
            if hasattr(modulator, tr):
                modulator.trigger_release()
        if hasattr(self.oscillator, tr):
            self.oscillator.trigger_release()
            
    @property
    def ended(self):
        e = "ended"
        ended = []
        for modulator in self.modulators:
            if hasattr(modulator, e):
                ended.append(modulator.ended)
        if hasattr(self.oscillator, e):
            ended.append(self.oscillator.ended)
        return all(ended)                           # return True if all generators are done

    