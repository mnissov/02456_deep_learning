import numpy as np

def probability_matrix( data ):
    x = np.array(data.pickup_zone)
    y = np.array(data.dropoff_zone)
    
    num_zones = max(x)+1
    count_mat = np.zeros((num_zones,num_zones), dtype=np.uint)
    for i in range(len(x)):
        idx = x[i]
        idy = y[i]
        count_mat[idx, idy] += 1
    norm_factor = np.sum(count_mat,axis=1)
    norm_factor = norm_factor + (norm_factor==0)
    
    prob_mat = count_mat.T/norm_factor
    return prob_mat.T
def count_matrix( data ):
    x = np.array(data.pickup_zone)
    y = np.array(data.dropoff_zone)
    
    num_zones = max(x)+1
    count_mat = np.zeros((num_zones,num_zones), dtype=np.uint)
    for i in range(len(x)):
        idx = int(x[i])
        idy = int(y[i])
        count_mat[idx, idy] += 1
    
    return count_mat
