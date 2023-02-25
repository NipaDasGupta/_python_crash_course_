class Employee:
    """Collect an employee's first name, last name and annual salary."""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self. annual_salary = annual_salary

    def give_rise(self, annual_salary=5000):
        """Adds $5,000 to the annual salary by default but also accepts a
        different raise amount."""
        self.annual_salary =  annual_salary
        return self.annual_salary
