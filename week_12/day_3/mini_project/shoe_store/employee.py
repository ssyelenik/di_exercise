import json
class Employee():
    def get_status(self,password):
        employees=self.get_employees()
        employee_found="no"
        for employee in employees:
            if password==employee['password']:
                employee_found="yes"
                return employee['status']
        if employee_found=="no":
            status="invalid_employee"
            return status

    def get_employees(self):
        with open("employee.json","r") as f:
            employees=json.load(f)
        return employees
