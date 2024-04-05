from project.clients.base_client import BaseClient


class Student(BaseClient):

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, 2.0)

    def add_loan(self, loan):
        if loan.__class__.__name__ != "StudentLoan":
            raise Exception("Inappropriate loan type!")

        self.loans.append(loan)

    def increase_clients_interest(self):
        self.interest += 1.0
