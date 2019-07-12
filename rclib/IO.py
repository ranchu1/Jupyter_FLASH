def IO_WeakLib_EOS():
   print("hello from IO.IO_WeakLib_EOS")

# ------------------------------------------------------------
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
  print( 'time =', time ,' s')
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

# ------------------------------------------------------------
def test_FLASH_IO_convert2_1D( dir, filename, ID, Verbose ):
  import h5py
  import numpy as np
  import matplotlib.pyplot as plt
  import time

  FileName = dir+filename+str(ID).zfill(4)
  print( 'filename =', FileName )
  f = h5py.File(FileName, 'r')
  
  real_scalars = f['real scalars']
  time = real_scalars[0][1]
  print( 'time =', time ,' s')

  string_scalars = f['string scalars']
  geometry = string_scalars[0][1]
  print( 'geometry =', geometry )  
   
  unknown_names = f['unknown names']
  if Verbose == 'describe':
    for ii in range(len(unknown_names)):
      print( 'name =', unknown_names[ii] )
 #   unknown_var[ii] = f[unknown_names[ii]]
    print( 'unknown names:', unknown_names )

  integer_runtime = f['integer runtime parameters']
  gr_titleszex = integer_runtime[57][1]
  print( 'gr_titleszex',gr_titleszex )

  integer_scalars = f['integer scalars']
  nxb = integer_scalars[0][1]
  nyb = integer_scalars[1][1]
  nzb = integer_scalars[2][1]
  ndim = integer_scalars[3][1]
  ## if Verbose == 'describe':
  print( '[nxb, nyb, nzb] = [',nxb, nyb, nzb,']' )
    
  block_size = f['block size']
  coordinates = f['coordinates']
  bounding_box = f['bounding box']
  coord_fined = np.zeros([nxb*len(coordinates[:,0]),ndim])
  print( 'size coord_fined', coord_fined.shape)

  velx = f['velx']
  vely = f['vely']
  velz = f['velz']

  dens = f['dens']
  dena = f['dena']
  prsa = f['prsa']
  pres = f['pres']
  
  dens_1dx = np.zeros([nxb*len(coordinates[:,0]),ndim])
  velx_1dx = np.zeros([nxb*len(coordinates[:,0]),ndim])
  for ii in range(len(coordinates[:,0])):
    for jj in range(nxb):
      kk = jj + ii * nxb
      coord_fined[kk] = coordinates[ii,0] + block_size[ii,0]*jj/nxb
      dens_1dx[kk] = dens[ii,0,0,jj]
      velx_1dx[kk] = velx[ii,0,0,jj]
  
  return( time, coord_fined, dens_1dx, velx_1dx )

# ------------------------------------------------------------