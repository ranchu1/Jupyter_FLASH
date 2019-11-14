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
def plot_FLASH_Yahil_vs_Analytical\
      ( Gravitational_constant, second, kilometer, light_speed, \
       collapse_time, kappa, gamma, radius, X1D, D1D, V1D, M1D, \
       time, time_a, radius_1dx, dens_1dx, velx_1dx ):
  
  import numpy as np
  import matplotlib.pyplot as plt

  fig, axs = plt.subplots(1,2, figsize=(12, 6), dpi= 160, facecolor='w', edgecolor='k')
  fig.subplots_adjust(hspace = 2.5, wspace= 0.4) # (hspace = .5, wspace=.001)

  axs = axs.ravel()

  test_time = [collapse_time - time_a* second]

  for mt in test_time:
    dimensionless_X = pow(kappa,-1/2) * pow(Gravitational_constant,(gamma-1)/2) \
    * radius * pow(mt,gamma-2)
    D_interp = np.interp(dimensionless_X, X1D, D1D)
    V_interp = np.interp(dimensionless_X, X1D, V1D)
    M_interp = np.interp(dimensionless_X, X1D, M1D)

    D = pow(Gravitational_constant,-1) * pow(mt,-2) * D_interp
    V = pow(kappa,1/2) * pow(Gravitational_constant,(1-gamma)/2) \
    * pow(mt,1-gamma) * V_interp
    
    ax1 = plt.subplot(121)
    plt.loglog(radius/kilometer, D,label='a-%.1f'%(mt*1e3)+' ms')
    plt.loglog(radius_1dx/kilometer, dens_1dx,'--.',\
               label='c-%.1f'%(150-time*1e3)+' ms')
    
    ax2 = plt.subplot(122)
    plt.semilogx(radius/kilometer,V/light_speed)
    plt.semilogx(radius_1dx/kilometer, velx_1dx/light_speed,'--.')

    
  ax1 = plt.subplot(121)
  plt.legend(loc='best')
  plt.xlim((1e-1, 1e5))
  plt.ylim((1e1, 1e15))
  plt.xlabel('Radius [km]',fontsize=16)
  plt.ylabel('Mass Density [g/cm3]',fontsize=16)
  ax1.tick_params(direction='out', length=6, width=2, colors='k',
                grid_color='k', grid_alpha=0.5,labelsize = 12)
    
  ax2 = plt.subplot(122)
  plt.xlim((1e-1, 1e5))
  plt.ylim((-0.15, 0.1))
  plt.xlabel('Radius [km]',fontsize=16)
  plt.ylabel('Velocity [c]',fontsize=16)
  ax2.tick_params(direction='out', length=6, width=2, colors='k',
                grid_color='k', grid_alpha=0.5,labelsize = 12)


  plt.subplots_adjust(bottom=0.25, top=0.75)
    
  return(fig)