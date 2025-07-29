# **Amazon Scrapping**
This repository contains a Python script (main.py) that automates the process of logging into Amazon.in and scraping product titles and prices from multiple best-seller categories. The final output is saved to a CSV file (best_sellers.csv).

# **✨ Features**
🤖 Automates login to Amazon.in using Selenium

📦 Scrapes product titles and prices from top 10 best-seller categories (kitchen, electronics, books, etc.)

📄 Stores the extracted data into a CSV file for further analysis

# **🛠️ Requirements**
🐍 Python 3.x

🕷️ Selenium

🌐 Chrome WebDriver (compatible with your Chrome version)

# **📦 Install dependencies**
bash
pip install selenium
You’ll also need to download ChromeDriver and ensure it is in your system PATH.

# **🚀 Usage**
1. Clone this repo:

bash
git clone https://github.com/YOUR_USERNAME/Amazon-Scrapping.git
cd Amazon-Scrapping
2. Edit credentials:
Open main.py, and replace the placeholders for username and password with your Amazon.in login credentials:

python
username = "your username"  # replace with your Amazon.in username
password = "your password"  # replace with your Amazon.in password
3. Run the script:

bash
python main.py
The script will log in to Amazon, scrape data, and produce a best_sellers.csv file in the same directory.

# **📊 Output**
A file named best_sellers.csv containing all scraped product titles and prices.

# **⚠️ Notes**
1. For personal/educational use only. Scraping commercial sites may violate their Terms of Service. Use responsibly!

2. If Amazon uses CAPTCHAs, 2FA, or changes its layout, the script may require updates.

3. Browser automation with Selenium may require ChromeDriver to be in your PATH, or specify its location in the script:

python
driver = webdriver.Chrome(executable_path='PATH_TO_CHROMEDRIVER')
# **⚠️ Disclaimer**
This project is for educational purposes only. Use at your own risk.
