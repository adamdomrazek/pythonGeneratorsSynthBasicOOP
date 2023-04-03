'''
    Nie udało się odpalić bo moduł librosa nie działa
'''

import matplotlib.pyplot as plt
import numpy as np

from synth import oscillators as oscry
from synth import helpers

from synthHelpers import prettyFigures as pf
from synth import signalOperations as sigop


# ===================================================================================
dur = 10
s1 = ["C4", "E4", "G4", "B4"] * dur
l1 = [0.25, 0.25, 0.25, 0.25] * dur

s2 = ["C3", "E3", "G3"] * dur
l2 = [0.333334,0.333334, 0.333334] * dur

s3 = ["C2", "G2"] * dur
l3 = [0.5,0.5] * dur

wavl = np.array(helpers.getSigfromNotes(oscry.TriangleOscillator(ampl=0.8), notes=s1, note_lens=l1)) + \
    np.array(helpers.getSigfromNotes(oscry.SineOscillator(), notes=s2, note_lens=l2)) + \
    np.array(helpers.getSigfromNotes(oscry.TriangleOscillator(ampl=0.4), notes=s3, note_lens=l3))

wavr = np.array(helpers.getSigfromNotes(oscry.TriangleOscillator(ampl=0.8), notes=s1[::-1], note_lens=l1)) + \
    np.array(helpers.getSigfromNotes(oscry.SineOscillator(), notes=s2[::-1], note_lens=l2)) + \
    np.array(helpers.getSigfromNotes(oscry.TriangleOscillator(ampl=0.4), notes=s3[::-1], note_lens=l3))

helpers.saveWaveFromArray(wavl, wavr, fname="c_maj7.wav")

# ===================================================================================
# osc_sig = osc.getValues(simTime=duration)
# plotStopTime = 5e-3


# osc_sig_plot = osc_sig[0:int(sampl_rate*plotStopTime)]
# n = np.linspace(0, plotStopTime, osc_sig_plot.shape[-1])

# # plot
# xmajor = plotStopTime/5
# ymajor = ampl/4
# pf.plot( (n, osc_sig_plot),
#         major_ticks=(xmajor, ymajor),
#         minor_ticks=(5, 2),
#         label='sawtooth wave',
#         _figsize=(7, 3))
# plt.show()


