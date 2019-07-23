# ------------------------------------------------------------
def IO_YahilProfile( filename ):
   import numpy as np

   dir = 'YahilProfile/'
   FileName = dir+filename
   print('Using', FileName)
    
   with open(FileName) as f:
    temp_X = [line.split()[0] for line in f] 
   with open(FileName) as f:
    temp_D = [line.split()[1] for line in f] 
   with open(FileName) as f:
    temp_V = [line.split()[2] for line in f] 
   with open(FileName) as f:
    temp_M = [line.split()[3] for line in f] 
    
   X = [float(i) for i in temp_X[1:len(temp_X)]]
   D = [float(i) for i in temp_D[1:len(temp_D)]]
   V = [float(i) for i in temp_V[1:len(temp_V)]]
   M = [float(i) for i in temp_M[1:len(temp_M)]]
    
   return( X, D, V, M )

# ------------------------------------------------------------
def test_FLASH_IO_2D( dir, filename, ID ):
  import h5py
  import numpy as np
  import matplotlib.pyplot as plt
  import time

  ## open file
  FileName = dir+filename+str(ID).zfill(4)
  print( 'filename =', FileName )
  f = h5py.File(FileName, 'r')
  
  ## read time
  real_scalars = f['real scalars']
  time = real_scalars[0][1]
  print( 'time =', time ,' s')

  ## read geometry
  string_scalars = f['string scalars']
  geometry = string_scalars[0][1] 
    
  if geometry[0:11] != b'cylindrical' :
    print('geometry:', geometry[0:11])
    print('!----------------------------!')
    print('Warning: NOT Cylindrical Data!')
    print('!----------------------------!')
    
  ## read coordinates and block size
  block_size = f['block size']
  coordinates = f['coordinates']
  bounding_box = f['bounding box']
    
  ## read variables
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
def FLASH_IO_1D( dir, filename, ID, Verbose ):
  # used for 1D in X direction only
  import h5py
  import numpy as np
  import matplotlib.pyplot as plt
  import time

  ## open file
  FileName = dir+filename+str(ID).zfill(4)
  print( 'filename =', FileName )
  f = h5py.File(FileName, 'r')
    
  ## read time
  real_scalars = f['real scalars']
  time = real_scalars[0][1]
  print( 'time =', time ,' s')
    
  ## read geometry
  string_scalars = f['string scalars']
  geometry = string_scalars[0][1] 

  ## read variables
  unknown_names = f['unknown names']
  if Verbose == 'describe':
    print( 'geometry =', geometry )
    for ii in range(len(unknown_names)):
      print( 'name =', unknown_names[ii] )
    print( 'unknown names:', unknown_names )

  ## read runtime
  integer_runtime = f['integer runtime parameters']
  gr_titleszex = integer_runtime[57][1]

  ## read block numbers and parameters
  integer_scalars = f['integer scalars']
  nxb = integer_scalars[0][1]

  nxb = 1

  nyb = integer_scalars[1][1]
  nzb = integer_scalars[2][1]
  ndim = integer_scalars[3][1]
  if Verbose == 'describe':
    print( 'gr_titleszex',gr_titleszex )
    print( '[nxb, nyb, nzb] = [',nxb, nyb, nzb,']' )
  block_size = f['block size']

  ## read coordinates [x,y,z] and variables
  coordinates = f['coordinates']
  bounding_box = f['bounding box']

  velx = f['velx']
  vely = f['vely']
  velz = f['velz']

  dens = f['dens']
  dena = f['dena']
  prsa = f['prsa']
  pres = f['pres']
    
  ## converting coordinates and variables to 1D array
  radius = np.zeros([nxb*len(coordinates[:,0])])
  print( 'variable.shape = grid(', len(coordinates[:,0]),') * sub(',\
          nxb*nyb*nzb,') = ', radius.shape)
  
  dens_1dx = np.zeros([nxb*len(coordinates[:,0])])
  velx_1dx = np.zeros([nxb*len(coordinates[:,0])])
  
  for ii in range(len(coordinates[:,0])):
    for jj in range(nxb):
      kk = jj + ii * nxb
      radius[kk] = coordinates[ii,0] + block_size[ii,0]*jj/nxb
      dens_1dx[kk] = dens[ii,0,0,jj]
      velx_1dx[kk] = velx[ii,0,0,jj]
  
  ## sort coordinates and variables
  rank_1d = np.argsort(radius)
  radius_sort = np.zeros([len(radius)])
  dens1d_sort = np.zeros([len(radius)])
  velx1d_sort = np.zeros([len(radius)])
  
  for kk in range(len(dens_1dx)):
    radius_sort[kk] = radius[rank_1d[kk]]
    dens1d_sort[kk] = dens_1dx[rank_1d[kk]]
    velx1d_sort[kk] = velx_1dx[rank_1d[kk]]
    
  return( time, radius_sort, dens1d_sort, velx1d_sort )

# ------------------------------------------------------------