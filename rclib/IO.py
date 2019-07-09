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
  veltot = velx
  dens = f['dens']
  dena = f['dena']
  prsa = f['prsa']
  pres = f['pres']
  
  return( block_size, coordinates, bounding_box, \
  veltot, dens, dena, pres, prsa )
