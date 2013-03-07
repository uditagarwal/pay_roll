# -*- coding: utf-8 -*-
"""
    attendance

    This file define model for attendance

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from datetime import datetime

from trytond.model import ModelView, ModelSQL, fields

__all__ = ['Attendance']


class Attendance(ModelSQL, ModelView):
    'Attendance'
    __name__ = 'attendance.attendance'

    employee = fields.Many2One('company.company', 'Employee', required=True,)
    date = fields.Date('Date')
    type = fields.Selection([
        ('full day', 'Full Day'),
        ('half day', 'Half Day'),
        ('absent', 'Absent'),
    ], 'Type', required = True)

    @classmethod
    def default_date():
        return datetime.utc.now()
