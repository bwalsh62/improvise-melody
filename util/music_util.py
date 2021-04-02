# -*- coding: utf-8 -*-
"""

By Ben Walsh \
For Liloquy

(C) 2021 Ben Walsh <ben@liloquy.io>

Created on Fri Apr  2 13:30:20 2021

"""

#%% Import libraries

import numpy as np
import os
from pygame import mixer

#%% Define mapping from note to frequency (Hz)
note_to_freq = {
        'D2': 73.42,
        'E2': 82.41,
        'F2': 87.31,
        'G2': 98.00,
        'A2': 110.00,
        'B2': 123.47,
        'C3': 130.81,
        'D3': 146.83,
        'E3': 164.81,
        'F3': 174.61,
        'G3': 196.00,
        'A3': 220.00,
        'B3': 246.94,
        'C4': 261.63,
        'C#4': 277.187,
        'D4': 293.66,
        'D#4': 311.13,
        'E4': 329.63,
        'F4': 349.23,
        'F#4': 370.00,
        'G4': 392.00,
        'G#4': 415.312,
        'A4': 440.00,
        'A#4': 466.172,
        'B4': 493.88,
        'C5': 523.25,
        'D5': 587.33,
        'E5': 659.25,
        'F5': 698.46,
        'G5': 783.99
}

#%% Define saved notes

mixer.init()

MUSIC_FPATH = r"C:\Users\benja\OneDrive\Documents\Python\liloquy-git\piano-gui\music_files\piano"

note_to_sound = {}
LIB_NOTES = ('C4',
             'Db4', 
             'D4', 
             'Eb4', 
             'E4', 
             'F4', 
             'Gb4', 
             'G4', 
             'Ab4',
             'A4', 
             'Bb4',
             'B4')

for lib_note in LIB_NOTES:
    lib_note_path = os.path.join(MUSIC_FPATH,"Piano_{}_2p4s.wav".format(lib_note))
    if os.path.exists(lib_note_path):
        note_to_sound[lib_note] = mixer.Sound(lib_note_path)
    else:
        print("{} does not exist".format(lib_note_path))

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

#%% Class to define notes to playback with associated metadata

class Note:
    
    fs = 44100  # Sampling frequency in Hz
    
    def __init__(self, note, instr='piano'):        
        #self.f0 = f0 # frequency in Hz
        self.note = note # Example C4
        self.f0 = note_to_freq[note]
        self.instr = instr
        self.sound = note_to_sound[note]
