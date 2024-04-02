from pypcl import PCDReader
from tqdm import tqdm

reader = PCDReader()
print(len(reader))
for i in tqdm(range(100)):
    reader.read("data/0000.pcd")

    x = reader.get_x()
    y = reader.get_y()
    z = reader.get_z()
    intensity = reader.get_intensity()
    timestamp = reader.get_timestamp()
    ring = reader.get_ring()
    print(f"{x[i]=}, {y[i]=}, {z[i]=}, {intensity[i]=}, {timestamp[i]=}, {ring[i]=}")

print(reader)
