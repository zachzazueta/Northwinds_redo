def get_sample(data):
    import numpy as np
    sample = np.random.choice(data,30)
    return sample
    
def get_sample_mean(data):
    sample_means = []
    for i in range(100):
        sample_means.append(get_sample(data).mean())
    return sample_means

def cohens_d(sample1,sample2):
    from numpy import std, mean, sqrt
    n1 = len(sample1)
    n2 = len(sample2)
    deg_freed = n1 + n2 - 2
    return abs(mean(sample1) - mean(sample2)) / sqrt(((n1 - 1) * std(sample1, ddof=1) **2 + (n2 - 1) * std(sample2, ddof=1) **2) / deg_freed)