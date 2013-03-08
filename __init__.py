# -*- coding: utf-8 -*-
"""
    __init__.py

    This file register model to tryton

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""

from trytond.pool import Pool
from .attendance import *

def register():
    Pool.register(
        Attendance,
        module='payroll', type_='model')
