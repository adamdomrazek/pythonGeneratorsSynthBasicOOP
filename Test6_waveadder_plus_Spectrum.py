import matplotlib.pyplot as plt
from synthHelpers import prettyFigures as pf
import numpy as np
from synth import oscillators as oscry
from synth import helpers
from synth import signalOperations as sigop


osc1 = oscry.SineOscillator(freq=10, ampl=1)
osc2 = oscry.SineOscillator(freq=20, ampl=0.5, phase=0)

oscsum = sigop.WaveAdder(osc1, osc2)

oscsum_sig = oscsum.getValues(1)
osc1sig = osc1.getValues(1)
osc2sig = osc2.getValues(1)

fslice=slice(0,30)
freq1, ampl1, _ = helpers.spectrumPlot(osc1sig, fslice, sample_rate=osc1.samplingRate)
freq2, ampl2, _ = helpers.spectrumPlot(osc2sig, fslice, sample_rate=osc2.samplingRate)
freqsum, amplsum, _ = helpers.spectrumPlot(oscsum_sig, fslice, sample_rate=osc2.samplingRate)

colors = "#323031", "#308E91", "#34369D","#5E2A7E", "#5E2A7E", "#6F3384"
fig = plt.figure(figsize=(15, 7))

plt.subplot2grid((1,4),(0,0),colspan=3) 
plt.title("Sum of Sines, Time Domain")
plt.plot(oscsum_sig/2, color=colors[0])
plt.plot(osc1sig, alpha=0.2, label='sig1', color=colors[1])
plt.plot(osc2sig, alpha=0.2, label='sig2', color=colors[2])
plt.legend(loc='upper right')

plt.subplot2grid((1,4),(0,3))
plt.title("Sum of Sines, Frequency Domain")
plt.plot(freqsum, amplsum/2, label="Summed", color=colors[0])
plt.plot(freq1,ampl1, label="sig1", alpha=0.4, color=colors[1])
plt.plot(freq2,ampl2, label="sig2", alpha=0.4, color=colors[2])
plt.legend()

plt.show()





