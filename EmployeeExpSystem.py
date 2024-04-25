class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.performance_rating = 0
        self.attendance_rating = 0
        self.productivity_rating = 0
        self.training_rating = 0
        self.job_competencies_rating = 0
        self.adaptability_rating = 0

    def evaluate_performance(self):
        self.attendance_rating = int(input("Enter attendance rating (1-10): "))
        self.productivity_rating = int(input("Enter productivity rating (1-10): "))
        self.training_rating = int(input("Enter training rating (1-10): "))
        self.job_competencies_rating = int(input("Enter job competencies rating (1-10): "))
        self.adaptability_rating = int(input("Enter adaptability rating (1-10): "))

        # Calculate the overall performance rating based on different criteria
        self.performance_rating = (self.attendance_rating + self.productivity_rating + self.training_rating + self.job_competencies_rating + self.adaptability_rating) / 5

    def display_performance(self):
        print("Employee:", self.name)
        print("Department:", self.department)
        print("Performance Rating:", self.performance_rating)

class EmployeeExpertSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, department):
        employee = Employee(name,department)
        self.employees.append(employee)

    def remove_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                print("\nEmployee", name, "removed successfully.")
                return
        print("Employee", name, "not found.")

    def update_employee_performance(self, name):
        for employee in self.employees:
            if employee.name == name:
                employee.evaluate_performance()
                print("\nPerformance for", name, "updated successfully.")
                return
        print("Employee", name, "not found.")

    def calculate_average_performance(self):
        if len(self.employees) == 0:
            print("No employees found.")
            return

        total_rating = 0
        for employee in self.employees:
            total_rating += employee.performance_rating
            print(total_rating)

        average_rating = total_rating / len(self.employees)
        print("Average Performance Rating is :", average_rating)

    def display_all_employees(self):
        if len(self.employees) == 0:
            print("No employees found.")
            return

        for employee in self.employees:
            employee.display_performance()


# Create an instance of the EmployeeExpertSystem class
expert_system = EmployeeExpertSystem()

while True:
    print("\nEmployee Performance Evaluation Expert System")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Update Performance")
    print("4. Calculate Average Performance")
    print("5. Display All Employees")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        name = input("\nEnter employee name: ")
        department = input("Enter employee department: ")
        expert_system.add_employee(name, department)
        print("Employee", name, "added successfully.")

    elif choice == "2":
        name = input("\nEnter employee name: ")
        expert_system.remove_employee(name)

    elif choice == "3":
        name = input("\nEnter employee name: ")
        expert_system.update_employee_performance(name)

    elif choice == "4":
        expert_system.calculate_average_performance()

    elif choice == "5":
        expert_system.display_all_employees()

    elif choice == "6":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")