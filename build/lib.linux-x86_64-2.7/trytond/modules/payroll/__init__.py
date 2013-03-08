# -*- coding: utf-8 -*-
"""
    __init__

    Description goes here...

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool
from payroll import *
from employee import *
from attendance import *

def register():
    Pool.register(
        Payroll, 
        module='payroll', type_='model')
