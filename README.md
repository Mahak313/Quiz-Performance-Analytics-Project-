# 📊 Quiz Performance Analytics Dashboard  
**End-to-End Data Analytics Project | Python • SQL Server • Power BI**

> A real-world analytics project built using **live data from Skill Guru Foundation**, showcasing the complete data pipeline from raw data cleaning to interactive business intelligence dashboards.

---

## 🌟 Project Overview

This project analyzes **quiz participation, completion trends, user engagement, and performance metrics** using production-level data from the **Skill Guru Foundation** platform.

The objective was to transform raw, unstructured data into meaningful business insights through a structured analytics workflow:

- **Python** for data cleaning & preprocessing  
- **SQL Server** for data storage & modeling  
- **Power BI** for visualization & dashboarding  

The result is a **professional, interactive dashboard** that supports data-driven decision-making in an educational environment.

---

## 🎯 Objectives

- Analyze quiz performance across subjects, days, schools, and modes  
- Identify participation and completion trends  
- Understand user engagement behavior  
- Demonstrate an **end-to-end analytics pipeline**  
- Build a recruiter-ready BI dashboard  

---

## 🗂️ Data Source (Live Data)

- 📌 **Source:** Skill Guru Foundation (Live Platform Data)  
- 📌 **Includes:**  
  - Quiz details (ID, type, status, participants, scores)  
  - User information (location, ratings, referrals, wallet)  
  - Timestamps (create, start, complete dates)  

✔ Data was handled ethically and used strictly for analytical and educational purposes.

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|--------|
| **Python (Pandas, NumPy)** | Data cleaning, preprocessing, validation |
| **SQL Server** | Data storage, transformation, modeling |
| **Power BI** | Data visualization & dashboard creation |
| **Excel / CSV** | Initial data extraction |

---

## 🔁 End-to-End Data Pipeline

Live Data (Skill Guru Foundation)
↓
Python (Cleaning & Preprocessing)
↓
SQL Server (Staging Tables)
↓
SQL Data Modeling (Fact & Dimension Tables)
↓
Power BI (Dashboard & Insights)


---

## 🧹 Data Cleaning with Python

Using **Python (Pandas)**, the following steps were performed:

- Removed duplicates and handled missing values  
- Standardized column names and formats  
- Converted text fields into:
  - Numeric values (participants, scores, ratings)  
  - DateTime values (create, start, complete dates)  
- Fixed inconsistent and invalid entries  
- Validated data before database insertion  

---

## 🔗 Python → SQL Server Integration

- Established database connection using **`pyodbc` / `SQLAlchemy`**  
- Inserted cleaned datasets into SQL Server staging tables  
- Applied data type validation and error handling  
- Automated the data loading workflow  

---

## 🗃️ Data Modeling in SQL Server

To support analytics, structured tables were created:

### 📌 Dimension Table: `dim_user`
Stores user-level attributes:
- User ID, Name, Email  
- Gender, City, State, School  
- Ratings (Learner, Guru)  
- Wallet Balance, Referrals  
- Created & Updated Timestamps  

### 📌 Fact Table: `fact_quiz`
Stores measurable quiz performance:
- Quiz ID  
- Creator/User Reference  
- Participants  
- Completed Users  
- Winner Score  
- Completion Ratio (KPI)  
- Quiz Dates  

✔ This structure enables fast querying, clean relationships, and scalable reporting.

---

## 📊 Power BI Integration

- Connected **Power BI directly to SQL Server**  
- Imported fact and dimension tables  
- Built data relationships  
- Created calculated measures and KPIs  
- Designed a **sky-themed, interactive dashboard**  

---

## 📈 Dashboard Highlights

The dashboard provides insights such as:

- 🔹 **Total Quizzes**  
- 🔹 **Total Participants**  
- 🔹 **Completed Users**  
- 🔹 **Monthly Participation Trends**  
- 🔹 **Quiz Completion by Subject**  
- 🔹 **Performance by Difficulty Level**  
- 🔹 **Quiz Status Distribution**  
- 🔹 **Completed Users by School**  
- 🔹 **User Engagement by Day**  
- 🔹 **Mode-wise Quiz Analysis (Live vs 1v1)**  

---


## 💡 Business Insights

- Identified **high-performing subjects**  
- Discovered **best days for user engagement**  
- Highlighted **schools with highest completion rates**  
- Compared **effectiveness of quiz modes**  
- Revealed real-world user behavior patterns  

---

## 🎓 Use Cases & Impact

- Helps educational platforms monitor learner engagement  
- Supports data-driven quiz scheduling  
- Identifies improvement areas in content strategy  
- Enhances performance tracking using real-world data  

---

## 🧠 Skills Demonstrated

- **Python:** Pandas, Data Cleaning, Preprocessing  
- **SQL:** Data Modeling, Fact & Dimension Tables, KPI calculations  
- **Power BI:** Dashboard Design, Data Visualization  
- **Analytics:** Business Insights, Reporting, Decision Support  

---


## 👩‍💻 Author & Contact

**Mahak Shrivastav**  
Aspiring Data Analyst | Business Intelligence Enthusiast  

📧 Email:  muskaanrastogi13@gmail.com 

🔗 LinkedIn:  www.linkedin.com/in/mahakshrivastav


📌 *Open to Data Analyst / BI Analyst opportunities*  

--------------------------------------------------


