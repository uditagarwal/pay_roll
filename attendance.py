# -*- coding: utf-8 -*-
"""
    attendance

    This file define model for attendance

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from datetime import datetime

from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval
from trytond.transaction import Transaction

__all__ = ['Attendance']


class Attendance(ModelSQL, ModelView):
    'Attendance'
    __name__ = 'payroll.attendance'

    employee = fields.Many2One('company.employee', 'Employee', required=True,
        domain=[('company', '=', Eval('company'))])
    date = fields.Date('Date')
    company = fields.Function(fields.Many2One('company.company', 'Company'),
        'get_company')
    type = fields.Selection([
        ('full day', 'Full Day'),
        ('half day', 'Half Day'),
        ('absent', 'Absent'),
    ], 'Type', required = True)

    @staticmethod
    def default_date():
        return  datetime.date(datetime.utcnow())

    def get_company():
        return Transaction().context.get('company')

    @classmethod
    def __setup__(cls):
        super(Attendance, cls).__setup__()
        cls._sql_constraints += [
            ('attendance_uniq', 'UNIQUE(employee, date)',
                'Attendance already marked!'),
            ]
