from pypcl import PCDReader
from tqdm import tqdm
import numpy as np


if __name__ == "__main__":
    reader = PCDReader()
    reader.read("data/0000.pcd")

    # load
    x = reader.get_x()
    y = reader.get_y()
    z = reader.get_z()
    intensity = reader.get_intensity()
    timestamp = reader.get_timestamp()
    ring = reader.get_ring()

    # cast to numpy array
    x = np.array(x, dtype=np.float32)
    y = np.array(y, dtype=np.float32)
    z = np.array(z, dtype=np.float32)
    intensity = np.array(intensity, dtype=np.float32)
    timestamp = np.array(timestamp, dtype=np.float64)
    ring = np.array(ring, dtype=np.uint8)

    np.savez_compressed("data/0000.npz", x=x, y=y, z=z, intensity=intensity, timestamp=timestamp, ring=ring)
