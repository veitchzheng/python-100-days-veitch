from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """员工(抽象类)"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """计算员工工资(抽象方法)"""
        pass


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hours=0):
        super().__init__(name)
        self.working_hours = working_hours

    def get_salary(self):
        return self.working_hours * 200.0


class Salesman(Employee):
    """销售"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


if __name__ == '__main__':
    emps = [Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'), Programmer('荀彧'), Salesman('张辽')]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hours = int(input(f'请输入{emp.name}本月工作时间: '))
        elif isinstance(emp, Salesman):
            emp.sales = float(input(f'请输入{emp.name}本月销售额: '))
        print(f'{emp.name}本月工资为: ￥{emp.get_salary():.2f}元')