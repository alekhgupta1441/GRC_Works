import numpy as np

# Two versions of the chirp function are provided.  Depending on need
# it is more convenient sometimes to describe a chirp in terms of low
# and high frequencies, along with time length of chirp.  Other times
# it is convenient to describe chirp in terms of center frequency,
# bandwidth, repetition rate, and sample rate.
#
# The frequency based version generates the chirp waveform.  The center
# frequency version simply has its parameters used to generate
# new parameters to call the frequency span version.
#
# See http://en.wikipedia.org/wiki/Chirp for details on derivation.
# chirp
#
# Generate a frequency sweep from low to high over time.
# Waveform description is based on number of samples.
#
# Inputs
#  numSamples: integer, number of samples in chirp waveform.
#  chirpLen_s: float, time span in seconds of chirp.
#  start_Hz: float, start (lower) frequency in Hz of chirp.
#  stop_Hz: float, stop (upper) frequency in Hz of chirp.
#  phase_rad: phase in radians at waveform start, default is 0.
#
# Output
#  Time domain chirp waveform of length numSamples.

def chirp(numSamples, chirpLen_s, start_Hz, stop_Hz, phase_rad = 0):

    times_s = np.linspace(0, chirpLen_s, numSamples) # Chirp times.
    k = (stop_Hz - start_Hz) / chirpLen_s # Chirp rate.
    sweepFreqs_Hz = (start_Hz + k/2. * times_s) * times_s
    chirp = np.sin(phase_rad + 2 * np.pi * sweepFreqs_Hz)

    return chirp

# chirpCtr
#
# Generate a frequency sweep from low to high over time.
# Waveform description is based on center frequency.
# This is primarily useful when generating a chirp to play against a
# previously captured signal using that sample rate.
#
# Inputs
#  centerFreq_Hz: float, center frequency in Hz of the chirp.
#  sampleRate_Hz: sample rate in Hz of chirp waveform.
#  repRate_Hz: integer, number of full chirps per second.
#  bandwidth_Hz: float, bandwidth of chirp.
#  phase_rad: phase in radians at waveform start, default is 0.
#
# Output
#  Time domain chirp waveform of length numSamples.

def chirpCtr(centerFreq_Hz, sampleRate_Hz, repRate_Hz, bandwidth_Hz, phase = 0):

    numSamples = int(sampleRate_Hz / repRate_Hz)
    start_Hz = centerFreq_Hz - bandwidth_Hz / 2.
    stop_Hz = centerFreq_Hz + bandwidth_Hz / 2.
    chirpLen_s = 1. / repRate_Hz

    return chirp(numSamples, chirpLen_s, start_Hz, stop_Hz, phase)
