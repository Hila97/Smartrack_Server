def eqsc(X, K=None, G=None):
    "equal-size clustering based on data exchanges between pairs of clusters"
    import numpy
    from scipy.spatial.distance import pdist, squareform  
    
    def error(K, m, D):
        """return average distances between data in one cluster, averaged over all clusters"""
        E = 0
        for k in range(K):
            i = numpy.where(m == k)[0] # indeces of datapoints belonging to class k
            E += numpy.mean(D[numpy.meshgrid(i,i)])
        return E / K
    numpy.random.seed(0) # repeatability
    N, n = X.shape
    if G is None and K is not None:
        G = N // K # group size
    elif K is None and G is not None:
        K = N // G # number of clusters
    else:
        raise Exception('must specify either K or G')
    D = squareform(pdist(X)) # distance matrix
    m = numpy.random.permutation(N) % K # initial membership
    E = error(K, m, D)
    t = 1
    while True:
        E_p = E
        for a in range(N): # systematically
            for b in range(a):
                m[a], m[b] = m[b], m[a] # exchange membership
                E_t = error(K, m, D)
                if E_t < E:
                    E = E_t
                else:
                    m[a], m[b] = m[b], m[a] # put them back
        if E_p == E:
            break
        t += 1           
    print(m)

import numpy
if __name__ == "__main__":
    # X=numpy.array([[32.4914493,34.89074859999999], [31.7721506,35.2040939],[31.8314244,35.2412881],[32.11383,34.8052563],[32.50455,35.450691],[31.7766348,34.6637991],[31.794795,35.127566],[32.100744,34.807026],[32.0482747,34.8242569]])
    X=numpy.array([[32.106497,34.81188100000001],[32.0747169,34.79148800000001],[32.0962934,34.7726703],[51.5478302,-0.1512823],[51.5061267,0.0170173],[51.5763589,-0.2236956],[34.008576,-118.498101],[34.13696960000001,-118.3541763],[34.13869049999999,-118.35644]])
    eqsc(X, G=3)