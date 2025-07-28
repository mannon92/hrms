import frappe
from frappe.model.document import Document

class EmployeeRecognition(Document):
    """Record of peer-to-peer recognition."""

    def validate(self):
        self.award_points()

    def award_points(self):
        if not self.points:
            return
        employee = frappe.get_doc("Employee", self.recognized_employee)
        current_points = employee.get("recognition_points") or 0
        employee.db_set("recognition_points", current_points + self.points)

    def redeem(self, reward, points_required):
        employee = frappe.get_doc("Employee", self.recognized_employee)
        current_points = employee.get("recognition_points") or 0
        if current_points < points_required:
            frappe.throw("Not enough recognition points")
        employee.db_set("recognition_points", current_points - points_required)
        frappe.msgprint(f"Redeemed {reward} for {points_required} points")
