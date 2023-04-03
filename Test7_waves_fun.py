import matplotlib.pyplot as plt
from synthHelpers import prettyFigures as pf
import numpy as np
from synth import oscillators as oscry
from synth import helpers
from synth import signalOperations as sigop

osc1 = sigop.WaveAdder(
    oscry.SquareOscillator(27.5, ampl=0.1),
    oscry.TriangleOscillator(55, ampl=0.5),
    oscry.SineOscillator(110),
    oscry.SquareOscillator(220, ampl=0.1),
    oscry.SineOscillator(440,ampl=0.3),
    oscry.TriangleOscillator(880,ampl=0.05),
)

wav1 = osc1.getValues(10) / 6    # /6 zeby ampl nie była za duża

osc2 = sigop.WaveAdder(
    oscry.SquareOscillator(27.5, ampl=0.1),
    oscry.TriangleOscillator(55, ampl=0.5),
    oscry.SineOscillator(115),
    oscry.SquareOscillator(220, ampl=0.1),
    oscry.SineOscillator(440,ampl=0.3),
    oscry.TriangleOscillator(880,ampl=0.05),
)

wav2 = osc2.getValues(10) / 6   # /6 zeby ampl nie była za duża

# helpers.saveWave(osc1, osc2, fname="ot_vibes.wav", ampl=0.1, simTime=10)
# helpers.saveWaveFromArray(wav1, wav2, fname="ot_vibes.wav", ampl=0.1, sr=osc1.samplingRate)

a,b,c = helpers.spectrumPlot(wav1, slice(0, 1000), sample_rate=osc1.samplingRate)
plt.plot(a, b)
plt.show()