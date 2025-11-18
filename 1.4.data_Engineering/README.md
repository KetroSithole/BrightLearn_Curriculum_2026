# 🎓 Data Engineering 6‑Month Course Guide (University Edition – README)

**complete, structured course guide** for a 6‑month Data Engineering program suitable for **university submission, portfolio use, or GitHub documentation**.

It includes:

* Clear weekly modules
* Learning outcomes
* Tools & technologies
* Practical project work
* Assessments & deliverables
* Dimensional modelling concepts
* Folder structure for GitHub/university submission

---

# 🧭 **Course Overview**

This course introduces foundational and intermediate concepts in Data Engineering including:

* SQL (beginner → advanced)
* SSIS (ETL development, data connectors, cleansing, automation)
* Git & GitHub for version control
* Automation using scripts & SQL Jobs
* Data Warehouse fundamentals (Fact/Dim tables)
* Real‑world mini projects and a final capstone project

> **No APIs are included**, as requested.

---

# 🛠️ **Required Tools & Software**

* **SQL Server Management Studio (SSMS)**
* **SQL Server + SSIS (SQL Server Data Tools)**
* **Visual Studio / Visual Studio Code**
* **Git & GitHub**
* **Optional:** Power BI for dashboards

---

# 📅 **WEEK‑BY‑WEEK COURSE BREAKDOWN**

Each week includes a **learning focus**, **practical tasks**, and **expected outcomes**.

---

# 📌 **Month 1 — SQL Foundations**

## **Week 1 – SQL Basics**

**Topics:** SELECT, WHERE, ORDER BY

**Tasks:** Simple SQL queries & filtering

**Outcome:** Ability to query single tables.

---

## **Week 2 – Aggregations & Grouping**

**Topics:** GROUP BY, HAVING, COUNT, SUM, AVG

**Outcome:** Build summary reports.

---

## **Week 3 – Table Joins**

**Topics:** INNER, LEFT, RIGHT, FULL

**Outcome:** Combine data across multiple tables.

---

## **Week 4 – Subqueries & CTEs**

**Topics:** IN, EXISTS, Common Table Expressions

**Outcome:** Create advanced reusable queries.

---

# 📌 **Month 2 — Advanced SQL Topics**

## **Week 5 – Window Functions**

**Topics:** ROW_NUMBER, RANK, DENSE_RANK, LEAD, LAG

**Outcome:** Perform analytic & time‑based calculations.

---

## **Week 6 – Stored Procedures & Functions**

**Outcome:** Write reusable backend logic.

---

## **Week 7 – Transactions & Triggers**

**Topics:** COMMIT, ROLLBACK, AFTER/INSTEAD OF triggers

**Outcome:** Handle data integrity operations.

---

## **Week 8 – Performance Tuning**

**Topics:** Indexing, Execution Plans, Partitioning

**Outcome:** Optimise SQL performance.

---

# 📌 **Month 3 — SSIS Foundations**

## **Week 9 – Introduction to SSIS**

**Topics:** ETL concepts, packages, Control Flow vs Data Flow

---

## **Week 10 – Data Connectors**

**Topics:** SQL, Flat File, Excel, ODBC, ADO.NET

---

## **Week 11 – Basic Transformations**

**Topics:** Derived Column, Lookup, Conditional Split

---

## **Week 12 – Data Cleansing Techniques**

**Outcome:** Standardise and clean incoming datasets.

---

# 📌 **Month 4 — SSIS Advanced (Cleaning, Logging, Deployment)**

## **Week 13 – Error Handling**

**Topics:** Redirect rows, error logs, fail-paths

---

## **Week 14 – Logging in SSIS**

**Topics:** Auditing, log providers, custom logs

---

## **Week 15 – Performance Optimisation**

**Topics:** Buffer tuning, FastParse, avoiding blocking transforms

---

## **Week 16 – Deployment & Scheduling**

**Topics:** SSISDB Catalog, Environment Variables, SQL Agent Jobs

**Outcome:** Build production‑ready ETL pipelines.

---

# 📌 **Month 5 — Git & GitHub**

## **Week 17 – Git Fundamentals**

Commit, push, pull, staging.

