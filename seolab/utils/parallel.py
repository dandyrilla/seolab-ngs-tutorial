from multiprocessing import Pool, cpu_count


def starmap(func, args, ncpus=None):
    if ncpus is None:
        ncpus = cpu_count()
    with Pool(ncpus) as pool:
        ret = pool.starmap(func, args)
    return ret
