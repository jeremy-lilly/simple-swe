import numpy as np
import torch as tn


def calc_compression(tt):
    entries = sum([tn.numel(core) for core in tt.cores])
    compression = entries / np.prod(np.array(tt.N))

    return compression, entries
# END calc_compression()
