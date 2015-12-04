Read on for instructions on how to install netcdf4-python on an Ubuntu Jaunty machine. The same instructions should work as well on previous versions.

# Installing the required dependencies #

There are only two dependencies to install, HDF5 (>=1.8.2) and netCDF4. The version of HDF5 shipped with Karmic is 1.6.6, so you'll need to compile from source. Lucid will ship with 1.8.3 so that won't be necessary, but until then, read on.

## HDF5 ##

  1. Download the current [HDF5 source release](http://www.hdfgroup.org/ftp/HDF5/current/src/).
  1. Unpack, go into the directory and execute:
```
./configure --prefix=/usr/local --enable-shared --enable-hl
make 
sudo make install
```

To speed things up, compile on more than one processor using
```
make -j n 
```
where n is the number of processes to be launched.

## netCDF4 ##

  1. Download the current [netCDF4 source release](ftp://ftp.unidata.ucar.edu/pub/netcdf/).
  1. Unpack, go into the directory and execute:
```
LDFLAGS=-L/usr/local/lib CPPFLAGS=-I/usr/local/include ./configure --enable-netcdf-4 --enable-dap --enable-shared --prefix=/usr/local
make 
make install
```


# Installing netcdf4-python #
When both HDF5 and netCDF4 are in /usr/local, make sure the linker will be able to find those libraries by executing
```
sudo ldconfig
```
then installing netcdf4-python is just a matter of doing
```
python setup.py install
```