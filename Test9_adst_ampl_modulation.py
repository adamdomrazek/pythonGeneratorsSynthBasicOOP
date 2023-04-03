import matplotlib.pyplot as plt
import numpy as np

from synth import oscillators as oscry
from synth import helpers
from synth import signalOperations as sigop
from synth import ADSR
from synthHelpers import prettyFigures as pf
import modulatedOscillator as mo


def apply_amp_mod():
    pass


if __name__ == '__main__':
    # source oscillator config
    sampl_rate  = 44_100
    freq        = 2000
    phase       = 0
    ampl        = 1
    duration    = 1
    plotStopTime = 20e-3
    
    src_oscillator = oscry.SquareOscillator(freq=freq, 
                                            phase=0, 
                                            ampl=1,
                                            sampling_rate=sampl_rate,
                                            wave_range=(-1, 1))
    ampl_modulator = ADSR.ADSR_Envelope(sampl_rate,
                                        attack_duration=0.005, 
                                        decay_duration=0.005,
                                        release_duration=1,
                                        sustain_level=0)
    modulated_osc = mo.ModulatedOscillator(oscillator=src_oscillator,
                                           modulators=ampl_modulator,
                                           amp_mod=apply_amp_mod)
    
# src_oscillator_signal = src_oscillator.getValues(simTime=duration)

# osc_sig_plot = osc_sig[0:int(sampl_rate*plotStopTime)]
# n = np.linspace(0, plotStopTime, osc_sig_plot.shape[-1])




# mod_sig = mod.getValues(simTime=duration)
# mod_sig_plot = mod_sig[0:int(sampl_rate*plotStopTime)]

# modulated_sig = mod_sig*osc_sig
# modulated_sig_plot = modulated_sig[0:int(sampl_rate*plotStopTime)]

# pf.plot( (n, modulated_sig_plot, n, mod_sig_plot), alpha=0.5,
#         major_ticks=(0.005,0.25),
#         minor_ticks=(5, 2),
#         label='sine wave',
#         _figsize=(7, 3))
# plt.show()

# # helpers.saveWaveFromArray(modulated_sig, fname='asdrmodTest.wav', ampl=1, sr=sampl_rate)
















