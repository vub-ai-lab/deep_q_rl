#! /usr/bin/env python
"""
Execute a training run of deep-Q-Leaning with parameters that
are consistent with:

Playing Atari with Deep Reinforcement Learning
NIPS Deep Learning Workshop 2013

"""

import launcher
import sys

class Defaults:
    # ----------------------
    # Experiment Parameters
    # ----------------------
    STEPS_PER_EPOCH = 50000
    EPOCHS = 100
    STEPS_PER_TEST = 50000
    PROGRESS_FREQUENCY = 5000

    # ----------------------
    # ALE Parameters
    # ----------------------
    BASE_ROM_PATH = "../roms/"
    ROM = 'breakout.bin'
    FRAME_SKIP = 4
    REPEAT_ACTION_PROBABILITY = 0
    COLOR_AVERAGING = True

    # ----------------------
    # Agent/Network parameters:
    # ----------------------
    UPDATE_RULE = 'rmsprop'
    BATCH_ACCUMULATOR = 'mean'
    LEARNING_RATE = .0002
    DISCOUNT = .99
    RMS_DECAY = .99 # (Rho)
    RMS_EPSILON = 1e-6
    MOMENTUM = 0
    CLIP_DELTA = 0
    EPSILON_START = 1.0
    EPSILON_MIN = .1
    EPSILON_DECAY = 1000000
    PHI_LENGTH = 4
    UPDATE_FREQUENCY = 4            # Perform training every step
    REPLAY_MEMORY_SIZE = 1000000
    BATCH_SIZE = 32
    NETWORK_TYPE = "nips_cudnn"
    FREEZE_INTERVAL = 2000            # -1
    REPLAY_START_SIZE = 50000
    RESIZE_METHOD = 'scale'           # crop
    RESIZED_WIDTH = 84
    RESIZED_HEIGHT = 84
    DEATH_ENDS_EPISODE = 'true'      # false
    MAX_START_NULLOPS = 10           # 0
    DETERMINISTIC = False
    CUDNN_DETERMINISTIC = False

if __name__ == "__main__":
    launcher.launch(sys.argv[1:], Defaults, __doc__)
