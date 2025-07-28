import frappe
from hrms.hr.doctype.employee_recognition.employee_recognition import EmployeeRecognition


def test_award_points(monkeypatch):
    emp = frappe._dict(name="EMP-0001", recognition_points=0)

    def fake_get_doc(dt, name):
        assert dt == "Employee"
        return emp

    monkeypatch.setattr(frappe, "get_doc", fake_get_doc)

    doc = EmployeeRecognition(
        awarding_employee="EMP-0002",
        recognized_employee="EMP-0001",
        points=10,
    )

    monkeypatch.setattr(emp, "db_set", lambda field, val: emp.update({field: val}))
    doc.validate()
    assert emp.recognition_points == 10
