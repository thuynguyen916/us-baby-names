# US Baby Name Popularity (2000–2023)

This project explores the most popular baby names in the United States from 2000 to 2023 — aka the Gen Z and Gen Alpha naming era, when names got ✨creative✨ and spelling became optional.

---

## 🔍 Features
- Search any baby name to view its popularity trend over time
- See gender distribution by percentage (F/M)
- Discover the most to least popular years based on birth count
- Forecast future name trends using Tableau’s built-in model

---

## 🗂️ Project Structure

- `README.md` – Project overview and documentation

- `cleaned-data/`
  - `us_baby_names.csv` – Combined dataset from 24 raw SSA files

- `data/`
  - (Not included in repo) Raw SSA files: `yob2000.txt` to `yob2023.txt`

- `images/`
  - `Dashboard.jpg` – Final dashboard preview
  - `csv-file-execution.jpg` – Python script output preview

- `scripts/`
  - `us_baby_names.py` – Python script to process and merge the raw `.txt` files

- `tableau/`
  - `US-Baby-Name-popularity.twbx` – Tableau Packaged Workbook (interactive dashboard)


## 🛠 Tools & Technologies
- **Python (Pandas)** – for data wrangling and merging 24 SSA `.txt` files into a unified dataset
- **Tableau Public** – for building the interactive dashboard

---

## 📂 Files Included
- `us_baby_names.py` – Python script to convert 24 raw `.txt` files to a cleaned CSV
- `us_baby_names.csv` – Final dataset (output from script)
- `US-Baby-Name-popularity.twbx` – Tableau workbook (packaged)
- `yobXXXX.txt` – SSA raw files for each year (2000-2023)

---

## 📊 Interactive Dashboard
Check it out here:  
🔗 [US Baby Name Popularity (Tableau)](https://public.tableau.com/app/profile/thuy.nguyen8558/viz/USBabyNamepopularity/Dashboard)

---

## 🎯 Results & Impact
This dashboard allows users to:
- Discover when their name peaked in popularity and how it's changed over time
- Understand gender trends behind common names
- Compare naming patterns across generations

By combining data wrangling with visual storytelling, this project makes demographic insights both accessible and engaging — empowering parents, analysts, and the data-curious alike.

---

## 👩‍💻 Author
**Thuy Nguyen**  
📧 [thuy.nguyen.gl00@gmail.com]  
🔗 [LinkedIn](www.linkedin.com/in/thuynguyen0916)  
📊 [Tableau Public](https://public.tableau.com/app/profile/thuy.nguyen8558)
