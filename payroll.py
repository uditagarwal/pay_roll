# -*- coding: utf-8 -*-
"""
    Payroll Record

    Description goes here...

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.

"""
from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval
from datetime import datetime

__all__ = ['Payroll']

class Payroll(ModelSQL, ModelView):
    'Payroll'
    __name__ = 'payroll.payroll'
    employees = fields.Many2One('company.employee', 'employee', 'Employee')
    fiscalyear = fields.Many2One('account.fiscalyear', 'Fiscal Year',
    required = True,on_change=['fiscalyear'])
    salary = fields.Function(fields.Numeric('Salary'), 'get_salary1')
    dayspresent = fields.Function(fields.Numeric('Present'), 'get_days_present')
    period = fields.Many2One('account.period', 'Period', required=True,
    on_change=['period'])
    
    def days_between(d1,d2):
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.strptime(d2, "%Y-%m-%d")
        return abs((d2-d1).days)

    def get_days_present(self,name):
        Attendance = Pool().get('payroll.attendance')
        attendances = Attendance.Search([
            ('employee', '=', self.employee.id),
            ('type', '=', 'full day')
        ])
        days_present = len(attendances)
        return days_present
 
    def get_salary(self,name):
        Salary = Pool().get('company.employee')
        salary = Salary.Search([
            ('employee','=',self.employee.id)])
        monthsalary = Salary[0].basic_salary + Salary[0].hra + Salary[0].da
        Period  = Poo().get('account.period')
        period = Period.search([
            ('period','=',self.period.id)])
        start_date =  period[0].start_date
        end_date = period[0].end_date
        difference = days_between(start_date,end_date)
        salaryperday = int(monthsalary)/int(difference)
        return salaryperday

    def get_salary1(self,name):
        spd = get_salary(self,name)
        att = get_days_present(self,name)
        return int(spd*att)


class PrintPayroll(ModelSQL, ModelView):
    'Print Payroll'
    __name__='payroll.printpayroll'
    fiscalyear = fields.Many2One('account.fiscalyear', 'Fiscal Year',
     required=True, on_change=['fiscalyear'])
    start_period = fields.Many2One('account.period','Start Period',
    domain = [('fiscalyear', '=', Eval('fiscalyear')),('start_date','<=',
    (Eval('end_period'),'start_date')),],depends=['fiscalyear','end_period'])
    end_period = fields.Many2One('account.period', 'End Period', domain=[
    ('fiscalyear', '=', Eval('fiscalyear')),('start_date', '>=',
    (Eval('start_period'), 'start_date'))],
    depends=['fiscalyear','start_period'])

    @staticmethod
    def default_fiscalyear():
        FiscalYear = Pool().get('account.fiscalyear')
        return FiscalYear.find(
            Transaction().context.get('company'), exception=False)

    def default_company():
        return Transaction().context.get('company')



