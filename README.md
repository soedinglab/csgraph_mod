### `csgraph_mod`

We have modified the implementation of Dijkstra's algorithm contained in the [csgraph](https://docs.scipy.org/doc/scipy/reference/sparse.csgraph.html) module for compressed sparse graph routines to return a list of visited nodes. We use this package to help us construct a minimal spanning tree between single-cell transcriptomes. For more information about this, please refer to the [MERLoT manuscript](https://www.biorxiv.org/content/early/2018/02/08/261768).

### Installation

`csgraph_mod` can be installed using the `pip` package manager or any `pip`-compatible package manager:

    git clone https://github.com/soedinglab/csgraph_mod.git
    cd csgraph_mod/
    pip install .

### Dependencies

`csgraph_mod` was developed and tested in [Python 3.5](https://www.python.org/downloads/release/python-350/) and [3.6](https://www.python.org/downloads/release/python-360/). While older Python 3 versions should work, there is no guarantee that they will. Installation requires:

* [`numpy`](www.numpy.org)
* [`scipy`](https://www.scipy.org/)
* [`cython`](http://cython.org/)

### Known problems

#### Missing `numpy` headers

In some cases (especially on Mac computers), the installer may complain that it cannot find some `numpy` headers:

    fatal error: 'numpy/arrayobject.h' file not found

In this case, try exporting the headers yourself. Run `export CFLAGS="-I <python_loc>/site-packages/numpy/core/include $CFLAGS"`, where `<python_loc>` is the directory where python is installed - something like `/usr/local/lib/python3.6`.