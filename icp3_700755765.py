#!/usr/bin/env python
# coding: utf-8

# In[24]:


class Employee:
    emp_count = 0 

    def __init__(self, name, family, salary, department):
        Employee.emp_count += 1
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

    def __str__(self):
        return f"Employee: {self.name} {self.family}, Salary: ${self.salary:.2f}, Department: {self.department}"

    def average_salary(self, employees):
        total_salary = sum(emp.salary for emp in employees)
        return total_salary / len(employees) if len(employees) else 0

class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        super().__init__(name, family, salary, department)

    def __str__(self):
        return f"Full-time Employee: {super().__str__()}"

emp1 = Employee("Deekshitha", "Gaddameedhi", 80000, "Quality Assurance")
emp2 = FulltimeEmployee("Deepika", "Chopra", 65000, "DevOps")

print(f"Number of Employees: {Employee.emp_count}")
print(emp1)
print(emp2)

employees = [emp1, emp2]
average_sal = emp1.average_salary(employees)
print(f"Average Salary: ${average_sal:.2f}")


# In[42]:


import numpy as np
random_vector = np.random.uniform(1, 20, 20)
print(random_vector,"\n")

reshaped= random_vector.reshape(4,5)
print(reshaped,"\n")

reshaped[np.arange(4), reshaped.argmax(axis=1)] = 0
print(reshaped)


# In[ ]:




