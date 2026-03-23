# 🚀 Job Analytics Dashboard (Web Scraping + Data Analysis + Streamlit)

An end-to-end **Web Scraping + Interactive Dashboard** project that collects job postings, analyzes them, and visualizes insights using **Streamlit**.

---

# 📌 Project Overview

This project scrapes job postings from a website, extracts detailed information, performs analysis on job descriptions, and builds an **interactive dashboard** for exploring job market insights.

The pipeline:

```
Web Scraping → Visualization Dashboard
```

---

# 🕸️ Web Scraping

The scraper collects job postings from:

```
https://realpython.github.io/fake-jobs/
```

### Extracted Fields

* Job Title
* Company
* Location
* Description (from detail page)
* URL

### Features

* Deep scraping (visits each job detail page)
* Clean structured dataset
* CSV export
* Handles missing data

Output file:

```
detailed_jobs.csv
```

---

# 📊 Data Analysis & Dashboard Features

The Streamlit dashboard provides:

### 🔍 Search & Filter

* Search inside job descriptions
* Filter by company
* Dynamic dataset filtering

### 📈 Metrics

* Total Jobs Found
* Total Companies
* Average Description Length

### ☁️ WordCloud

* Extracts most common keywords
* Highlights important job skills

### 📍 Location Distribution

* Top job locations
* Horizontal bar chart

### 🏢 Company Distribution

* Treemap visualization
* Company market share

### 📋 Interactive Table

* Clickable job links
* Scrollable dataframe
* Clean UI

---

# 🖼️ Dataset Example

The scraped dataset contains structured job postings:

| Job Title        | Company   | Location | Description | URL  |
| ---------------- | --------- | -------- | ----------- | ---- |
| Data Scientist   | Company X | NY       | ...         | link |
| Python Developer | Company Y | Remote   | ...         | link |

---

# 🛠️ Tech Stack

* Python
* Requests
* BeautifulSoup
* Pandas
* Streamlit
* Plotly
* Matplotlib
* WordCloud

---

# 📂 Project Structure

```
Job-Analytics/
│
├── jobs_dataset.py        # Web Scraper
├── jobs_Dasjbored.py      # Streamlit Dashboard
├── detailed_jobs.csv      # Scraped dataset
├── README.md
```

---

# 🚀 How To Run

## 1. Install Requirements

```bash
pip install requests beautifulsoup4 pandas streamlit plotly matplotlib wordcloud
```

---

## 2. Run Web Scraper

```bash
python jobs_dataset.py
```

This will generate:

```
detailed_jobs.csv
```

---

## 3. Run Dashboard

```bash
streamlit run jobs_Dasjbored.py
```

---

# 📈 Example Insights

The dashboard helps answer:

* What are the most common job skills?
* Which companies post the most jobs?
* Where are jobs located?
* What keywords appear in job descriptions?

---

# 🎯 Project Goals

* Practice Web Scraping
* Perform Text Analysis
* Build Interactive Dashboard
* Create End-to-End Data Project
* Portfolio-ready Data Science Project

---

# 🧠 Future Improvements

* Add NLP skill extraction
* Add salary analysis
* Deploy on Streamlit Cloud
* Add job category classification
* Add sentiment analysis

---

# 👨‍💻 Author

Built as a **Data Analytics / Data Science Portfolio Project**
Using Web Scraping + Visualization + Streamlit Dashboard

---
