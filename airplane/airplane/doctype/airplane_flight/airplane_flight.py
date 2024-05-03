# Copyright (c) 2024, Dheeraj S and contributors
# For license information, please see license.txt
from frappe.model.document import Document

import frappe


# from frappe.website.website_generator import WebsiteGenerator
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(Document):
    def validate(self):
        self.check_source_and_destination_airport()
        self.set_flight_status()
        
    def set_flight_status(self):
        if self.docstatus == 0:
            if self.status != "Completed":
                self.status = "Completed"

    def check_source_and_destination_airport(self):
        if self.source_airport == self.destination_airport:
            # self.destination_airport = 0
            # self.destination_airport_code = 0
            frappe.throw(_("Destination airport cleared as source and destination airports cannot be the same."))
