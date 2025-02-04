# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:30:30 2025

@author: somai
Challenge 3: Access Visualization
Objective
Develop a visual representation of the company's access control system to identify patterns,
overlaps, and security risks.
Scenario
The company’s security team is struggling to interpret raw access data. They need a clear way to see:
Employees who have access to financial records, technical documents, or both.
Employees with no access, who may need onboarding.
Any overlap that could indicate excessive privileges or security risks.
Instead of listing raw data, your task is to create a structured representation that makes these relationships intuitive and easy to understand.
Your Task
Using the provided employee access data, design a way to illustrate:
Who belongs where? Group employees based on their level of access.
Where is the overlap? Show employees who have access to both financial and technical records.
Who is left out? Identify employees without access.
Are there risks? Indicate employees who might be exposed to unnecessary data.
Your output should visually highlight these relationships without explicitly listing them in a simple table or list. 
Think beyond just printing data—use a format that helps detect patterns at a glance.
"""
finance = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}
tech = {"E7642", "E8873", "E6590", "E9812", "E4520"}
other = {"E9999"}

print(at_least_one = finance | tech)
print(both_access = finance & tech)
print(only_tech_access = tech - finance)
print(only_finance_access = finance - tech)
print(no_access = other - (finance | tech))
