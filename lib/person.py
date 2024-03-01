#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Simon",job="ITC"):
        self.set_name(name)
        self.set_job(job)
    
    def set_name(self, name):
        if isinstance(name, str) and 1<=len(name)<=25:
            saved=name.title()
            print("setting name")
            self._name=saved
            print(saved)
        else:
            print("Name must be string between 1 and 25 characters.")
    
    def set_job(self, job):
        if job in APPROVED_JOBS:
            print("setting job")
            self._job=job
            print(job)
        else:
            print("Job must be in list of approved jobs.")
    
    @property
    def name(self):
        return self._name
    
    @property
    def breed(self):
        return self._breed


