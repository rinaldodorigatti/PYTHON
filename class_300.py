


def main():
    class PayrollSystem:
        def calculate_amount(self, employees):
            calculwithbonus = 0
            salaryandbonus = 0
            print("==== Calculating payroll ====")
            print("=============================")
            # for employee in employees:
            print(f"Payroll for  : {employees.idd} - {employees.name}")
            print(f"Check amount : {employees.calculate_amount()}")
            salarywithbonus = (employees.calculate_amount() / 100) * employees.calculate_bonus()
            salaryandbonus = employees.calculate_amount() + salarywithbonus
            salaryandbonusf = "{:.2f}".format(salaryandbonus)
            print(f"Bonus        : {employees.calculate_bonus()}")
            print(f"+Bonus       : {salaryandbonusf}")
            print("")


    class PayrollSystem1:
        def calculate_payroll(self, employees):
            print("")
            print('Calculating Payroll')
            print('===================')
            for employee in employees:
                print(f'Payroll for: {employee.idd} - {employee.name}')
                print(f'- Check amount: {employee.calculate_amount()}')
                print('')


    class Employee:
        def __init__(self, idd, name):
            self.idd = idd
            self.name = name


    class SalaryEmployee(Employee):
        def __init__(self, idd, name, weekly_salary, bonus):
            super().__init__(idd, name)
            self.weekly_salary = weekly_salary
            self.bonus = bonus

        def calculate_amount(self):
            return self.weekly_salary

        def calculate_bonus(self):
            return self.bonus

        def __eq__(self, other):
            return self.weekly_salary == other.weekly_salary

        def __lt__(self, other):
            return self.weekly_salary < other.weekly_salary

        def __gt__(self, other):
            return self.weekly_salary > other.weekly_salary


    class HourlyEmployee(Employee):
        def __init__(self, idd, name, hours_worked, rate_hours):
            super().__init__(idd, name)
            self.hours_worked = hours_worked
            self.rate_hours = rate_hours

        def calculate_amount(self):
            formatage = "{:.2f}".format(self.hours_worked * self.rate_hours)
            return formatage


    class ComissionEmployee(SalaryEmployee):
        def __init__(self, idd, name, weekly_salary, comission, bonus):
            super().__init__(idd, name, weekly_salary, bonus)
            self.comission = comission

        def calculatecomission(self):
            fixed = super().calculate_amount()
            return fixed + self.comission


    class DisgruntledEmployee:
        def __init__(self, idd, name):
            self.idd = idd
            self.name = name

        def calculate_amount(self):
            return 10000


    se = SalaryEmployee(1, 'Rinaldo', 350, 10)
    print(se.calculate_amount())

    ep = SalaryEmployee(1, 'Rinaldo', 340, 8)
    # ep = {'idd': 1, 'name': 'Rinaldo'}
    ff = PayrollSystem()
    ff.calculate_amount(ep)

    ep1 = SalaryEmployee(2, 'Sara', 211, 5)
    egal = (ep == ep1)
    pluspetit = (ep < ep1)
    plusgrand = (ep > ep1)
    print(f'Compare ep == ep1 : {egal}')
    print(f'Compare ep < ep1  : {pluspetit}')
    print(f'Compare ep > ep1  : {plusgrand}')

    ep2 = HourlyEmployee(3, 'Diego', 35, 10.4915)
    heures = ep2.calculate_amount()
    print(f'Moyenne heures : {heures}')

    ep3 = ComissionEmployee(4, 'Lucie', 355, 55, 0.5)
    comission = ep3.calculatecomission()
    print(f'Comission      : {comission}')

    ep6 = DisgruntledEmployee(20, 'Anonymous')

    ep4 = PayrollSystem1()
    ep4.calculate_payroll([ep1, ep2, ep3, ep6])


if __name__ == '__main__':
    main()
