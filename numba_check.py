#!/usr/bin/env python

import numba.cuda
numba.cuda.api.detect()
numba.cuda.cudadrv.libs.test()
