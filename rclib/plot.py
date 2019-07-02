def test_matrixplot():
  import numpy as np
  import matplotlib.pyplot as plt
  
  alpha = ['ABC', 'DEF', 'GHI', 'JKL']
  
  data = np.random.random((4,4))
  
  fig = plt.figure()
  ax = fig.add_subplot(111)
  cax = ax.matshow(data, interpolation='nearest')
  fig.colorbar(cax)
  
  ax.set_xticklabels(['']+alpha)
  ax.set_yticklabels(['']+alpha)
  
  plt.show()
  
  return

# ---------------------------------------
def plot_1Dline(x, y):
  import matplotlib.pyplot as plt

  fig = plt.figure()
  plt.plot(x, y)
  plt.show()
  
  return

# ---------------------------------------
def plot_1Ddot(x, y):
  import matplotlib.pyplot as plt

  fig = plt.figure()
  plt.plot(x, y, '.')
 # plt.gca().set_aspect('equal', adjustable='box')
  plt.xlabel('x axis')
  plt.ylabel('y axis')
  plt.show()

  return

# ---------------------------------------
def test_FLASHplot( filename ):
  import h5py
  import numpy as np
  import math
  import matplotlib.pyplot as plt
  import time

  #filename = 'wl-EOS-SFHo-25-40-100.h5'
  print( 'filename =',filename )
  f = h5py.File(filename, 'r')
  velx = f['velx']
  vely = f['vely']
  velz = f['velz']
  #veltot = math.pow(velx,2) + math.pow(vely,2) + math.pow(velz,2)
  #veltot = math.sqrt( veltot )
  veltot = velx
  dens = f['dens']
  pres = f['pres']
  
  return( veltot, dens, pres )

# ---------------------------------------
def plot_point2point( x1, x2, y1, y2 ):
  import matplotlib.pyplot as plt

  for i in range(0, len(x1)):
    plt.plot( [x1[i], x2[i]], [y1[i], y2[i]], 'bo-')
  
  plt.show()
  
  return
  
# ---------------------------------------
def plot_Grid2D( x1, x2, y1, y2 ):
  import matplotlib.pyplot as plt
 
  for i in range(0,len(x1)):
    plt.plot( [x1[i], x2[i]], [y1[i], y1[i]], 'b-', linewidth=1.0, alpha=0.7 )
    plt.plot( [x2[i], x2[i]], [y1[i], y2[i]], 'b-', linewidth=1.0, alpha=0.7 )
    plt.plot( [x1[i], x2[i]], [y2[i], y2[i]], 'b-', linewidth=1.0, alpha=0.7 )
    plt.plot( [x1[i], x1[i]], [y1[i], y2[i]], 'b-', linewidth=1.0, alpha=0.7 )

  plt.gca().set_aspect('equal', adjustable='box')
  plt.xlabel('x axis')
  plt.ylabel('y axis')
  plt.show()

  return

# ---------------------------------------
def plot_FLASHGrid2D( bounding_boundary ):
  import matplotlib.pyplot as plt

  x1 = bounding_boundary[:,0,0]
  x2 = bounding_boundary[:,0,1]
  y1 = bounding_boundary[:,1,0]
  y2 = bounding_boundary[:,1,1]

  plot_Grid2D( x1, x2, y1, y2 ) # function in this module

  plt.figure(num=None, figsize=(16,12), dpi=160, facecolor='w', edgecolor='k')

  #plt.show()
  return

# ---------------------------------------
def plot_FLASHVariable_2DCylindrical\
      ( coordinates, variable ):
  import matplotlib.pyplot as plt
  import numpy as np
  import rclib.Scale as rcscale 

  r = np.square(coordinates[:,0]) + np.square(coordinates[:,1])
  r = np.sqrt( r )

  plot_arr = np.zeros(len(r))

  plot_arr = rcscale.scale_FLASH_2DCylindrical( variable )
 
  plt.plot(r,plot_arr,'b.')
  #plt.gca().set_aspect('equal', adjustable='box')
  plt.xlabel('r')
  plt.ylabel('variable')
  plt.show()

  return
 
# ---------------------------------------
