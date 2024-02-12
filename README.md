Interactive Vending Machine Management System
Description
This repository hosts the code for an Interactive Vending Machine Management System, a Python-based application designed as part of a university assignment. This system provides a simulated environment for managing a vending machine's operations, including inventory tracking, sales recording, and facilitating customer transactions.

Features
Object-Oriented Design: Utilizes classes and objects to model real-world vending machine operations.
Inventory Management: Tracks items in the vending machine, including sweets, salty snacks, and liquids.
Sales Tracking: Records transactions and maintains sales data.
Secure Transactions: Implements alphanumeric keys for secure customer purchases.
Error Handling: Robust system to handle various operational errors.
User-Friendly Interface: Designed for easy use and interaction with customers.


Customer Class: Manages customer information, including name, address, and mobile number. It also tracks customer purchase orders.

MobileApp Class: Acts as a simulated mobile application interface. It handles item selection, generates a transaction key, and manages customer information.

VendingMachine Class: Represents a vending machine, managing items and tracking total sales. It includes functions to add items, find items by ID, display available items, and update sales.

Item Class and Subclasses (Sweet, Salty, Liquid): The base class 'Item' is extended by three subclasses representing different types of items (Sweet, Salty, Liquid). Each class has unique attributes like flavor, salt content, or volume, in addition to common attributes like item ID, name, manufacturer, price, and quantity.

Item Selection and Payment Process: The MobileApp class facilitates the item selection and payment process. Customers select items from a vending machine, confirm their purchase, and receive a unique alphanumeric key for the transaction. The payment process includes error handling for invalid inputs.

Sales Tracking and Reporting: The system can track and display sales data. Vending machines maintain records of total sales and sales by item type. The VendingMachine class includes methods to display sales summaries, both overall and categorized by item type.

Sample Usage: The code includes an example of initializing vending machines, adding items to them, and simulating a customer interaction using the mobile app interface.
