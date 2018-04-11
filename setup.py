import os

from setuptools import setup, Extension, find_packages
import numpy

try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False


__NAME__ = "csgraph_mod"
__VERSION__ = "0.0.2"
__AUTHOR__ = "Nikolaos Papadopoulos, Johannes Soeding"
__AUTHOR_EMAIL__ = "npapado@mpibpc.mpg.de"
__DESCRIPTION__ = "Modified Dijkstra algorithm from the shortest_path.pyx collection of SciPy"
__LICENSE__ = "BSD"


ext = ".pyx" if USE_CYTHON else ".c"
module_names = [
    "csgraph_mod.shortest_path_mod"
]

extensions = []
for module_name in module_names:
    file_name = module_name.replace(".", os.sep) + ext
    extension = Extension(module_name, [file_name])
    extensions.append(extension)
if USE_CYTHON:
    extensions = cythonize(extensions)

setup(
    name=__NAME__,
    version=__VERSION__,
    author=__AUTHOR__,
    author_email=__AUTHOR_EMAIL__,
    description=__DESCRIPTION__,
    license=__LICENSE__,
    ext_modules=extensions,
    packages=find_packages(),
    include_dirs=[numpy.get_include()],
    test_suite="nose.collector"
)
