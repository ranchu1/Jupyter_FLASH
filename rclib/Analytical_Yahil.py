def analytical_yahil_k_r_g( kappa, rho, gamma ):
    import numpy as np
    
    pres = np.zeros(len(rho))
    pres = kappa * rho ** gamma
    
    return( pres )

# -----------------NOT FINISHED --------------------
def analytical_yahil_k_r_g_t( kappa, radius, gamma, mTime ):
    import numpy as np
    
    G = 1.0
    X = pow(kappa,-1/2) * pow(G,(gamma-1)/2) * radius * pow(mTime,gamma-2)
    
    #return( rho, velocity, mass, energy, pres )

# -----------------------------------------