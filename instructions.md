# 🛠️ Quick Setup Guide

### 1. Prerequisites
Make sure you have these installed on your Windows PC (check Google if you need setup steps):
* **Python 3**
* **MySQL Server & Workbench**
* **MySQL Connector** (Run `pip install mysql-connector-python` in Command Prompt)

---

### 2. Choose Your Database File
* **`vyatra_demo.sql` (Recommended):** Has sample data loaded so you can test booking features instantly.
* **`skeleton.sql`:** Completely empty tables. You must manually insert admin credentials into the database first to log in.

---

### 3. Import the Database
1. Open **MySQL Workbench** and click your local connection.
2. Create a blank database first: Click the **Create a new schema** icon at the top (or run `CREATE DATABASE bus_booking;` in a query tab).
3. Go to **Server** -> **Data Import/Restore**.
4. Choose **Import from Self-Contained File** and select your `.sql` file.
5. Under **Default Target Schema**, select the blank database you just created.
6. Click **Start Import** at the bottom right.

---

### 4. Run the Project
1. Open the Python script and look for the database connection lines.
2. The default is usually set to username `root` and password `password` (or whatever password you set during MySQL installation). Modify these lines if yours is different:
   ```python
   user="root",
   password="password"

