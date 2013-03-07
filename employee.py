# -*- coding: utf-8 -*-
"""
    Extending employee

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""

from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['Employee']
__metaclass__ = PoolMeta

class Employee():
    __name__ = 'company.employee'
    #_inherits = {'party.party': 'party'}

    basic_salary = fields.Numeric('Salary', required=True)
    hra = fields.Numeric('House Rent Allowance', required=True)
    da = fields.Numeric('Daily Allowance', required=True)

