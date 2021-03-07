import random
import numpy as np
#https://maspypy.com/%E6%95%B0%E5%AD%A6%E3%83%BBnumpy-%E9%AB%98%E9%80%9F%E3%83%95%E3%83%BC%E3%83%AA%E3%82%A8%E5%A4%89%E6%8F%9Bfft%E3%81%AB%E3%82%88%E3%82%8B%E7%95%B3%E3%81%BF%E8%BE%BC%E3%81%BF
def fft(f, g):
    """
    fft numpy ver.
    constraint:
        coefficients are all integer values.
        let n = max(size(f) ,size(g)) and h = max(coefficients)
        h*h*n should be represented by 64-bit float.
    return f*g
    """
    fft_len = 1<< (len(f) + len(g) - 1).bit_length()
    Ff = np.fft.rfft(f, fft_len)
    Fg = np.fft.rfft(g, fft_len)
    Fh = Ff * Fg
    h = np.fft.irfft(Fh, fft_len)
    h = np.rint(h).astype(np.int64)
    return h[:len(f) + len(g) - 1]