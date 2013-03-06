from trytond.pool import Pool

def register():
    Pool.register(
        module='payroll', type_='model')
