from scipy.io import wavfile
#audio format must be .wav or else cant read
(fs, x)= wavfile.read('/home/r210785/Documents/CL_LAB/week-8/Chorus.wav')
# Reverse the audio sample
x_reverse = x[::-1]
wavfile.write('aud.wav', fs, x_reverse)
