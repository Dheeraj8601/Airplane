import frappe
import random
import string
from frappe.model.document import Document
from frappe import _

class AirplaneTicket(Document):
    def before_submit(self):
        if self.ticket_status != "Boarded":
            frappe.throw("Cannot submit Airplane Ticket. Status must be 'Boarded'.")

    def validate(self):
        self.remove_duplicate()
        self.calculate_total_amount()
        #self.set_seat()
        self.check_capacity()

    def set_seat(self):
        if not self.seat:
            random_number = str(random.randint(10, 49))  
            random_letter = random.choice(string.ascii_uppercase[:3])  
            seat = random_number + random_letter
            self.seat = seat
            frappe.msgprint(_(self.seat))

    def remove_duplicate(self):
        unique_add_ons = set()

        for idx in range(len(self.add_ons) - 1, -1, -1):
            add_on = self.add_ons[idx]
            if add_on.item in unique_add_ons:
                self.add_ons.pop(idx)
                frappe.msgprint(_("Duplicate item removed"))
            else:
                unique_add_ons.add(add_on.item)

    def calculate_total_amount(self):
        total_amount = self.flight_price

        for add_on in self.add_ons:
            total_amount += add_on.amount

        self.total_amount = total_amount
        frappe.msgprint('Total amount is {}'.format(self.total_amount))
        
    def check_capacity(self):
        # Get the capacity of the airplane linked to this ticket
        airplane_capacity = frappe.get_value("Airplane", self.flight, "capacity")

        # If airplane_capacity is None or empty, set it to 0
        if not airplane_capacity:
            airplane_capacity = 0

        # Get the count of tickets for this flight
        ticket_count = frappe.db.count("Airplane Ticket", {"flight": self.flight, "ticket_status": ["!=", "Cancelled"]})

        if ticket_count >= airplane_capacity:
            frappe.throw("Cannot create Airplane Ticket. Capacity of the airplane exceeded.")
