**The netcdf4-python project has migrated to [github](https://github.com/Unidata/netcdf4-python). Please go to the github page to create new issues/bug reports.**

netCDF version 4 has many features not found in earlier versions of the library and is implemented on top of HDF5. This module can read and write files in both the new netCDF 4 and the old netCDF 3 format, and can create files that are readable by HDF5 clients. The API modelled after Scientific.IO.NetCDF, and should be familiar to users of that module.

Most new features of netCDF 4 are implemented, such as multiple unlimited dimensions, groups and zlib data compression. All the new numeric data types (such as 64 bit and unsigned integer types) are implemented. Compound and variable length (vlen) data types are supported, but the enum and opaque data types are not. Mixtures of compound and vlen data types (compound types containing vlens, and vlens containing compound types) are not supported.

**Quick Links**:

[Download Source (version 1.0.8 and newer)](https://pypi.python.org/pypi/netCDF4#downloads)

[Download Windows Binaries (version 1.0.8 and newer)](http://www.lfd.uci.edu/~gohlke/pythonlibs/#netcdf4)

[Older Downloads](http://code.google.com/p/netcdf4-python/downloads/list)

**News**:

**20140225**:  The netcdf4-python project has migrated from googlecode to [github](https://github.com/Unidata/netcdf4-python).  The source code repository is now hosted under the [Unidata project](https://github.com/Unidata), along with the netCDF C library.