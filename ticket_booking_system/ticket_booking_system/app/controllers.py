from .models import TicketModel

class TicketController:

    def __init__(self):
        self.model = TicketModel()

    def create_booking(self, name, movie, seats):
        self.model.book_ticket(name, movie, seats)

    def list_bookings(self):
        return self.model.get_all()