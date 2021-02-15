# SCADA-Finder

## Background and Motivation
Cyber-attacks on critical power plants are turning out to be increasingly prevalent. Indian transport and power & energy sector is widely dependent on OT systems. These OT systems may comprise of ICS, SCADA, DCS, PLC, RTU, etc. Many of such ICS/SCADA devices are associated with the open network for the operational requirement. But few of the OT systems are inadvertently connected to the public networks, making them vulnerable to be available for hackers. 
Keeping this in mind, we have developed a framework that would passively check for ICS/SCADA systems connected to the Internet.
The program not only searches for the above details but also stores the results in the database so that it's later available to be analyzed.
The stakeholders of NCIIPC can stay informed about these online ICS/SCADA systems and their vulnerabilities; Hereafter, the necessary actions opted on time for their protection.
Objective
The core objective of the project is to identify online ICS/SCADA systems and their vulnerabilities using passive reconnaissance. 
Scope
The project shall identify various ICS/SCADA systems of our nation openly indexed online on the Internet. The framework is also able to identify the organization; As well as the vulnerability, if present in the device.


## Methodologies used:
In order to meet the objective of the project, the following methodologies were used:
•	Designed script to identify various online ICS/SCADA systems of the nation from shodan.io.
•	Curated various specially designed filters to fetch results from shodan.
•	Designed script to identified various online ICS/SCADA systems of the nation from censys.io. 
•	Curated various specially designed filters from Censys.
•	The fetched information are recursively stored into the database.

## Software and Hardware Requirements
This section describes the software and hardware requirements of the system.
Software Requirements:
•	Python 3.6.8
•	Shodan CLI
•	Censys CLI
•	XAMP Server
