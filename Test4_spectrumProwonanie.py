#
import matplotlib.pyplot as plt
from synthHelpers import prettyFigures as pf
import numpy as np
from synth import oscillators as oscry
from synth import helpers
from synth import signalOperations as sigop


freq = 100; fslice = slice(80, 800)

fig, axes = plt.subplots(1, 4)
fig.set_size_inches(10, 3)
ax1, ax2, ax3, ax4 = axes
fig.tight_layout() 

osc = oscry.SineOscillator(freq=freq)
osc_sig = osc.getValues(simTime=1)
fplot, magplot, phaseplot = helpers.spectrumPlot(osc_sig, spslice=fslice, sample_rate=44_100)
pf.plot2((fplot, magplot), ax=ax1, title='sine osciallator', xlabel='frequency', ylabel='amplitude')

osc = oscry.SquareOscillator(freq=freq)
osc_sig = osc.getValues(simTime=1)
fplot, magplot, phaseplot = helpers.spectrumPlot(osc_sig, spslice=fslice, sample_rate=44_100)
pf.plot2((fplot, magplot), ax=ax2, title='square osciallator', xlabel='frequency')

osc = oscry.SawtoothOscillator(freq=freq)
osc_sig = osc.getValues(simTime=1)
fplot, magplot, phaseplot = helpers.spectrumPlot(osc_sig, spslice=fslice, sample_rate=44_100)
pf.plot2((fplot, magplot), ax=ax3, title='sawtooth osciallator', xlabel='frequency')

osc = oscry.TriangleOscillator(freq=freq)
sc_sig = osc.getValues(simTime=1)
fplot, magplot, phaseplot = helpers.spectrumPlot(osc_sig, spslice=fslice, sample_rate=44_100)
pf.plot2((fplot, magplot), ax=ax4, title='triangle osciallator', xlabel='frequency')

plt.show()






