import csv


listobjs = []
users = {k:v for (k,v) in enumerate(range(100))}

class Employees:

    def __init__(self, firstname,lastname,email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    @classmethod
    def from_str(cls,emp_str):
        #emp_str = "".join(emp_str)
        first,last,mail = emp_str
        return cls(first,last,mail)

    def all_info(self):
        return f"Name: {self.firstname} {self.lastname} | Contact: {self.email}"




with open("notpyfiles\\names.csv") as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for index,line in enumerate(csv_reader):
        listobjs.append((line["first_name"],line["last_name"],line["email"]))


for i, x in enumerate(listobjs):
    users[i] = Employees.from_str(listobjs[i])
    print(users[i].all_info())






