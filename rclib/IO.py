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
    
   X = np.asarray([float(i) for i in temp_X[1:len(temp_X)]])
   D = np.asarray([float(i) for i in temp_D[1:len(temp_D)]])
   V = np.asarray([float(i) for i in temp_V[1:len(temp_V)]])
   M = np.asarray([float(i) for i in temp_M[1:len(temp_M)]])
    
   return( X, D, V, M )

# ------------------------------------------------------------
def IO_VisitCurve( filename ):
   import numpy as np

   FileName = filename
   print('Using', FileName)
    
   with open(FileName) as f:
    temp_R = [line.split()[0] for line in f] 
   with open(FileName) as f:
    temp_D = [line.split()[1] for line in f] 
    
   R = np.asarray([float(i) for i in temp_R[0:len(temp_R)]])
   D = np.asarray([float(i) for i in temp_D[0:len(temp_D)]])
    
   return( R, D)
# ------------------------------------------------------------
def FLASH_IO_1D( dir, filename, ID, filefollowindex, Verbose ):
  # used for 1D in X direction only
  import h5py
  import numpy as np
  import matplotlib.pyplot as plt
  import time

  ## open file
  FileName = dir+filename+str(ID).zfill(4)+filefollowindex
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
  nyb = integer_scalars[1][1]
  nzb = integer_scalars[2][1]
  ndim = integer_scalars[3][1]
  global_block = integer_scalars[4][1]
  if Verbose == 'describe':
    print( 'gr_titleszex',gr_titleszex )
    print( '[nxb, nyb, nzb] = [',nxb, nyb, nzb,']' )
  block_size = f['block size']

  gsurr_blks = f['gsurr_blks']
  which_child = f['which child']
 
  ## count how many meaningful blocks
  blk_count = 0
  for ii in range(len(which_child[:])):
    if (gsurr_blks[ii,0,0,1,1] == 1 ):
        blk_count = blk_count + 1

  ## read coordinates [x,y,z] and variables
  coordinates = f['coordinates']
  bounding_box = f['bounding box']
  refine_level = f['refine level']

  velx = f['velx']
  vely = f['vely']
  velz = f['velz']

  dens = f['dens']
  pres = f['pres']
    
  ## converting coordinates and variables to 1D array
  print( 'variable.shape = global_block(', global_block,') * sub(',\
          nxb*nyb*nzb,') ')
  print( 'output variable.shape = meaningful block(', blk_count,') * sub(',\
          nxb*nyb*nzb,')')

  radius = np.zeros(nxb*blk_count)
  dens_1dx = np.zeros(nxb*blk_count)
  velx_1dx = np.zeros(nxb*blk_count)
  
  ii_count = -1
  for ii in range(global_block):
    if (gsurr_blks[ii,0,0,1,1] == 1):
        ii_count = ii_count + 1
        for jj in range(nxb): # over subcell [8]
            kk = jj + ii_count * nxb
            dsubcell = block_size[ii,0]/nxb
            radius[kk] = bounding_box[ii,0,0] + dsubcell * (jj+0.5)
            dens_1dx[kk] = dens[ii,0,0,jj]
            velx_1dx[kk] = velx[ii,0,0,jj]
            
    
  ### sort coordinates and variables
  #rank_1d = np.argsort(radius)
  #radius_sort = np.zeros([len(radius)])
  #dens1d_sort = np.zeros([len(radius)])
  #velx1d_sort = np.zeros([len(radius)])
  
  #for kk in range(len(dens_1dx)):
  #  radius_sort[kk] = radius[rank_1d[kk]]
  #  dens1d_sort[kk] = dens_1dx[rank_1d[kk]]
  #  velx1d_sort[kk] = velx_1dx[rank_1d[kk]]
   
  return( time, radius, dens_1dx, velx_1dx )
