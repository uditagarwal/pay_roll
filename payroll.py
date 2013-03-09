# -*- coding: utf-8 -*-
"""
    Payroll Record

    Payroll Record

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.

"""
from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval
from trytond.pool import Pool

__all__ = ['Payroll']


class Payroll(ModelSQL, ModelView):
    'Payroll'
    __name__ = 'payroll.payroll'
    employees = fields.Many2One(
        'company.employee', 'employee', 'Employee', required=True
    )
    fiscal_year = fields.Many2One(
        'account.fiscalyear', 'Fiscal Year', required=True
    )
    salary = fields.Function(
        fields.Numeric('Salary'), 'get_salary'
    )
    days_present = fields.Function(
        fields.Integer('Present'), 'get_days_present'
    )
    period = fields.Many2One(
        'account.period', 'Period', domain=[
            ('fiscalyear', '=', Eval('fiscal_year'))
        ], depends=['fiscal_year'], required=True
    )

    def get_days_present(self,name):
        """
        Return number of days present for the employee
        """

        Attendance = Pool().get('payroll.attendance')

        return Attendance.search([
            ('employee', '=', self.employees.id),
            ('type', '=', 'full day'),
            ('date', '>=', self.period.start_date),
            ('date', '<=', self.period.end_date),
        ], count=True)

    def get_salary(self,name):
        """
        Return salary for the employee and period in this record
        """

        monthly_salary = self.employees.total_sal

        salary_per_day = monthly_salary / \
            abs((self.period.end_date - self.period.start_date)).days
        return salary_per_day * self.days_present

    @classmethod
    def __setup__(cls):
        super(Payroll, cls).__setup__()
        cls._sql_constraints += [
            ('salary_uniq', 'UNIQUE(employees, period)',
                'Salary already given!'),
        ]
