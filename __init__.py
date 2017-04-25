##########################################################################
#  This file is part of the deModel library, a Python package for using
#  Python to model fixed point arithmetic algorithms.
#
#  Copyright (C) 2007 Dillon Engineering, Inc.
#  http://www.dilloneng.com
#
#  The deModel library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public License as
#  published by the Free Software Foundation; either version 2.1 of the
#  License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library. 
#  If not, see <http://www.gnu.org/licenses/>
##########################################################################
""" Dillon Engineering Logic modelling class

Provided class:
  - DeFixedInt

Provided functions:
  - arrayFixedInt

"""

__author__ = "$Author: guenter $"
__revision__ = "$Revision: 395 $"
__version__ = "0.2"


from _fixedInt import DeFixedInt
from _fixedInt import DeFixedIntOverflowError
from _fixedInt import arrayFixedInt

__all__ = [ "arrayFixedInt",
            "DeFixedInt", 
            "DeFixedIntOverflowError"]
