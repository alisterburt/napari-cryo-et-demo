import mrcfile
import napari
import numpy as np
import starfile
from scipy.spatial.transform import Rotation as R

# files containing data
tomogram_file = 'hiv/01_10.00Apx.mrc'
particles_file = 'hiv/01_10.00Apx_particles.star'

# loading data into memory
# tomogram is a numpy array containing image array data
# df is a pandas DataFrame containing table of info from STAR file
with mrcfile.open(tomogram_file) as mrc:
    tomogram = mrc.data.copy()
df = starfile.read(particles_file)

# get particle positions as (n, 3) numpy array from DataFrame
xyz = df[['rlnCoordinateX', 'rlnCoordinateY', 'rlnCoordinateZ']].to_numpy()

# get particle orientations as Euler angles from DataFrame
euler_angles = df[['rlnAngleRot', 'rlnAngleTilt', 'rlnAnglePsi']].to_numpy()

# turn Euler angles into a scipy 'Rotation' object, rotate Z vectors to see
# where they point for the aligned particle
rotations = R.from_euler(seq='ZYZ', angles=euler_angles, degrees=True).inv()
rotated_z_vectors = rotations.apply([0, 0, 1])


# instantiate a napari viewer
viewer = napari.Viewer(ndisplay=3)

# set up napari vectors layer data
# (n, 2, 3) array
# dim 0: batch dimension
# dim 1: first row is start point of vector, second is direction vector
# dim 2: components of direction vector e.g. (x, y, z)
vectors = np.zeros((rotated_z_vectors.shape[0], 2, 3))

# set vectors data
vectors[:, 0, :] = xyz[:, ::-1]
vectors[:, 1, :] = rotated_z_vectors[:, ::-1]

# add data to viewer
viewer.add_image(tomogram, blending='translucent_no_depth', colormap='gray_r')
viewer.add_points(xyz[:, ::-1], face_color='cornflowerblue', size=10)
viewer.add_vectors(vectors, length=10, edge_color='orange')

# this line is required for the GUI window to be kept open when running
# napari from a script
napari.run()
