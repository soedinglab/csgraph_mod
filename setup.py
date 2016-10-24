import os

from setuptools import setup, Extension, find_packages

try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False


__NAME__ = "csgraph_mod"
__VERSION__ = "0.0.2"
__AUTHOR__ = "Christian Roth"
__AUTHOR_EMAIL__ = "christian.roth@mpibpc.mpg.de"
__DESCRIPTION__ = "An implementation of an efficient interval tree in python."
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
    test_suite="nose.collector"
)