---

## **Week 18 – Branching & Merging**

Feature branches, merge strategies.

---

## **Week 19 – Conflict Resolution**

Resolve merge issues.

---

## **Week 20 – GitHub Workflow**

Pull requests, Issues, Documentation standards.

---

# 📌 **Month 6 — Automation & Capstone**

## **Week 21 – Automation Scripts**

PowerShell/Python for file & SQL automation.

---

## **Week 22 – SQL Agent Jobs**

Scheduling tasks, email alerts.

---

## **Week 23 – Optional CI/CD**

GitHub Actions automation.

---

## **Week 24 – Final Capstone Project**

A full ETL Data Engineering Pipeline:

1. Extract (CSV → SSIS)
2. Transform (Clean, Lookup, Standardize)
3. Load (SQL Data Warehouse)
4. Automate (SQL Agent Job)
5. Version Control (GitHub)

---

# 🧠 **DIMENSION & FACT TABLES – CLASS NOTES**

## **Fact Tables (Measures)**

* Numeric events (sales, calls, amounts)
* Large & growing
* Linked to dimensions via keys

## **Dimension Tables (Descriptions)**

* Text attributes (customer names, product types)
* Used for filtering, grouping

**Star Schema Example:**

```
         DimCustomer     DimProduct     DimStore
               \             |             /
                \            |            /
                     FactSales
```

---

# 📁 **Recommended Folder Structure for Submission**

```
📦 University-DataEngineering-Course
 ┣ 📂 SQL
 ┣ 📂 SSIS-Packages
 ┣ 📂 Screenshots
 ┣ 📂 Automation
 ┣ 📂 Documentation
 ┗ 📜 README.md
```

---

# 📝 **Assessment & Deliverables**

* Weekly practical exercises
* Monthly mini‑project
* Final Capstone ETL Project
* GitHub repository submission
* Documentation & presentation

---

If you'd like, I can **add real SQL scripts**, **add SSIS diagrams**, or **format this like a professional university portfolio**.

---

# 🧑‍🏫 **DETAILED TEACHING GUIDE (Use in Class)**

This section expands each week with **what you must teach**, **how to teach it**, class exercises, homework, and outcomes.

---

## **WEEK 1 – SQL BASICS**

### **What to Teach**

* What is a database?
* What is SQL and why it is used
* Table structure (rows/columns)
* SELECT, WHERE, ORDER BY

### **How to Teach It**

* Start with a simple database example
* Demonstrate basic SQL queries live

### **Class Exercise**

* Students write 10 SELECT queries

### **Homework**

* Query a sample dataset and submit 20 queries

---

## **WEEK 2 – AGGREGATIONS & GROUPING**

### **What to Teach**

* SUM, COUNT, AVG, MIN, MAX
* GROUP BY logic
* HAVING vs WHERE

### **How to Teach It**

* Use sales dataset to demo grouping

### **Class Exercise**

* Students build summary reports

### **Homework**

* Create 5 analytical summary queries

---

## **WEEK 3 – JOINS**

### **What to Teach**

* INNER, LEFT, RIGHT, FULL JOIN
* Primary keys & foreign keys

### **Class Exercise**

* ERD drawing session
* Join tables together

### **Homework**

* Write 10 join queries

---

## **WEEK 4 – SUBQUERIES & CTEs**

Teach subqueries, EXISTS, and CTE structure.

---

## **WEEKS 5–8 (ADVANCED SQL)**

Teach window functions, triggers, indexing, performance tuning.

---

## **WEEKS 9–16 (SSIS)**

Teach ETL concepts, connectors, transformations, cleansing, logging, deployment.

---

## **WEEKS 17–20 (GIT)**

Teach version control, branching, conflicts, GitHub workflow.

---

## **WEEKS 21–24 (AUTOMATION & PROJECT)**

Teach scripting, SQL Agent jobs, CI/CD basics, and oversee final project.

---

If you want this turned into a **full university syllabus** with lesson outcomes, exams, and marking criteria, say: **“Create the full syllabus.”**

---

# 🎓 **FULL UNIVERSITY SYLLABUS — Data Engineering (6-Month Program)**

