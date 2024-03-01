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
    def __init__(self, name,job):
        self.name=name
        self.job=job
    def get_name(self):
        print("getting name")
        return self._name
    def set_name(self, name):
        if isinstance(name, str) and 1<=len(name)<=25:
            saved=name.title()
            print("setting name")
            self._name=saved
            print(saved)
        else:
            print("Name must be string between 1 and 25 characters.")
    name=property(get_name, set_name)
    def get_job(self):
        print("getting job")
        return self.get_job
    def set_job(self, job):
        if job in APPROVED_JOBS:
            print("setting job")
            self._job=job
            print(job)
        else:
            print("Job must be in list of approved jobs.")
    job=property(get_job, set_job)
        

Car=Person(name="bMW", job="ITC")
Car.name="simon"
Car.job="Software Engineering"
