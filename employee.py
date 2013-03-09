# -*- coding: utf-8 -*-
"""
    Extending employee

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pool import Pool

__all__ = ['Employee']
__metaclass__ = PoolMeta


class Employee():
    """Extends employee model by adding three fields

    """
    __name__ = 'company.employee'

    basic_salary = fields.Numeric('Salary', required=True)
    hra = fields.Numeric('House Rent Allowance', required=True)
    da = fields.Numeric('Daily Allowance', required=True)
<<<<<<< HEAD
    total_sal = fields.Function(fields.Numeric('Inhand Salary'), 'get_salary')

    def get_salary(self,name):
        Employee = Pool().get('company.employee')
        return sum([self.basic_salary, self.hra, self.da])

    @classmethod
    def __setup__(cls):
        super(Employee, cls).__setup__()
        cls._constraints += [
            ('check_hra', 'hra_not_valid'),
            ('check_da', 'da_not_valid'),
            ]
        cls._error_messages.update({
                'hra_not_valid': 'HRA should be less than your salary.',
                'da_not_valid': 'Your Daily Allowance seems greater than \
                your salary. Please enter the correct value.',
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
=======
>>>>>>> 0343c6d59e60caf0405f3bb79780df63b8f622cc
