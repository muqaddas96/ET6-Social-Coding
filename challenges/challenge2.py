# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:30:30 2025

@author: somai
Challenge 2: Digital Access Control
Objective
Use set operations to analyze and improve a company's digital access control system while 
identifying potential security risks in data access.
Scenario
A secure company vault stores sensitive data, where employees are granted access based on their roles:
Finance Team (F): Needs access to financial records.
Tech Team (T): Needs access to technical documents.
Some employees belong to both teams due to cross-departmental responsibilities.
Access Data (Given)
The security system tracks employee IDs (formatted as "E####").

A = finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}
B = tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}
C = All Employees

Additionally, two special cases exist:
E0001 (Admin): Has access to all data but is not listed in specific access groups.
E9999 (New Employee): Has no assigned access yet.
Your Task
Analyze the current access structure and identify potential security risks by answering the following:
Who has access to at least one type of data?
Who has access to both financial and technical data?
Who has exclusive access to only one type of data?
Which employees currently lack access (but exist in the system)?
Are there unnecessary overlaps in access that could pose a security risk?
What changes would you recommend to enhance security and minimize excessive access?
# -*- coding: utf-8 -*-

"""
finance = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}
tech = {"E7642", "E8873", "E6590", "E9812", "E4520"}
other = {"E9999"}

print(at_least_one = finance | tech)
print(both_access = finance & tech)
print(only_tech_access = tech - finance)
print(only_finance_access = finance - tech)
print(no_access = other - (finance | tech))
