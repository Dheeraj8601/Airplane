# Copyright (c) 2024, Dheeraj S and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Airplane(Document):
    @classmethod
    def add_initial_audit_completed_field(cls):
        return {
            "fieldname": "initial_audit_completed",
            "label": __("Initial Audit Completed"),
            "fieldtype": "Check",
            "default": 0
        }

    def on_update(self):
        # Set permissions based on user roles
        if "Airport Authority Personnel" in frappe.get_roles():
            self.flags.ignore_permissions = True
            self.initial_audit_completed = 1
            self.flags.ignore_permissions = False
