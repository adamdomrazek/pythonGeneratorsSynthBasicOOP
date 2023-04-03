import matplotlib.pyplot as plt
from synthHelpers import prettyFigures as pf
import numpy as np
from synth import oscillators as oscry
from synth import helpers
from synth import signalOperations as sigop

sampl_rate  = 44_100
freq        = 400
phase       = 0
ampl        = 0.1
duration    = 1
osc = oscry.TriangleOscillator(freq=freq, phase=0, ampl=ampl, sampling_rate=sampl_rate, wave_range=(-1, 1))
osc_sig = osc.getValues(simTime=duration)

plotStopTime = 5e-3

osc_sig_plot = osc_sig[0:int(sampl_rate*plotStopTime)]
n = np.linspace(0, plotStopTime, osc_sig_plot.shape[-1])

# plot
xmajor = plotStopTime/5
ymajor = ampl/4
pf.plot( (n, osc_sig_plot),
        major_ticks=(xmajor, ymajor),
        minor_ticks=(5, 2),
        label='sawtooth wave',
        _figsize=(7, 3))
plt.show()

helpers.saveWave(wave1=osc, wave2=None, fname=f'test_trianle{freq}hz.wav', ampl=1, simTime=duration)