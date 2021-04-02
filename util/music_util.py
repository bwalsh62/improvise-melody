# -*- coding: utf-8 -*-
"""

By Ben Walsh \
For Liloquy

(C) 2021 Ben Walsh <ben@liloquy.io>

Created on Fri Apr  2 13:30:20 2021

"""

#%% Import libraries

import numpy as np

#%% Generate array of notes based on input note distribution
# Takes optional input melody_len
# Assumes time-independent distributions

def gen_melody_from_distro(distro, melody_len=8):
    
    # Make CDF
    dict_vals = list(distro.values())
    cdf = [dict_vals[0]]
    for val in dict_vals[1:]:
        cdf.append(val + cdf[-1])
    
    generated_melody = []
    for note in range(melody_len):
        generated_melody.append(list(distro.keys())[np.argmax(np.array(cdf) > np.random.rand())])

    return generated_melody
