import pytest
from ligotools import write_wavfile
from ligotools import reqshift
from scipy.interpolate import interp1d
import numpy as np
from scipy.io import wavfile

np.random.seed(42) 

# This function generates a random dataset of size 4096 and asserts that the result of calling reqshift returns the expected value.
def testing_reqshift():
    data = np.random.rand(4096)
    result = [0.91106389, 1.4043249, 1.12951738, 0.73463462, 0.39314469, 0.33419548, 0.67618818, 0.87367694, 0.30667375, -0.03525917]
    req_shift = reqshift(data,fshift=100,sample_rate=4096)
    assert np.allclose(result, req_shift[:10])

def testing_write_wavfile():
    filename  = "test_wavfile.wav"
    x = np.arange(1, 100)
    f = 1/10
    data = np.sin(2 * np.pi * f * x)

    write_wavfile(filename,f,data)
    _, output = wavfile.read(filename)
    
    result = np.int16(data/np.max(np.abs(data)) * 32767 * 0.9)
    assert np.allclose(output, result)