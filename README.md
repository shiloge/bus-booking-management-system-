# Vyathra - Bus Reservation Management System

---

## About the Project

This is a basic, menu-driven terminal application that works entirely inside the command prompt without any graphical user interface (GUI). It is our very first Python project, developed from scratch by ourselves as a Class 12 Computer Science project. 

It acts as a basic digital terminal for managing bus travel operations. It connects a Python backend directly to a MySQL database, allowing everyday users to check schedules and book seats while giving administrators basic controls to add routes, manage user grids, and audit overall booking data.

We built this by taking enough time to learn the concepts, gathering help and references from our CBSE Sultan Chand textbook, W3Schools, and Gemini to structure the database setup and code workflows. The application is built as a basic framework with limitations within the school framework and is not meant for practical, real-world use.

---

## What the Project Does

### User Options
* Login & Registration: Takes the username and password directly from the user and matches it against the database records.
* Ticket Booking: Allows users to view available bus routes and select the number of seats they want to book.
* Booking ID Generation: Automatically generates a unique tracking code for every successful booking transaction.
* Booking History: Users can retrieve a history list of their past bus bookings.
* Update Profile: Users can edit their active profile data directly from the account settings.

### Admin Options
* Manage Routes: Admin can add new bus routes (with up to 3 custom stops) or delete existing routes from the system.
* View Bus Routes: Admin can view the complete current listing of all bus schedules and routes.
* View All Bookings: Admin can audit the complete transactional booking history of every ticket issued across the system.
* Manage Users: Admin has access to view specific user data, review full user grids, or drop user accounts entirely.

---

## Technical Specifications & References

* Language: Python 3.10
* Database Management: MySQL
* Connectivity Module: mysql-connector-python
* External References: Implemented core practical concepts including parametric data queries, dynamic table mapping, and sys library hooks. A slight assist from AI was utilized strictly for structuring resources and documentation rather than direct code generation.

---

## Database Table Explanations

The backend uses five simple tables to keep things organized:
1. cred: Stores essential user account login credentials.
2. userdata: Holds the complete details of the registered user.
3. bussid: Contains the active bus routes, timings, and prices.
4. bookings: Logs the tickets booked by the user and the seat counts.
5. curr: Works like a runtime random access memory (RAM). It is a temporary table that stores session data for the currently logged-in user and clears out completely upon logout.

*(Note: The complete working flowchart for this database layout and the program logic has been attached inside the project PDF file for quick reference.)*

---

## Database Attachments & Structural State

There are two separate SQL database backups attached to this project repository:
* vyathra_blueprint.sql: Contains the pure skeleton structure and empty table frameworks for a fresh installation.
* vyathra_demo.sql: Contains the table architecture pre-loaded with sample testing records for quick, immediate operational testing.

Note that there are multiple structural logical flows remaining within the database handling; while minor problems and logical loop errors were cleaned up right before this upload, the system remains a basic academic framework rather than an optimized database deployment.

---

## Project Component Files
The repository includes the following items:
* Source Script: The complete Python connection script handling the backend menus.
* Database Blueprints: The SQL structure frameworks including the demo records used during system testing loops.
* Documentation PDF: The complete guide containing structural data layouts and code block references.

---

Project developed by Shilo George and Allan Binu Scaria.
