def IO_WeakLib_EOS():
   print("hello from IO.IO_WeakLib_EOS")

def test_FLASH_IO( dir, filename, ID ):
  import h5py
  import numpy as np
  import matplotlib.pyplot as plt
  import time

  FileName = dir+filename+str(ID).zfill(4)
  print( 'filename =', FileName )
  f = h5py.File(FileName, 'r')
  
  real_scalars = f['real scalars']
  time = real_scalars[0][1]
  block_size = f['block size']
  coordinates = f['coordinates']
  bounding_box = f['bounding box']
  velx = f['velx']
  vely = f['vely']
  velz = f['velz']
  # Assume 2DCylindrical or Cartesian
  veltot = np.square(velx) + np.square(vely) \
           + np.square(velz)
  veltot = np.sqrt( veltot )

  dens = f['dens']
  dena = f['dena']
  prsa = f['prsa']
  pres = f['pres']
  
  
  return( time, block_size, coordinates, bounding_box, \
  veltot, dens, dena, pres, prsa )
