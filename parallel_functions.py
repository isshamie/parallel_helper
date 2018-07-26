def multi_run_wrapper(args):
    curr_func = args[0]
    return curr_func(args[1], *args[2])


def parallel_ar(ar, func, func_args=(), num_processes=4):
    '''
    Function to parallelize a function that operates on each row in the array

    Input: 
    ar: Numpy array
    func: Function that is essentially the same uses a for loop the same way you would call it without a for loop. 
          i.e do not write this function as operating on one element in your array. 
          Also, the function should either return: a) a numpy array OR b) None. 
    func_args: Arguments that would be used by each element in the array
    num_processes: Number of parallel processes to run

    Returns:
    new_x: if func returns an array then this is a numpy array with all the elements returned
    OR None if func returns None and just does some calling.
    '''

    import pandas as pd
    import multiprocessing
    import itertools
    import numpy as np

    # calculate the chunk size as an integer
    chunk_size = int(ar.shape[0] / num_processes)

    # will work even if the length of the dataframe is not evenly divisible by num_processes
    chunks = [ar[i:i + chunk_size] for i in range(0, ar.shape[0], chunk_size)]

    # create our pool with `num_processes` processes
    pool = multiprocessing.Pool(processes=num_processes)

    # apply our function to each chunk in the list
    result = pool.map(multi_run_wrapper, zip(itertools.repeat(func), chunks, itertools.repeat(func_args)))

    if result[0] is None:
        return

    
    #new_x = np.zeros(result[0].shape)
    #new_x = np.array()

    new_x = np.vstack(result).flatten() #Flatten out the results
    # for i in result:
    #     new_x = new_x + i

    pool.terminate()
    return new_x, result


def parallel_df(df, func, func_args=(), num_processes=4):
    '''
    Function to parallelize a function that loops over dataframe rows

    '''
    import pandas as pd
    import multiprocessing
    import itertools

    # calculate the chunk size as an integer
    chunk_size = int(df.shape[0] / num_processes)

    # will work even if the length of the dataframe is not evenly divisible by num_processes
    chunks = [df.loc[df.index[i:i + chunk_size]] for i in range(0, df.shape[0], chunk_size)]

    # create our pool with `num_processes` processes
    pool = multiprocessing.Pool(processes=num_processes)

    # apply our function to each chunk in the list
    result = pool.map(multi_run_wrapper, itertools.izip(itertools.repeat(func), chunks, itertools.repeat(func_args)))

    # print result[0]

    new_df = pd.DataFrame()
    for i in result:
        # since i is just a dataframe
        # we can reassign the original dataframe based on the index of each chunk
        new_df = new_df.append(i)
        # print df.loc[result[i].index,:]
        # df.loc[result[i].index,:] = result[i]
    pool.terminate()
    return new_df
