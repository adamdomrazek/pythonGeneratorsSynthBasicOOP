import numpy as np
from scipy.io import wavfile 

from synth.oscillators import Oscillator
# import librosa

# ============================= save wave =============================

# formatSig = lambda wav, amp: np.int16(wav * amp * (2**15 - 1))
formatSig = lambda sig, ampl: np.round(ampl * sig * (2**15-1)).astype(np.int16)

def saveWave(wave1:Oscillator, wave2:Oscillator=None, fname='temp.wav', ampl=0.1, simTime=1):
    wave = wave1.getValues(simTime=simTime)    
    # wave = np.array(wave)
    wave = formatSig(wave, ampl)
    
    if wave2 is not None:
        wave2 = wave2.getValues(simTime=simTime)    
        # wave2 = np.array(wave2)
        wave2 = formatSig(wave2, ampl)
        wave = np.stack([wave, wave2]).T

    wavfile.write(fname, rate=wave1.samplingRate, data=wave)

def saveWaveFromArray(wave1:np.array, wave2:np.array=None, fname='temp.wav', ampl=0.1, sr=44_100):    
    # wave = np.array(wave)
    wave = formatSig(wave1, ampl)
    
    if wave2 is not None:
        # wave2 = np.array(wave2)
        wave2 = formatSig(wave2, ampl)
        wave = np.stack([wave, wave2]).T

    wavfile.write(fname, rate=sr, data=wave)
    

# ============================= spectrum plot =============================

def spectrumPlot(wave, spslice=slice(0, 1000), sample_rate=44_100):
    sp = np.fft.fft(wave)
    sp_mag = np.abs(sp)
    sp_phase = np.angle(sp)
    freq = np.linspace(0, sample_rate, len(wave))
    ampl = sp_mag * 2 / sample_rate
    phase = sp_phase
    return freq[spslice], ampl[spslice], phase[spslice]

# ============================= get values =============================

''' Was used for testing purposes '''
def getValues(osc, simTime, sr):
        ''' Will have to think about this one - don't know if it is a good practice '''
        iter(osc)
        sig = np.array([next(i) for i in range(sr * simTime)])
        return sig  


# ============================= get signal from specified note =============================
# librosa nie działa
# def getSigfromNotes(osc, notes=["C4", "E4", "G4"], note_lens=[0.5,0.5,0.5], SR=44_100):
#     samples = []
#     osc = iter(osc)
#     for note, note_len in zip(notes, note_lens):
#         osc.freq = librosa.note_to_hz(note)
#         for _ in range(int(SR * note_len)):
#             samples.append(next(osc))
#     return samples