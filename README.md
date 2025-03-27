# 🎯 **TalentEdge Course Scraper**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Scrapy](https://img.shields.io/badge/Scrapy-2.11.0-green?style=for-the-badge&logo=scrapy)
![Pandas](https://img.shields.io/badge/Pandas-1.5.3-orange?style=for-the-badge&logo=pandas)
![Excel](https://img.shields.io/badge/Excel-Data%20Export-brightgreen?style=for-the-badge&logo=microsoft-excel)

## 🚀 **Project Overview**
This project is a web scraper built using `Scrapy` to extract detailed course information from [TalentEdge](https://talentedge.com). The scraper navigates through course pages and collects data, including:
- **Course Title**
- **Description**
- **Duration, Timing & Start Date**
- **Skills & Learning Outcomes**
- **Eligibility Criteria**
- **Topics Covered**
- **Faculty Information (Names, Designations, Descriptions)**
- **Institute Name**
- **Course Fee in INR & USD**
- **Target Audience**

The extracted data is saved in a structured Excel file for easy reference and analysis. ✅

---

## ⚙️ **Tech Stack**
- **Language:** Python 3.8+
- **Libraries:** 
  - `Scrapy` → For web scraping  
  - `Pandas` → For data manipulation and export  
  - `OpenPyXL` → For Excel handling  
- **Data Format:** Excel (`.xlsx`)

---

## 📊 **Directory Structure**
```
📁 TalentEdge-Scraper  
 ├── 📄 README.md             → Project documentation  
 ├── 📄 requirements.txt      → List of dependencies  
 ├── 📄 course_data.xlsx      → Output Excel file with scraped data  
 ├── 📄 scrapy.cfg            → Scrapy configuration  
 ├── 📁 spiders               → Spider scripts  
 │     └── data_spider.py     → Main scraper script  
 ├── 📁 logs                  → Logs for debugging  
 └── 📁 output                → (Optional) Store raw HTML or JSON files
```

---

## 🔧 **Installation**
1. **Clone the Repository**
```bash
git clone https://github.com/Nidhiii2/Web-Scraping-Project.git
cd TalentEdge-Scraper
```

2. **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate      # Windows
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 🚦 **Usage**
1. **Run the Scraper**
```bash
scrapy crawl data
```

2. **Output**
- The scraped data is saved in `course_data.xlsx`.
- The Excel file contains all the extracted course details in a tabular format.

---

## 🔥 **Features**
✔️ Extracts comprehensive course details from multiple pages  
✔️ Exports data into Excel format  
✔️ Handles missing data gracefully  
✔️ Supports dynamic crawling of multiple course URLs  

---

## 🛠️ **Customization**
You can easily add more course URLs by modifying the `start_requests()` method:
```python
urls = [
    "https://talentedge.com/iim-kozhikode/professional-certificate-programme-in-hr-management-and-analytics",
    "https://talentedge.com/iim-lucknow/supply-chain-management",
    "https://talentedge.com/iim-raipur/certificate-course-machine-learning-for-managers",
]
```
Add or remove URLs as required. 

---

## ✅ **Example Output**

| Course Title                                   | Duration    | Start Date     | Faculty               | Fee in INR   | Fee in USD    |
|------------------------------------------------|-------------|----------------|------------------------|--------------|----------------|
| HR Management & Analytics                      | 12 months   | Aug 2025       | Dr. XYZ (IIM K)        | INR 1,00,000 | USD 1,200      |
| Machine Learning for Managers                   | 6 months    | Sep 2025       | Prof. ABC (IIM Raipur) | INR 80,000   | USD 1,000      |
| Doctor of Business Administration (GGU)         | 36 months   | Rolling Basis  | Dr. DEF (GGU)          | INR 3,50,000 | USD 4,200      |

---

## ⚠️ **Error Handling & Logging**
- All errors are logged in the `logs/` folder.
- Graceful handling of missing or invalid data prevents script crashes.

---

## 📚 **Dependencies**
Install the necessary libraries by running:
```bash
pip install scrapy pandas openpyxl
```

---

## 📌 **Future Enhancements**
✅ Add support for JSON/CSV exports  
✅ Implement multi-threaded scraping for faster execution  
✅ Include dynamic course pagination scraping  

---

## 👩‍💻 **Author**
👋 Developed by **Nidhi Saroj**  
🔗 [LinkedIn](https://www.linkedin.com/in/nidhi-saroj-705b362a6/) | [GitHub](https://github.com/Nidhiii2)
