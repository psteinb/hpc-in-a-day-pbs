#/usr/bin/env python3

from mpi4py import MPI

def print_hostname():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    hname = MPI.Get_processor_name()

    print("this is %2i/%2i running on %s" % (rank+1,size,hname))

    comm.Barrier()


if __name__ == '__main__':

    print_hostname()
