# Germany Data Talent Intelligence Platform

## 1. Business Problem

Fresh graduates and entry-level candidates in Germany often struggle to understand which data, BI, analytics, and AI skills are currently demanded by employers. Job descriptions are spread across multiple platforms, making it difficult to compare roles, required skills, locations, work models, and realistic entry-level opportunities.

This project solves that problem by collecting and analysing German data-related job postings to identify skill demand, role categories, language requirements, work models, and student-friendly or entry-level opportunities.

---

## 2. Project Objective

The objective of this project is to build a corporate-style data analytics workflow that transforms raw job postings into structured business insights.

The project answers questions such as:

- Which skills are most demanded in German data jobs?
- Which roles are most common: BI, Data Analytics, Data Engineering, or AI/ML?
- Which jobs are suitable for working students or entry-level candidates?
- Which tools appear most often in job descriptions?
- How important are SQL, Python, Tableau, Power BI, reporting, and data analysis?
- Which language requirements appear in job descriptions?
- Which work models are common: hybrid, remote, on-site, or unspecified?

---

## 3. Data Source

The dataset was manually collected from real German job descriptions related to:

- Working Student Data Analyst
- Working Student Business Intelligence
- Junior Data Analyst
- Junior Business Intelligence Analyst
- Junior Data Engineer
- Data Analytics Consultant
- BI / Reporting roles
- Data Engineering and analytics support roles

For each job posting, the dataset includes:

- Job title
- Company
- Location
- Employment type
- Work model
- Source
- Date collected
- Job description
- Extracted skills
- Role category
- Language requirement

---

## 4. Tech Stack

| Area | Technology |
|---|---|
| Data collection | Manual structured CSV collection |
| Data cleaning | Python, pandas |
| Skill extraction | Python, regex, rule-based matching |
| SQL analysis | DuckDB SQL |
| BI dashboard | Tableau |
| Version control | Git, GitHub |
| Future extension | PostgreSQL, Streamlit, Docker |

---

## 5. Project Architecture

```text
Raw job descriptions
        ↓
Python data cleaning
        ↓
Skill extraction pipeline
        ↓
Processed job dataset
        ↓
SQL analysis with DuckDB
        ↓
Tableau-ready datasets
        ↓
Tableau dashboards
        ↓
Business insights and career strategy
