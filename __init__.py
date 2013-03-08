#-*- coding: utf-8 -*-
#"""
#<<<<<<< HEAD
#    __init__

   # Description goes here...
#=======
#    __init__.py

    #This file register model to tryton
#>>>>>>> 5068a2e36d5ab77e41ad35973b7538408cc8d1ce

 #   :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
  #  :license: BSD, see LICENSE for more details.
#"""
from trytond.pool import Pool
#<<<<<<< HEAD
from .payroll import *
from .employee import *
from .attendance import *

def register():
    Pool.register(
        Payroll, 
	Attendance,
        module='payroll', type_='model')

    Pool.register(
        Employee,
        module='company', type_='model')
#=======
#from .payroll import *
#from .employee import *
#from .attendance import *

#def register():
 #   Pool.register(        
  #      )
#>>>>>>> 5068a2e36d5ab77e41ad35973b7538408cc8d1ce