This syllabus is designed for academic submission and delivery. It includes module outcomes, weekly topics, assessments, grading structure, teaching methods, and required resources.

---

# 📘 **Module Information**

**Module Name:** Data Engineering Foundations
**Module Code:** DE-101
**Duration:** 6 Months (24 Weeks)
**Credit Value:** 30 Credits
**Level:** Undergraduate (Year 2 or 3)
**Delivery Mode:** Hybrid / In-Person
**Assessment:** Practical Labs, Assignments, Final Capstone Project

---

# 🧠 **Module Description**

This module provides students with foundational and intermediate knowledge of data engineering. Students will learn SQL, ETL pipelines using SSIS, automation, Git/GitHub version control, and data warehouse concepts. The module emphasises hands-on experience through weekly labs and a full-scale industry-style capstone project.

---

# 🎯 **Module Learning Outcomes**

By the end of this module, students will be able to:

1. Write and optimise SQL queries ranging from basic to advanced.
2. Design ETL pipelines using SSIS with proper data cleansing and error handling.
3. Apply dimensional modelling concepts (Fact/Dim tables).
4. Use Git and GitHub for version control and collaborative workflows.
5. Automate data workflows using scripts and SQL jobs.
6. Deliver an end-to-end data engineering project using real-world methodology.

---

# 🏫 **Teaching & Learning Strategy**

* **Lectures:** Introduce weekly concepts with demonstrations.
* **Hands-on Labs:** Weekly practical exercises.
* **Group Work:** SSIS project work, Git collaboration.
* **Independent Study:** Reading, practice datasets, research.
* **Final Project:** Real ETL pipeline with documentation.

---

# 📅 **Weekly Breakdown**

A detailed breakdown is already included above. This syllabus references the week-by-week teaching plan for delivery.

---

# 🧪 **Assessment Structure**

### **1. Weekly Labs (30%)**

* SQL queries
* SSIS transformations
* Git exercises
* Automation tasks

### **2. Assignments (30%)**

* **Assignment 1:** SQL Analysis Report (Week 6)
* **Assignment 2:** ETL Pipeline Design Using SSIS (Week 14)
* **Assignment 3:** GitHub Documentation & Version Control (Week 20)

### **3. Final Capstone Project (40%)**

A fully documented Data Engineering pipeline:

* Extract data from multiple sources (CSV, SQL)
* Transform data (cleansing, standardisation, lookups)
* Load into warehouse tables (Fact & Dimension)
* Automate refresh via SQL Agent Job
* Submit on GitHub with README

Rubric includes:

* Technical accuracy (40%)
* Documentation (20%)
* Code quality (20%)
* Presentation (20%)

---

# 📚 **Recommended Reading & Resources**

### **Books**

* *The Data Warehouse Toolkit* — Ralph Kimball
* *SQL for Data Analysis* — O’Reilly
* *Fundamentals of Data Engineering* — Joe Reis & Matt Housley

### **Online Platforms**

* Microsoft Learn (SSIS + SQL)
* SQLBolt
* LeetCode (SQL)
* GitHub Learning Lab

---

# 🖥️ **Software Requirements**

* SQL Server + SSMS
* SSIS via SQL Server Data Tools
* Visual Studio / VS Code
* Git & GitHub
* PowerShell / Python
* Optional: Power BI for dashboards

---

# 🏆 **Capstone Project Requirements**

Students must complete:

1. ERD + Dimensional Model (Fact & Dim tables)
2. SSIS ETL Pipeline (Extract–Transform–Load)
3. SQL Tables & Optimized Queries
4. Automation using SQL Jobs
5. GitHub Repository containing:

   * Code
   * Screenshots
   * Documentation (README)
   * Version history

---

# 🎤 **Final Presentation Guidelines**

Students must deliver:

* 10-minute demonstration of project
* Technical overview (ERD, ETL steps, optimisation)
* Challenges & solutions
* Q&A with lecturer panel

---

# ✔️ **Completion Requirements**

To pass the module, students must:

* Attend at least 70% of classes
* Submit all assignments
* Pass the capstone with at least 40%
* Demonstrate GitHub usage and documentation quality

---
