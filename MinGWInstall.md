Installation Guide for netCDF-0.8.2 on MinGW (32-bit XP SP3)

# Introduction #

This page is useful only if you are absolutely sure you need to compile and install netCDF4-0.8.2 from its source distribution.

# Details #

Installation Guide for netCDF-0.8.2 on MinGW (32-bit XP SP3)

1. zlib-1.2.3

Nothing is really special about this. In my example, I just typed
```
./configure
make install
```
It will install zlib in /local

2. HDF5-1.8.3-snap2 release

Compile/Install in MSYS
See below the reason for ‘snap2’
Read and fix lines as suggested:
http://www.hdfgroup.org/ftp/HDF5/current/src/unpacked/release_docs/INSTALL_MinGW.txt

Make sure using /bin/make.exe when build and install hdf5 (ref: http://www.redantigua.com/msys-win.html)

Note: export LIBS=”-lws2\_32 –lmsvcr71” should be done instead of export LIBS=”-lws2\_32” as described in the installation note above.

Following is what I did for compilation and installation.
```
./configure --prefix=/c/hdf5 --enable-hl --with-zlib=/local/include,/local/lib
./make
./make install
```
3. netcdf-4.1-beta2.tar.gz

Compile/Install in MSYS
From INSTALL doc in netcdf-4.1-beta2.tar.gz
```
“To use the netCDF-4 features you will also need to have a
HDF5-1.8.3-snap2 release installed. HDF5, in turn, must have been built
with zlib, version 1.2.3 (or better)”
```

Following is what I did for compilation and installation.
```
./configure --with-zlib=/local --enable-netcdf-4 --with-hdf5=/c/hdf5 --prefix=/c/netcdf4
./make
./make install
```
4. netCDF-0.8.2

Compile/Install in XP Command Windows (if you set path properly in MSYS, it may work too):
```
python setup.py build –c mingw32
```

One hard thing to figure out (at least for me) about compiling netCDF-0.8.2 under XP was that somehow the order of library in the call line of gcc affects how it searches libraries (hence, functions). So, it is likely the build command will choke. You will get this
```
error: Command "g++ -mno-cygwin -shared build\temp.win32-2.5\Release\netcdf4.o 
-LC:\netcdf4\lib -LC:\hdf5\lib -LC:\Python25\libs 
-LC:\Python25\PCBuild -Wl,-RC:\netcdf4\lib -Wl,-RC:\hdf5\lib 
-lnetcdf -lhdf5 -lhdf5_hl -lz -lpython25 -lmsvcr71
```
To fix this error, “-lhdf5 –lhdf5\_hl” should be “–lhdf5\_hl  -lhdf5”. To do it, I changed a line in setup.py
```
'libs = ['netcdf','hdf5','hdf5_hl','z']'
to
'libs = ['netcdf','hdf5_hl','hdf5','z']'
```