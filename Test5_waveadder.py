import matplotlib.pyplot as plt
from synthHelpers import prettyFigures as pf
import numpy as np
from synth import oscillators as oscry
from synth import helpers
from synth import signalOperations as sigop


osc1 = oscry.SineOscillator(freq=2, ampl=2)
osc2 = oscry.SineOscillator(freq=4, ampl=1, phase=0)
osc3 = oscry.SineOscillator(freq=6, ampl=1, phase=0)

oscsum = sigop.WaveAdder(osc1, osc2, osc3)

oscsum_sig = oscsum.getValues(1)
osc1sig = osc1.getValues(1)
osc2sig = osc2.getValues(1)
osc3sig = osc3.getValues(1)


fig, ax = plt.subplots(1, 1)
fig.set_size_inches(10, 5)
pf.plot2(oscsum_sig, ax=ax, label='sum of sig1 and sig2')
pf.plot2(osc1sig, ax=ax, label='sig1')
pf.plot2(osc2sig, ax=ax, label='sig2')
pf.plot2(osc3sig, ax=ax, label='sig3')

plt.legend(loc='upper right')
plt.show()





