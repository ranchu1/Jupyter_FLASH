def scale_FLASH_2DCylindrical( var ):
  import numpy as np
 
  var_1D = np.zeros(len(var[:,0,0,0]))
  #print('var    shape ', var.shape)

  for ii in range(0,len(var_1D)):
    kk = 0;
    for i in range(0,len(var[0,:,0,0])):
      for j in range(0,len(var[0,0,:,0])):
        for k in range(0,len(var[0,0,0,:])):
          var_1D[ii] = var_1D[ii] + var[ii,i,j,k]
          kk = kk + 1
          #print('var_1D[ii]',var_1D[ii],kk)
    var_1D[ii] =  var_1D[ii] / kk
    #print('var_1D[ii]', ii, var_1D[ii])

  #print('var_1D shape ', var_1D.shape)

  return( var_1D )

# ---------------------------------------
def scale_FLASH_2DCylindrical_Coordinate( var ):
  import numpy as np

  r = np.square(var[:,0]) + np.square(var[:,1])
  r = np.sqrt( r )
 
  return( r )

# ---------------------------------------
