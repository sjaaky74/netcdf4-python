import unittest, os, tempfile
import numpy as np
from numpy.random.mtrand import uniform 
from numpy.testing import assert_array_equal, assert_array_almost_equal
import netCDF4

# rudimentary test of diskless file capability.

# create an n1dim by n2dim by n3dim random array
n1dim = 10
n2dim = 73 
n3dim = 144
ranarr = 100.*uniform(size=(n1dim,n2dim,n3dim))
FILE_NAME = tempfile.mktemp(".nc")

class DisklessTestCase(unittest.TestCase):

    def setUp(self):
        self.file = FILE_NAME
        f = netCDF4.Dataset(self.file,'w',diskless=True)
        self.f = f
        # foo has a single unlimited dimension
        f.createDimension('n1', n1dim)
        f.createDimension('n2', n2dim)
        f.createDimension('n3', n3dim)
        foo = f.createVariable('data1', ranarr.dtype.str[1:], ('n1','n2','n3'))
        # write some data to it.
        foo[0:n1dim-1] = ranarr[:-1,:,:]
        foo[n1dim-1] = ranarr[-1,:,:]
        # bar has 2 unlimited dimensions
        f.createDimension('n4', None)
        # write some data to it.
        bar = f.createVariable('data2', ranarr.dtype.str[1:], ('n1','n2','n4'))
        bar[0:n1dim,:, 0:n3dim] = 2.0

    def tearDown(self):
        self.f.close()

    def runTest(self):
        """testing diskless file capability"""
        foo = self.f.variables['data1']
        bar = self.f.variables['data2']
        # check shape.
        self.assert_(foo.shape == (n1dim,n2dim,n3dim))
        self.assert_(bar.shape == (n1dim,n2dim,n3dim))
        # check data.
        assert_array_almost_equal(foo[:], ranarr)
        assert_array_almost_equal(bar[:,:,:], 2.*np.ones((n1dim,n2dim,n3dim),ranarr.dtype))
        # file does not actually exist on disk
        assert(os.path.isfile(self.file)==False)

if __name__ == '__main__':
    unittest.main()
