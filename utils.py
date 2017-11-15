from multiprocessing.dummy import Pool as ThreadPool

def multi_process(func, data, num_thread):
    pool = ThreadPool(num_thread)
    result = pool.map(func, data)
    pool.close()
    pool.join()
    return result

def open_line(f):
    with open(f) as tmps:
        content = tmps.readlines()
    content = [x.strip() for x in content]
    return content
