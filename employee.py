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
    """Extends employee model by adding three fields

    """
    __name__ = 'company.employee'

    basic_salary = fields.Numeric('Salary', required=True)
    hra = fields.Numeric('House Rent Allowance', required=True)
    da = fields.Numeric('Daily Allowance', required=True)

    @classmethod
    def __setup__(cls):
        super(Employee, cls).__setup__()
        cls._constraints += [
            ('check_hra', 'hra_not_valid'),
            ('check_da', 'da_not_valid'),
            ]
        cls._error_messages.update({
                'hra_not_valid': 'Invalid Values',
                'da_not_valid': 'Not Valid',
                })

    def check_hra(self):
        """
        Checks if hra is greater than basic salary
        """
        return self.basic_salary > self.hra and self.hra < 6000


    def check_da(self):
        """
        Checks if da is greater than basic salary and hra
        """
        return self.basic_salary > self.da and self.da < 3000
