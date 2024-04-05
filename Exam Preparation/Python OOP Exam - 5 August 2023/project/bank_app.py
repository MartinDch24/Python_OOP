from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan
from project.clients.student import Student
from project.clients.adult import Adult


class BankApp:
    VALID_LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENT_TYPES = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []
        self.granted_loans = []

    def add_loan(self, loan_type: str):
        try:
            new_loan = self.VALID_LOAN_TYPES[loan_type]()
        except KeyError:
            raise Exception("Invalid loan type!")

        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        try:
            new_client = self.VALID_CLIENT_TYPES[client_type](client_name, client_id, income)
        except KeyError:
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = next(filter(lambda c: c.client_id == client_id, self.clients))
        loan = next(filter(lambda l: l.__class__.__name__ == loan_type, self.loans))

        client.add_loan(loan)
        self.granted_loans.append(loan)
        self.loans.remove(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        changed_loans = 0

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                changed_loans += 1

        return f"Successfully changed {changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        affected_clients = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                affected_clients += 1

        return f"Number of clients affected: {affected_clients}."

    def get_statistics(self):
        return (f"Active Clients: {len(self.clients)}\n"
                f"Total Income: {(sum(c.income for c in self.clients) if self.clients else 0):.2f}\n"
                f"Granted Loans: {len(self.granted_loans)}, "
                f"Total Sum: {(sum(l.amount for l in self.granted_loans)if self.granted_loans else 0):.2f}\n"
                f"Available Loans: {len(self.loans)}, "
                f"Total Sum: {(sum(l.amount for l in self.loans) if self.loans else 0):.2f}\n"
                f"Average Client Interest Rate: "
                f"{(sum(c.interest for c in self.clients)/len(self.clients) if self.clients else 0):.2f}")
