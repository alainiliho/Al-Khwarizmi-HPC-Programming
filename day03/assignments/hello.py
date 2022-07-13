if __name__ =="__main__":
    from pyccel.stdlib.internal.openmp import(
        omp_get_num_threads, omp_get_thread_num,
        omp_in_parallel, omp_set_num_threads
    )
    #$omp parallel
    
    rank = omp_get_thread_num(), omp_get_num_threads()
    print("Hello from the rank ",rank[0] , "thread")
    
    #$omp end parallel
    
    print("Parallel execution of hello_world with",rank[1] ,"threads")
